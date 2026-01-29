# Online Admission System with QR Code

A secure, modern web application for collecting admission information through QR code scanning.

## Features

✅ **QR Code Generation** - Generates unique QR codes pointing to the admission form  
✅ **Responsive Design** - Works on desktop, tablet, and mobile devices  
✅ **Image Upload** - Secure file upload with validation  
✅ **Data Validation** - Client-side and server-side validation  
✅ **Database Storage** - SQLite database for storing submissions  
✅ **Security** - HTTPS support, file type validation, input sanitization  
✅ **Admin API** - Endpoints to view submissions  

## Project Structure

```
OnlineAdmissionSystem/
├── app.py                 # Flask backend application
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── templates/
│   ├── index.html        # QR code display page
│   └── admission_form.html # Admission form page
├── static/               # CSS, JS files (if needed)
├── uploads/              # Uploaded pictures
└── admissions.db         # SQLite database (auto-created)
```

## Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Setup Steps

1. **Clone/Extract the project**
```bash
cd OnlineAdmissionSystem
```

2. **Create a virtual environment (recommended)**
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the application**
```bash
python app.py
```

5. **Access the application**
- Open your browser and go to `https://127.0.0.1:5000`
- The QR code will be displayed on the main page
- Scan it or click "Go to Form" to access the admission form

## How It Works

### For Admins
1. Go to `https://127.0.0.1:5000/` to see the QR code
2. Download the QR code or share the link
3. Access `/api/admissions` to view all submissions (JSON format)

### For Users
1. Scan the QR code with their phone camera or QR scanner app
2. Fill in the admission form:
   - Full Name
   - Phone Number
   - Work Place
   - Personal Picture (JPG, PNG, GIF, or WEBP)
3. Click "Submit Form"
4. Receive confirmation

## API Endpoints

### Public Endpoints
- `GET /` - Main page with QR code
- `GET /admission-form` - Admission form page
- `POST /api/submit-admission` - Submit admission form
- `GET /api/health` - Health check

### Admin Endpoints
- `GET /api/admissions` - Get all admissions (returns JSON)
- `GET /api/admissions/<id>` - Get specific admission
- `GET /api/admissions/<id>/picture` - Download picture

## Configuration

### File Uploads
- **Maximum file size**: 10 MB
- **Allowed formats**: PNG, JPG, JPEG, GIF, WEBP
- **Storage**: `uploads/` directory

### Database
- **Type**: SQLite
- **Location**: `admissions.db` (auto-created)

## Security Features

🔒 **Security Measures:**
- Input validation (name, phone, workplace)
- File type validation
- File size limits
- Secure file naming (timestamp-based)
- File hash for integrity
- CORS enabled
- HTTPS support

## Customization

### Change Port
Edit `app.py` and modify:
```python
app.run(debug=True, host='0.0.0.0', port=5000)
# Change 5000 to your desired port
```

### Change Colors
Edit `templates/index.html` and `templates/admission_form.html`:
```css
--primary-color: #667eea;
--secondary-color: #764ba2;
```

### Add Form Fields
1. Add input field in `templates/admission_form.html`
2. Add validation in JavaScript
3. Add column in `Admission` model in `app.py`
4. Add to form submission handler

## Database Schema

### Admissions Table
```sql
CREATE TABLE admission (
    id INTEGER PRIMARY KEY,
    name VARCHAR(120) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    workplace VARCHAR(200) NOT NULL,
    picture VARCHAR(300),
    picture_hash VARCHAR(64),
    submission_date DATETIME DEFAULT NOW,
    ip_address VARCHAR(50),
    status VARCHAR(20) DEFAULT 'submitted',
    notes TEXT
);
```

## Troubleshooting

### Issue: "Module not found" error
**Solution**: Install requirements again
```bash
pip install -r requirements.txt
```

### Issue: Port already in use
**Solution**: Change the port in `app.py` or kill the process using the port

### Issue: Picture upload fails
**Solution**: Check file size (max 10MB) and format (PNG, JPG, GIF, WEBP)

### Issue: Database errors
**Solution**: Delete `admissions.db` and restart the application

## Production Deployment

### For Production Use:

1. **Use a production server**
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

2. **Use environment variables**
```bash
export FLASK_ENV=production
export SECRET_KEY=your-secret-key-here
```

3. **Enable HTTPS**
- Get SSL certificate (Let's Encrypt)
- Configure in production server

4. **Database**
- Use PostgreSQL instead of SQLite for production

5. **File Storage**
- Use cloud storage (AWS S3, Azure Blob) instead of local filesystem

## License

This project is open source and available for educational purposes.

## Support

For issues or questions, please create an issue or contact the development team.

---

**Created**: January 2026  
**Version**: 1.0.0
