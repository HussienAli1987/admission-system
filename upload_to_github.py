"""
Upload Admission System to GitHub
Pushes all files from D:\OnlineAdmissionSystem to your repo
"""

import subprocess
import os
import sys

def run_cmd(cmd, cwd=None):
    """Run command and return output"""
    try:
        result = subprocess.run(
            cmd,
            shell=True,
            cwd=cwd,
            capture_output=True,
            text=True,
            timeout=30
        )
        print(f"✓ {cmd}")
        if result.stdout:
            print(result.stdout[:500])
        return result.returncode == 0
    except Exception as e:
        print(f"✗ Error: {e}")
        return False

def main():
    project_dir = r"D:\OnlineAdmissionSystem"
    repo_url = "https://github.com/HussienAli1987/admission-system.git"
    
    print("=" * 70)
    print("📤 UPLOADING TO GITHUB")
    print("=" * 70)
    
    # Change to project directory
    os.chdir(project_dir)
    print(f"\n📁 Working directory: {project_dir}")
    
    # Check if .git exists, if not initialize
    if not os.path.exists(".git"):
        print("\n🔧 Initializing git repository...")
        run_cmd("git init", project_dir)
    
    # Configure git (local only)
    print("\n⚙️ Configuring git...")
    run_cmd('git config user.email "hussienali@email.com"', project_dir)
    run_cmd('git config user.name "Hussien Ali"', project_dir)
    
    # Remove old remote if exists
    print("\n🔗 Setting remote...")
    run_cmd("git remote remove origin", project_dir)
    run_cmd(f'git remote add origin "{repo_url}"', project_dir)
    
    # Stage all files
    print("\n📋 Staging all files...")
    run_cmd("git add .", project_dir)
    
    # Check status
    print("\n📊 Git status:")
    run_cmd("git status", project_dir)
    
    # Commit
    print("\n💾 Committing...")
    run_cmd('git commit -m "Upload admission system - all files"', project_dir)
    
    # Set branch to main
    print("\n🌿 Setting main branch...")
    run_cmd("git branch -M main", project_dir)
    
    # Push to GitHub
    print("\n🚀 Pushing to GitHub...")
    push_cmd = "git push -u origin main"
    if run_cmd(push_cmd, project_dir):
        print("\n" + "=" * 70)
        print("✅ SUCCESS! Files uploaded to GitHub")
        print("=" * 70)
        print(f"\n📍 Repository: {repo_url}")
        print(f"📍 View at: https://github.com/HussienAli1987/admission-system")
        print("\n" + "=" * 70)
    else:
        print("\n⚠️ Push may have failed or needs authentication")
        print("If prompted, enter your GitHub Personal Access Token (not password)")
        print("\nTo create a token:")
        print("1. Go to: https://github.com/settings/tokens")
        print("2. Click 'Generate new token'")
        print("3. Select 'repo' scope")
        print("4. Copy token and paste when prompted")

if __name__ == '__main__':
    main()
