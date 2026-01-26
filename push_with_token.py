"""
Push to GitHub using token
"""
import subprocess
import os

os.chdir(r"D:\OnlineAdmissionSystem")

token = "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"
repo_url = f"https://{token}@github.com/HussienAli1987/admission-system.git"

try:
    # Set remote URL with token
    result1 = subprocess.run(
        ["git", "remote", "set-url", "origin", repo_url],
        capture_output=True,
        text=True,
        timeout=10
    )
    print("Remote URL updated")
    
    # Push to GitHub
    result2 = subprocess.run(
        ["git", "push", "-u", "origin", "main"],
        capture_output=True,
        text=True,
        timeout=30
    )
    
    print(result2.stdout)
    if result2.stderr:
        print("Errors:", result2.stderr)
    
    if result2.returncode == 0:
        print("\n✅ SUCCESS! All files uploaded to GitHub")
        print("Repository: https://github.com/HussienAli1987/admission-system")
    else:
        print(f"\n⚠️ Push returned code: {result2.returncode}")
        
except Exception as e:
    print(f"❌ Error: {e}")
