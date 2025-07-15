#!/usr/bin/env python3
"""
Digital Culture Platform - One-Click Setup & Launch
Perfect deployment with automatic configuration
"""

import subprocess
import sys
import os
import webbrowser
import time
import platform

def check_python():
    """Check Python version"""
    if sys.version_info < (3, 8):
        print("❌ Python 3.8+ is required")
        print(f"Current version: {sys.version}")
        return False
    print(f"✅ Python {sys.version.split()[0]} detected")
    return True

def install_packages():
    """Install required packages"""
    print("📦 Installing required packages...")
    try:
        subprocess.check_call([
            sys.executable, '-m', 'pip', 'install', 
            '-r', 'requirements.txt', '--quiet'
        ])
        print("✅ All packages installed successfully")
        return True
    except subprocess.CalledProcessError:
        print("❌ Package installation failed")
        print("Please run manually: pip install -r requirements.txt")
        return False

def setup_environment():
    """Set up environment variables"""
    env_vars = {
        'FLASK_APP': 'app.py',
        'FLASK_ENV': 'development',
        'DATABASE_URL': 'sqlite:///digital_culture.db'
    }
    
    for key, value in env_vars.items():
        os.environ[key] = value
    
    print("✅ Environment configured")

def launch_application():
    """Launch the Flask application"""
    print("🚀 Starting Digital Culture Analytics Platform...")
    print("")
    print("=" * 60)
    print("🌐 Application URL: http://localhost:5000")
    print("👨‍💼 Admin Login: admin / admin123")
    print("👤 Demo User: Demo User / demo@test.com")
    print("📊 Features: Analytics, Surveys, Reports, User Management")
    print("=" * 60)
    print("")
    print("Press Ctrl+C to stop the application")
    print("")
    
    # Open browser after delay
    def open_browser():
        time.sleep(3)
        try:
            webbrowser.open('http://localhost:5000')
            print("🌐 Browser opened automatically")
        except:
            print("🌐 Please open: http://localhost:5000")
    
    import threading
    browser_thread = threading.Thread(target=open_browser)
    browser_thread.daemon = True
    browser_thread.start()
    
    # Run application
    try:
        subprocess.call([sys.executable, 'app.py'])
    except KeyboardInterrupt:
        print("\n👋 Application stopped. Thank you!")

def main():
    """Main setup and launch function"""
    print("🎯 Digital Culture Analytics Platform")
    print("📈 Complete deployment with 33 participants")
    print("=" * 50)
    
    if not os.path.exists('app.py'):
        print("❌ app.py not found. Extract ZIP properly.")
        return
    
    if not check_python():
        return
    
    if install_packages():
        setup_environment()
        launch_application()
    else:
        print("❌ Setup failed. Please install manually and run:")
        print("   python app.py")

if __name__ == "__main__":
    main()
