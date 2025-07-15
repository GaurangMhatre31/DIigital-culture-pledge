# Hindalco Digital Culture Platform - Deployment Instructions

## You Downloaded: HINDALCO_DIGITAL_CULTURE_COMPLETE_FINAL_20250714_133955.zip

## Correct Setup Steps:

### For Windows:
1. Extract the ZIP file to any folder (e.g., C:\Hindalco)
2. Open Command Prompt in that folder
3. Run: `START_HINDALCO_PLATFORM.bat`

OR manually:
1. Extract ZIP file
2. Open Command Prompt in the extracted folder
3. Run: `pip install -r requirements.txt`
4. Run: `python enhanced_data_loader.py`
5. Run: `python app.py`

### For Mac/Linux:
1. Extract the ZIP file to any folder
2. Open Terminal in that folder
3. Run: `chmod +x START_HINDALCO_PLATFORM.sh`
4. Run: `./START_HINDALCO_PLATFORM.sh`

## What's Included in Your ZIP:
- `app.py` - Main application (NOT hindalco_launcher.py)
- `enhanced_data_loader.py` - Loads all 33 participants
- `START_HINDALCO_PLATFORM.bat` - Windows launcher
- `START_HINDALCO_PLATFORM.sh` - Mac/Linux launcher
- `data/hindalco_complete_data.csv` - All participant data
- `templates/` and `static/` folders - Web interface
- `requirements.txt` - Python dependencies

## Access After Setup:
- Open browser to: http://localhost:5000
- Admin login: admin / admin123
- Demo user: demo@test.com / Demo User

## The file `hindalco_launcher.py` is NOT in your downloaded package.
## Use the correct files mentioned above instead.