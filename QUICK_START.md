# 🚀 QUICK START GUIDE

## Super Easy Launch (Just Double-Click!)

### Windows Users:
1. Extract `digital_culture_final.zip`
2. **Double-click `start.bat`**
3. Wait for setup to complete
4. Browser opens automatically at http://localhost:5000

### Mac/Linux Users:
1. Extract `digital_culture_final.zip`
2. **Double-click `start.sh`** (or run in terminal)
3. Wait for setup to complete
4. Browser opens automatically at http://localhost:5000

### Alternative Methods:

**Method 1 - Python Direct:**
```bash
python start.py
```

**Method 2 - Full Setup:**
```bash
# Windows
setup.bat

# Mac/Linux
bash setup.sh
```

## Access Your Application

- **Main App**: http://localhost:5000
- **Admin Panel**: http://localhost:5000/admin/login
- **Username**: admin
- **Password**: admin123

## What Happens Automatically:

✅ Installs all required Python packages
✅ Creates SQLite database
✅ Sets up admin user (admin/admin123)
✅ Loads sample participant data
✅ Starts web server on port 5000

## Troubleshooting:

**Python not found?**
- Install Python 3.8+ from https://python.org
- Make sure it's added to PATH

**Port 5000 busy?**
- Stop other applications using port 5000
- Or edit `start.py` and change port number

**Dependencies fail?**
- Run: `pip install -r requirements_standalone.txt`
- Or use the setup scripts first

## Features Available:

- 📊 Executive Dashboard with Analytics
- 👥 Participant Management
- 📋 Survey Forms and Tracking
- 📄 PDF Report Generation
- 📊 Excel Exports with Charts
- 📧 Email Reminder System
- 💼 PowerPoint Presentation Generation

## Need Help?
Check `README.md` for detailed instructions or `replit.md` for technical documentation.