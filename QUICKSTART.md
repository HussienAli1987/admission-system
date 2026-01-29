## 🚀 Quick Start Guide - Online Admission System

### Step 1: Install Python Requirements
```bash
cd D:\OnlineAdmissionSystem
pip install -r requirements.txt
```

### Step 2: Run the Application
```bash
python app.py
```

You should see:
```
 * Running on https://127.0.0.1:5000
```

### Step 3: Access the Application

**Main Page (QR Code Display):**
- URL: `https://127.0.0.1:5000/`
- Shows: QR code + link to admission form
- Download QR code or share link with clients

**Admission Form:**
- URL: `https://127.0.0.1:5000/admission-form`
- Users fill in: Name, Phone, Workplace, Picture

**Admin Dashboard:**
- URL: `https://127.0.0.1:5000/admin`
- View all submissions in a table format
- Click "View" to see full details
- Click "Download" to download pictures

---

## 📱 How to Use (For Your Clients)

1. **Scan QR Code** with phone camera
2. **Fill Form** with their information:
   - Full Name
   - Phone Number
   - Work Place
   - Personal Picture (JPG/PNG)
3. **Click Submit**
4. **See Confirmation** message

---

## 🛠️ Features Implemented

✅ QR Code Generation  
✅ Responsive Web Form  
✅ Image Upload with Validation  
✅ Client-side Validation  
✅ Server-side Validation  
✅ Database Storage (SQLite)  
✅ Admin Dashboard  
✅ Security Features  
✅ File Hash Tracking  
✅ IP Address Logging  

---

## 📊 Database

The system automatically creates `admissions.db` with this structure:

| Column | Type | Description |
|--------|------|-------------|
| id | INTEGER | Primary key |
| name | VARCHAR | User's full name |
| phone | VARCHAR | Phone number |
| workplace | VARCHAR | Work place |
| picture | VARCHAR | Filename of uploaded picture |
| picture_hash | VARCHAR | SHA256 hash of file |
| submission_date | DATETIME | When submitted |
| ip_address | VARCHAR | Client IP address |
| status | VARCHAR | submitted/verified/approved |
| notes | TEXT | Admin notes |

---

## 🔒 Security Features

✓ Input validation (name, phone format)  
✓ File type whitelist (PNG, JPG, GIF, WEBP)  
✓ File size limit (10MB)  
✓ HTTPS support  
✓ Secure file naming (timestamp-based)  
✓ File integrity tracking (SHA256 hash)  
✓ CORS enabled  
✓ SQL injection protection (SQLAlchemy ORM)  

---

## 📡 API Endpoints

### Public
- `GET /` - Main page with QR code
- `GET /admission-form` - Admission form
- `POST /api/submit-admission` - Submit form
- `GET /api/health` - Health check

### Admin
- `GET /admin` - Admin dashboard
- `GET /api/admissions` - List all (JSON)
- `GET /api/admissions/<id>` - Get one (JSON)
- `GET /api/admissions/<id>/picture` - Download picture

---

## 🐛 Troubleshooting

**Issue**: Port 5000 already in use
```bash
# Change port in app.py:
app.run(debug=True, host='0.0.0.0', port=5001)  # Use 5001 instead
```

**Issue**: "Module not found"
```bash
pip install -r requirements.txt
```

**Issue**: Picture upload fails
- Check file size (max 10MB)
- Check format (PNG, JPG, GIF, WEBP only)

**Issue**: Database errors
```bash
# Delete the database and restart
rm admissions.db
python app.py
```

---

## 🌐 Deployment

### For Testing (Your Machine)
```bash
python app.py
# Opens on https://127.0.0.1:5000
```

### For Production (Cloud Server)

1. **Install on server:**
```bash
pip install -r requirements.txt
pip install gunicorn
```

2. **Run with Gunicorn:**
```bash
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

3. **Use HTTPS (Let's Encrypt):**
- Get free SSL certificate
- Configure reverse proxy (Nginx)
- Enable HTTPS

4. **Use PostgreSQL:**
- Change `SQLALCHEMY_DATABASE_URI` to PostgreSQL
- More reliable than SQLite

---

## 📝 Customization

### Add Form Field

1. **Edit admission_form.html** - Add input field
2. **Edit app.py** - Add column to Admission model
3. **Edit validation** - Add JavaScript validation

### Change Colors

Edit CSS in templates (primary: `#667eea`, secondary: `#764ba2`)

### Change Company Name

Search and replace throughout templates

---

## 💡 Tips

1. **Share QR Code**: Print it and display in office
2. **Monitor Submissions**: Check `/admin` dashboard
3. **Backup Data**: Regularly backup `admissions.db`
4. **Export Data**: Use `/api/admissions` to export as JSON

---

## ✨ What's Next?

Add more features:
- Email notifications
- Payment integration
- Document upload
- Admin approval workflow
- Email verification
- SMS notifications
- Analytics dashboard

---

**Version**: 1.0.0  
**Created**: January 2026  
**Support**: For issues, check README.md or troubleshooting section
