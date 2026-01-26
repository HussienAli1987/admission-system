#!/usr/bin/env python3
"""
Installation verification and setup script
Run this to check if everything is ready
"""

import os
import sys
from pathlib import Path

def check_file_exists(filepath):
    if Path(filepath).exists():
        print(f"  ✅ {filepath}")
        return True
    else:
        print(f"  ❌ {filepath} (MISSING)")
        return False

def check_package(package_name):
    try:
        __import__(package_name)
        print(f"  ✅ {package_name}")
        return True
    except ImportError:
        print(f"  ❌ {package_name} (NOT INSTALLED)")
        return False

def main():
    print("\n" + "="*70)
    print("🔍 Online Admission System - Installation Verification")
    print("="*70 + "\n")

    all_good = True

    # Check files
    print("📄 Checking files:")
    required_files = [
        "app.py",
        "requirements.txt",
        "README.md",
        "QUICKSTART.md",
        "templates/index.html",
        "templates/admission_form.html",
        "templates/admin.html",
        "uploads/",
    ]

    for file in required_files:
        if not check_file_exists(file):
            all_good = False

    print()

    # Check Python packages
    print("📦 Checking Python packages:")
    required_packages = [
        "flask",
        "flask_sqlalchemy",
        "flask_cors",
        "qrcode",
        "PIL",
    ]

    for package in required_packages:
        if not check_package(package):
            all_good = False

    print()

    # Summary
    if all_good:
        print("✅ Everything looks good!")
        print("\n🚀 You can now run the application:")
        print("   Option 1: python run.py")
        print("   Option 2: python app.py")
        print("\n📖 Then visit: https://127.0.0.1:5000")
    else:
        print("❌ Some issues found!")
        print("\n💻 To fix, run:")
        print("   pip install -r requirements.txt")
        print("\n📖 Then run verification again:")
        print("   python check_setup.py")
        sys.exit(1)

    print("\n" + "="*70 + "\n")

if __name__ == "__main__":
    main()
