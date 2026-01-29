"""
Online Admission System with QR Code
Secure Flask application for collecting admission data
"""

from flask import Flask, render_template, request, jsonify, send_file, url_for, session, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from werkzeug.utils import secure_filename
from werkzeug.security import check_password_hash, generate_password_hash
import qrcode
import os
import secrets
from datetime import datetime
from io import BytesIO
import base64
import hashlib
from functools import wraps

# Configuration
app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex(32)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///admissions.db'
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024  # 10MB max file size
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0  # Disable caching
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif', 'webp'}

# Admin credentials (set your admin username/password)
ADMIN_USERNAME = os.environ.get('ADMIN_USERNAME', 'admin')
ADMIN_PASSWORD_HASH = generate_password_hash(os.environ.get('ADMIN_PASSWORD', 'egy$4119'))

# Initialize extensions
db = SQLAlchemy(app)
CORS(app)

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)


# Database Model
class Admission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    workplace = db.Column(db.String(200), nullable=False)
    nationality = db.Column(db.String(100), nullable=False)
    activity = db.Column(db.String(200), nullable=False)
    picture = db.Column(db.String(300), nullable=True)
    picture_hash = db.Column(db.String(64), nullable=True)
    submission_date = db.Column(db.DateTime, default=datetime.utcnow)
    ip_address = db.Column(db.String(50), nullable=True)
    status = db.Column(db.String(20), default='submitted')  # submitted, verified, approved
    notes = db.Column(db.Text, nullable=True)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'phone': self.phone,
            'workplace': self.workplace,
            'nationality': self.nationality,
            'activity': self.activity,
            'picture': self.picture,
            'submission_date': self.submission_date.isoformat(),
            'status': self.status
        }


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


def get_client_ip():
    """Get client IP address"""
    if request.headers.getlist("X-Forwarded-For"):
        return request.headers.getlist("X-Forwarded-For")[0]
    return request.remote_addr


def login_required(f):
    """Decorator to require admin login"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not session.get('admin_logged_in'):
            return redirect(url_for('admin_login'))
        return f(*args, **kwargs)
    return decorated_function


def generate_qr_code(data):
    """Generate QR code as base64 image"""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    
    # Convert to base64
    buffer = BytesIO()
    img.save(buffer, format='PNG')
    buffer.seek(0)
    img_base64 = base64.b64encode(buffer.getvalue()).decode()
    
    return img_base64


@app.route('/')
def index():
    """Main page with QR code"""
    # Generate QR code pointing to the form
    form_url = url_for('admission_form', _external=True)
    qr_code = generate_qr_code(form_url)
    
    return render_template('index.html', qr_code=qr_code, form_url=form_url)


@app.route('/admission-form')
def admission_form():
    """Admission form page"""
    return render_template('admission_form.html')


@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    """Admin login page"""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if username == ADMIN_USERNAME and check_password_hash(ADMIN_PASSWORD_HASH, password):
            session['admin_logged_in'] = True
            return redirect(url_for('admin_dashboard'))
        else:
            return render_template('admin_login.html', error='Invalid credentials')
    
    return render_template('admin_login.html')


@app.route('/admin/logout')
def admin_logout():
    """Admin logout"""
    session.pop('admin_logged_in', None)
    return redirect(url_for('admin_login'))


@app.route('/admin')
@login_required
def admin_dashboard():
    """Admin dashboard to view admissions"""
    return render_template('admin.html')


@app.route('/api/submit-admission', methods=['POST'])
def submit_admission():
    """Handle admission form submission"""
    try:
        # Validate required fields
        name = request.form.get('name', '').strip()
        phone = request.form.get('phone', '').strip()
        workplace = request.form.get('workplace', '').strip()
        nationality = request.form.get('nationality', '').strip()
        activity = request.form.get('activity', '').strip()

        if not name or not phone or not workplace or not nationality or not activity:
            return jsonify({'success': False, 'error': 'All fields are required'}), 400

        # Validate name (at least 2 characters, only letters and spaces)
        if len(name) < 2 or not all(c.isalpha() or c.isspace() for c in name):
            return jsonify({'success': False, 'error': 'Invalid name format'}), 400

        # Validate phone (10-20 digits)
        if not phone.replace('+', '').replace('-', '').replace(' ', '').isdigit() or len(phone) < 10:
            return jsonify({'success': False, 'error': 'Invalid phone number'}), 400

        if len(workplace) < 2:
            return jsonify({'success': False, 'error': 'Invalid workplace'}), 400

        if len(nationality) < 2:
            return jsonify({'success': False, 'error': 'Invalid nationality'}), 400

        if len(activity) < 2:
            return jsonify({'success': False, 'error': 'Invalid activity'}), 400

        # Handle image upload
        picture_filename = None
        picture_hash = None

        if 'picture' in request.files:
            file = request.files['picture']
            if file and file.filename and allowed_file(file.filename):
                # Generate secure filename
                timestamp = datetime.now().strftime('%Y%m%d_%H%M%S_')
                filename = secure_filename(file.filename)
                picture_filename = timestamp + filename

                # Save file
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], picture_filename)
                file.save(filepath)

                # Calculate file hash
                with open(filepath, 'rb') as f:
                    picture_hash = hashlib.sha256(f.read()).hexdigest()

            elif file and file.filename:
                return jsonify({'success': False, 'error': 'Invalid file format. Allowed: PNG, JPG, JPEG, GIF, WEBP'}), 400

        # Create admission record
        admission = Admission(
            name=name,
            phone=phone,
            workplace=workplace,
            nationality=nationality,
            activity=activity,
            picture=picture_filename,
            picture_hash=picture_hash,
            ip_address=get_client_ip()
        )

        db.session.add(admission)
        db.session.commit()

        return jsonify({
            'success': True,
            'message': 'Your admission form has been submitted successfully!',
            'admission_id': admission.id,
            'data': admission.to_dict()
        }), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/api/admissions', methods=['GET'])
@login_required
def get_admissions():
    """Get all admissions (admin endpoint)"""
    admissions = Admission.query.all()
    return jsonify([adm.to_dict() for adm in admissions])


@app.route('/api/admissions/<int:admission_id>', methods=['GET'])
@login_required
def get_admission(admission_id):
    """Get specific admission"""
    admission = Admission.query.get_or_404(admission_id)
    return jsonify(admission.to_dict())


@app.route('/api/admissions/<int:admission_id>/picture')
@login_required
def get_picture(admission_id):
    """Get admission picture"""
    admission = Admission.query.get_or_404(admission_id)
    if admission.picture:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], admission.picture)
        if os.path.exists(filepath):
            return send_file(filepath, mimetype='image/jpeg')
    return jsonify({'error': 'Picture not found'}), 404


@app.route('/api/health')
def health():
    """Health check endpoint"""
    return jsonify({'status': 'ok', 'timestamp': datetime.utcnow().isoformat()})


@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404


@app.errorhandler(500)
def server_error(error):
    db.session.rollback()
    return jsonify({'error': 'Internal server error'}), 500


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_ENV') == 'development'
    
    app.run(debug=debug, host='0.0.0.0', port=port)
