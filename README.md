# Digital Culture Analytics & Management Platform

A comprehensive Flask-based web application for tracking digital culture pledges and survey responses with advanced analytics and reporting capabilities.

## Features

- **Executive Dashboard**: Premium admin interface with real-time analytics
- **Participant Management**: Complete user and survey tracking system
- **Advanced Reporting**: PDF, Excel, and PowerPoint exports with embedded charts
- **Email System**: Automated reminder and notification system
- **Analytics**: Interactive charts and comprehensive data visualization
- **Responsive Design**: Professional Bootstrap 5 UI with modern styling

## Quick Setup

### Prerequisites
- Python 3.8 or higher
- PostgreSQL (optional - SQLite works for development)

### Installation

1. **Extract the ZIP file** to your desired directory
2. **Install Python dependencies**:
   ```bash
   pip install -r requirements_standalone.txt
   ```

3. **Set environment variables**:
   ```bash
   export SESSION_SECRET="your-secret-key-here"
   export DATABASE_URL="sqlite:///app.db"  # or your PostgreSQL URL
   ```

4. **Initialize the database**:
   ```bash
   python -c "from app import db; db.create_all()"
   ```

5. **Load sample data** (optional):
   ```bash
   python data_loader.py
   ```

6. **Run the application**:
   ```bash
   python main.py
   ```

7. **Access the application**:
   - Main app: http://localhost:5000
   - Admin login: http://localhost:5000/admin/login
   - Default admin credentials: admin/admin123

## Project Structure

```
digital_culture_app/
├── app.py                 # Main Flask application
├── main.py               # Application entry point
├── models.py             # Database models
├── utils.py              # Utility functions
├── requirements.txt      # Python dependencies
├── templates/            # HTML templates
├── static/              # CSS, JS, and assets
├── data/                # Sample data files
└── README.md            # This file
```

## Environment Variables

- `SESSION_SECRET`: Secret key for Flask sessions
- `DATABASE_URL`: Database connection URL
- `MAIL_SERVER`: SMTP server for email functionality (optional)
- `MAIL_PORT`: SMTP port (optional)
- `MAIL_USERNAME`: Email username (optional)
- `MAIL_PASSWORD`: Email password (optional)

## Production Deployment

For production deployment:
1. Use PostgreSQL instead of SQLite
2. Set proper environment variables
3. Use a WSGI server like Gunicorn
4. Configure nginx as reverse proxy
5. Set up SSL certificates

## Support

For technical support or questions, refer to the comprehensive documentation in `replit.md`.