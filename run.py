#!/usr/bin/env python3
"""
Easy launcher for Online Admission System
Run this file to start the application
"""

import os
import sys
import webbrowser
import time
from pathlib import Path

def main():
    print("\n" + "="*60)
    print("🎓  Online Admission System - Launcher")
    print("="*60 + "\n")

    # Check if requirements are installed
    try:
        import flask
        import flask_sqlalchemy
        import qrcode
    except ImportError:
        print("❌ Dependencies not installed!\n")
        print("Installing required packages...")
        os.system("pip install -r requirements.txt")
        print("\n✅ Dependencies installed!\n")

    # Change to app directory
    app_dir = Path(__file__).parent
    os.chdir(app_dir)

    # Create uploads folder if needed
    uploads_dir = app_dir / "uploads"
    uploads_dir.mkdir(exist_ok=True)

    print("📁 Project directory:", app_dir)
    print("📦 Database: admissions.db")
    print("📂 Uploads folder: uploads/\n")

    print("Starting application...\n")
    print("-" * 60)

    # Try to import and run
    try:
        from app import app, db
        
        # Create tables
        with app.app_context():
            db.create_all()
            print("✅ Database initialized")

        print("\n🌐 Application URLs:")
        print("   QR Code Page:    https://127.0.0.1:5000/")
        print("   Admission Form:  https://127.0.0.1:5000/admission-form")
        print("   Admin Dashboard: https://127.0.0.1:5000/admin")
        print("   API:             https://127.0.0.1:5000/api/admissions")

        print("\n💡 Note: You may see SSL certificate warning (normal for local)")
        print("   Just click 'Proceed' or 'Advanced' to continue\n")
        print("-" * 60)

        # Ask if user wants to open browser
        time.sleep(2)
        try:
            response = input("\n🔗 Open in browser now? (y/n): ").strip().lower()
            if response == 'y':
                time.sleep(2)
                webbrowser.open('https://127.0.0.1:5000', new=2)
        except:
            pass

        print("\n⏳ Starting server...\n")
        app.run(debug=True, host='0.0.0.0', port=5000, ssl_context='adhoc')

    except ImportError as e:
        print(f"\n❌ Error: {e}")
        print("\nPlease run:")
        print("  pip install -r requirements.txt")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Error starting application: {e}")
        sys.exit(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Application stopped by user")
        sys.exit(0)
