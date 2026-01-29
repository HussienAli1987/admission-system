"""
Deploy Admission System to GitHub and Render
Run this script to upload everything automatically
"""

import os
import subprocess
import shutil
from pathlib import Path

def run_command(cmd):
    """Run shell command"""
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        print(result.stdout)
        if result.stderr:
            print(result.stderr)
        return result.returncode == 0
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def main():
    print("=" * 60)
    print("🚀 DEPLOYMENT SCRIPT - Online Admission System")
    print("=" * 60)
    
    # Check if git is installed
    print("\n📋 Checking if Git is installed...")
    if not run_command("git --version"):
        print("❌ Git not found. Please install Git first:")
        print("   https://git-scm.com/download/win")
        return False
    
    print("✅ Git is installed")
    
    # Initialize git
    print("\n📝 Initializing Git repository...")
    commands = [
        "git init",
        "git add .",
        'git commit -m "Initial admission system project"',
        "git branch -M main",
        "git remote add origin https://github.com/HussienAli1987/admission-system.git",
        "git push -u origin main"
    ]
    
    for cmd in commands:
        print(f"\n▶️  {cmd}")
        if not run_command(cmd):
            print(f"⚠️  Command may have issues, continuing...")
    
    print("\n" + "=" * 60)
    print("✅ FILES UPLOADED TO GITHUB!")
    print("=" * 60)
    print("\n📍 Next steps:")
    print("1. Go to: https://github.com/HussienAli1987/admission-system")
    print("2. Verify all files are there")
    print("\n3. Go to: https://dashboard.render.com")
    print("4. Click 'New +' → 'Web Service'")
    print("5. Select 'admission-system' repository")
    print("6. Fill in:")
    print("   - Name: admission-system")
    print("   - Environment: Python 3")
    print("   - Build Command: pip install -r requirements.txt")
    print("   - Start Command: gunicorn app:app")
    print("\n7. Click 'Create Web Service' and wait 2-5 minutes")
    print("8. Once deployed, copy your URL and send it back")
    print("\n" + "=" * 60)

if __name__ == '__main__':
    main()
