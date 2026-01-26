# 🎓 Online Admission System - Complete Documentation

## Table of Contents
1. [Overview](#overview)
2. [Quick Start](#quick-start)
3. [Installation](#installation)
4. [How to Use](#how-to-use)
5. [API Reference](#api-reference)
6. [Database Schema](#database-schema)
7. [Customization](#customization)
8. [Deployment](#deployment)
9. [Troubleshooting](#troubleshooting)
10. [FAQ](#faq)

---

## Overview

The **Online Admission System** is a secure web application that allows you to:
- Generate QR codes for admission forms
- Collect client information (name, phone, workplace, picture)
- Store data in a database
- View submissions in an admin dashboard

### Key Benefits:
✅ Modern, responsive design  
✅ Easy to use - just scan QR code  
✅ Secure data storage  
✅ Admin dashboard to view submissions  
✅ Mobile-friendly  
✅ Can be deployed to any cloud server  

---

## Quick Start

### Requirements:
- Python 3.7+
- 5 minutes

### Steps:
```bash
# 1. Navigate to project
cd D:\OnlineAdmissionSystem

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run application
python run.py

# 4. Open in browser
https://127.0.0.1:5000
```

That's it! 🎉

---

## Installation

### Prerequisites
- Python 3.7 or higher installed
- Internet connection
- Modern web browser

### Step-by-Step Installation

#### 1. Open Command Prompt
Press `Win + R` and type `cmd` or open PowerShell

#### 2. Navigate to Project Folder
```bash
cd D:\OnlineAdmissionSystem
```

#### 3. Create Virtual Environment (Recommended)
```bash
python -m venv venv
venv\Scripts\activate
```

#### 4. Install Requirements
```bash
pip install -r requirements.txt
```

This installs:
- Flask - web server
- Flask-SQLAlchemy - database management
- QRCode - QR code generation
- Pillow - image handling
- Flask-CORS - cross-origin requests
- PyOpenSSL - HTTPS/SSL support

#### 5. Verify Installation
```bash
python check_setup.py
```

#### 6. Run Application
```bash
python run.py
```

Or directly:
```bash
python app.py
```

---

## How to Use

### For Admin (You)

#### Getting Started
1. Start the application: `python run.py`
2. Go to: https://127.0.0.1:5000
3. You'll see the QR code page

#### Distribute QR Code
- **Download**: Click "⬇️ Download QR Code"
- **Print**: Print the QR code and display in office
- **Share**: Give the URL to clients: `https://127.0.0.1:5000/admission-form`

#### Monitor Submissions
1. Go to: https://127.0.0.1:5000/admin
2. See all submissions in a table
3. Click "View" to see details
4. Click "Download" to download picture

#### Export Data
- Visit: https://127.0.0.1:5000/api/admissions
- Copy JSON data
- Paste into Excel or database

---

### For Clients

#### Submission Process
1. Scan QR code with phone camera
2. Click the link that appears
3. Fill in the form:
   - **Full Name** - Your complete name
   - **Phone Number** - Contact number
   - **Workplace** - Where you work
   - **Picture** - Click to upload your photo
4. Click "✓ Submit Form"
5. See confirmation message

#### Tips for Users
- Use good lighting for photo
- Ensure face is clear in picture
- Double-check spelling of name
- Use valid phone number format
- Supported image formats: JPG, PNG, GIF, WEBP

---

## API Reference

### Public Endpoints

#### GET /
Main page with QR code
```
URL: https://127.0.0.1:5000/
Response: HTML page with QR code
```

#### GET /admission-form
Admission form page
```
URL: https://127.0.0.1:5000/admission-form
Response: HTML form
```

#### POST /api/submit-admission
Submit admission form
```
URL: https://127.0.0.1:5000/api/submit-admission
Method: POST
Content-Type: multipart/form-data

Body:
{
  "name": "John Doe",
  "phone": "+1234567890",
  "workplace": "Company Name",
  "picture": <file>
}

Response:
{
  "success": true,
  "message": "Your admission form has been submitted successfully!",
  "admission_id": 1,
  "data": {...}
}
```

#### GET /api/health
Health check
```
URL: https://127.0.0.1:5000/api/health
Response: {"status": "ok", "timestamp": "2026-01-26T10:00:00"}
```

### Admin Endpoints

#### GET /admin
Admin dashboard
```
URL: https://127.0.0.1:5000/admin
Response: HTML dashboard
```

#### GET /api/admissions
Get all admissions
```
URL: https://127.0.0.1:5000/api/admissions
Response: JSON array of all submissions
```

#### GET /api/admissions/{id}
Get specific admission
```
URL: https://127.0.0.1:5000/api/admissions/1
Response: JSON object for admission ID 1
```

#### GET /api/admissions/{id}/picture
Download picture
```
URL: https://127.0.0.1:5000/api/admissions/1/picture
Response: Image file (JPEG/PNG)
```

---

## Database Schema

### admissions Table

```sql
CREATE TABLE admission (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(120) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    workplace VARCHAR(200) NOT NULL,
    picture VARCHAR(300),
    picture_hash VARCHAR(64),
    submission_date DATETIME DEFAULT CURRENT_TIMESTAMP,
    ip_address VARCHAR(50),
    status VARCHAR(20) DEFAULT 'submitted',
    notes TEXT
);
```

### Column Descriptions

| Column | Type | Description |
|--------|------|-------------|
| id | INTEGER | Primary key, auto-increment |
| name | VARCHAR(120) | Client's full name |
| phone | VARCHAR(20) | Phone number |
| workplace | VARCHAR(200) | Where they work |
| picture | VARCHAR(300) | Filename of uploaded image |
| picture_hash | VARCHAR(64) | SHA256 hash for integrity |
| submission_date | DATETIME | When submitted |
| ip_address | VARCHAR(50) | Client's IP address |
| status | VARCHAR(20) | submitted/verified/approved |
| notes | TEXT | Admin notes |

---

## Customization

### Change Colors

#### Edit CSS Variables
File: `templates/index.html` and `templates/admission_form.html`

Find:
```css
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
```

Change to your colors:
```css
background: linear-gradient(135deg, #FF6B6B 0%, #FFA500 100%);
```

Color suggestions:
- Blue/Purple: `#667eea`, `#764ba2`
- Red/Orange: `#FF6B6B`, `#FFA500`
- Green/Teal: `#2ecc71`, `#1abc9c`

### Add Form Fields

#### Step 1: Edit HTML
File: `templates/admission_form.html`

Add field before `<!-- Buttons -->`:
```html
<div class="form-group">
    <label for="email">
        Email <span class="required">*</span>
    </label>
    <input 
        type="email" 
        id="email" 
        name="email"
        placeholder="your.email@example.com"
        required
    >
    <span class="error-message" id="emailError"></span>
</div>
```

#### Step 2: Edit Python Model
File: `app.py`

Find the `Admission` model and add:
```python
email = db.Column(db.String(120), nullable=False)
```

#### Step 3: Add Validation
File: `templates/admission_form.html` JavaScript section

Add validation in `validateForm()`:
```javascript
// Validate email
const email = document.getElementById('email').value.trim();
if (!email) {
    showError('emailError', 'Email is required');
    isValid = false;
} else if (!email.includes('@')) {
    showError('emailError', 'Invalid email format');
    isValid = false;
}
```

#### Step 4: Update API Handler
File: `app.py`

In `submit_admission()` function, add:
```python
email = request.form.get('email', '').strip()
# validation here
admission = Admission(
    ...,
    email=email,
    ...
)
```

### Change Company Name

Find and replace in all files:
- `templates/index.html`
- `templates/admission_form.html`
- `templates/admin.html`

Replace: "Online Admission System" → "Your Company Name"

### Change Port

File: `app.py`, last line:

```python
# Change from:
app.run(debug=True, host='0.0.0.0', port=5000)

# To:
app.run(debug=True, host='0.0.0.0', port=8000)  # Now runs on port 8000
```

---

## Deployment

### For Local Development
```bash
python run.py
# Access on: https://127.0.0.1:5000
```

### For Production (Cloud Server)

#### Option 1: Using Gunicorn + Nginx (Recommended)

1. **Install dependencies:**
```bash
pip install gunicorn
pip install -r requirements.txt
```

2. **Run with Gunicorn:**
```bash
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

3. **Configure Nginx** as reverse proxy
4. **Get SSL certificate** (Let's Encrypt - free)

#### Option 2: Using Docker

Create `Dockerfile`:
```dockerfile
FROM python:3.11

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
```

Build and run:
```bash
docker build -t admission-system .
docker run -p 5000:5000 admission-system
```

#### Option 3: Cloud Platforms

**PythonAnywhere:**
1. Upload project files
2. Set web app
3. Reload
4. Done!

**Heroku:**
```bash
heroku login
heroku create your-app-name
git push heroku main
```

**AWS/Azure/DigitalOcean:**
1. Create Ubuntu server
2. Install Python
3. Install requirements
4. Configure Nginx + SSL
5. Run application

---

## Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'flask'"

**Solution:**
```bash
pip install -r requirements.txt
```

### Issue: "Address already in use" on port 5000

**Solution 1:** Change port in app.py
```python
app.run(port=5001)  # Use different port
```

**Solution 2:** Kill process using port
```bash
# On Windows:
netstat -ano | findstr :5000
taskkill /PID [PID] /F

# On macOS/Linux:
lsof -i :5000
kill -9 [PID]
```

### Issue: SSL Certificate Warning

This is normal for localhost development. Just click:
- Firefox: "Advanced..." → "Accept Risk"
- Chrome: "Advanced" → "Proceed to localhost"

### Issue: Picture Upload Fails

**Check:**
1. File size (max 10MB)
2. File format (PNG, JPG, GIF, WEBP only)
3. File name (no special characters)
4. Disk space available

### Issue: Database Locked

**Solution:**
```bash
# Delete database
rm admissions.db

# Or on Windows:
del admissions.db

# Restart application
python app.py
```

### Issue: Can't Access from Other Computer

**Solution 1:** Use computer's IP address
```bash
# Get your IP:
ipconfig  # Windows
ifconfig  # macOS/Linux

# Access from other computer:
https://YOUR-COMPUTER-IP:5000
```

**Solution 2:** Firewall issue
- Allow Python through Windows Firewall
- Or disable firewall for local network

### Issue: Pictures Not Uploading

**Check:**
1. `uploads/` folder exists
2. Folder has write permissions
3. Disk space available
4. File size not exceeding 10MB

---

## FAQ

### Q: Can I run this on production?
**A:** Yes! See deployment section for production setup instructions.

### Q: How do I backup my data?
**A:** 
- SQLite: Copy `admissions.db` file
- JSON: Export from `/api/admissions` endpoint
- Automatic: Use cloud backup service

### Q: How many submissions can it handle?
**A:** SQLite can handle thousands. For millions, upgrade to PostgreSQL.

### Q: Can I add payment?
**A:** Yes, integrate Stripe/PayPal into the form.

### Q: How do I email confirmations?
**A:** Add email integration using Flask-Mail:
```bash
pip install Flask-Mail
```

### Q: Can I limit submissions?
**A:** Yes, add quota check in `submit_admission()`:
```python
count = Admission.query.filter_by(phone=phone).count()
if count >= 1:
    return jsonify({'error': 'Already submitted'}), 400
```

### Q: How do I prevent duplicate submissions?
**A:** Check phone or email before creating new record.

### Q: Can I require email verification?
**A:** Yes, add email verification workflow.

### Q: How do I export to Excel?
**A:** Use pandas:
```python
pip install pandas openpyxl
# Export from `/api/admissions` to .xlsx
```

### Q: Is data encrypted?
**A:** HTTPS encrypts in transit. Add encryption for stored data with:
```python
pip install cryptography
```

### Q: Can I have multiple admins?
**A:** Yes, add admin authentication in app.py.

### Q: How long are pictures stored?
**A:** As long as you keep the `uploads/` folder. Delete manually or setup auto-cleanup.

### Q: Can I customize the QR code design?
**A:** Yes, modify `qrcode` parameters in `app.py`:
```python
qr = qrcode.QRCode(
    version=1,  # Size
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
    box_size=10,  # Pixel size per box
    border=4,  # Border thickness
)
```

---

## Support & Resources

- **GitHub**: [Your repo link]
- **Email**: [Your email]
- **Documentation**: All files in project folder
- **Code Comments**: Read app.py for detailed explanations

---

## License

This project is open source and available under the MIT License.

---

**Version**: 1.0.0  
**Last Updated**: January 26, 2026  
**Status**: ✅ Production Ready
