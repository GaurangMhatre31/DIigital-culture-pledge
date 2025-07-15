# Email Configuration Guide for Digital Culture Survey Application

## Overview
The application now supports sending email reminders to participants using Flask-Mail. Here's how to configure it properly.

## Required Environment Variables

Add these environment variables to your Replit project secrets:

### Gmail Configuration (Recommended)
```
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=true
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-specific-password
MAIL_DEFAULT_SENDER=your-email@gmail.com
```

### Other Email Providers
For other email providers, update the MAIL_SERVER and MAIL_PORT accordingly:

- **Outlook/Hotmail**: `smtp-mail.outlook.com:587`
- **Yahoo**: `smtp.mail.yahoo.com:587`
- **Corporate SMTP**: Contact your IT team for server details

## Setting Up Gmail App Password

1. **Enable 2-Factor Authentication** on your Gmail account
2. Go to Google Account settings → Security
3. Under "Signing in to Google," select "App passwords"
4. Generate a new app password for "Mail"
5. Use this 16-character password (not your regular Gmail password) in `MAIL_PASSWORD`

## How to Add Secrets in Replit

1. Click on the "Secrets" tab in the left sidebar
2. Add each environment variable one by one:
   - Key: `MAIL_USERNAME`
   - Value: `your-email@gmail.com`
3. Repeat for all required variables

## Email Features

### Individual Reminders
- Admin can send reminder emails to individual participants
- Click the email icon next to any participant in the admin dashboard
- Professional HTML-formatted emails with login instructions

### Bulk Reminders
- Select multiple participants using checkboxes
- Click "Bulk Reminders" to send emails to all selected participants
- Real-time feedback showing successful/failed email counts

### Email Content
- Professional HTML template with company branding
- Personalized greeting with participant name
- Clear instructions for accessing the survey
- Direct link to the application
- Participant's login email included for reference

## Error Handling

The system provides detailed error messages for:
- Missing email configuration
- Invalid email addresses
- SMTP connection issues
- Individual email failures in bulk operations

## Testing Email Configuration

1. Set up the environment variables as described above
2. Restart the application
3. Go to Admin Dashboard → Participants tab
4. Try sending a test reminder to a single participant
5. Check the notification for success/error messages

## Troubleshooting

### Common Issues:

1. **"Email configuration not available"**
   - Check that all required environment variables are set
   - Restart the application after adding secrets

2. **"Authentication failed"**
   - Verify Gmail app password is correct
   - Ensure 2FA is enabled on Gmail account

3. **"Connection refused"**
   - Check MAIL_SERVER and MAIL_PORT settings
   - Verify network connectivity

4. **Emails not received**
   - Check spam/junk folders
   - Verify recipient email addresses are correct
   - Test with a different email provider

## Production Considerations

- Use a dedicated business email account for sending notifications
- Consider using transactional email services like SendGrid, AWS SES, or Mailgun for high volume
- Set up SPF, DKIM, and DMARC records for better deliverability
- Monitor email sending logs and bounce rates

## Security Notes

- Never commit email credentials to code repositories
- Use environment variables for all sensitive configuration
- Regularly rotate email passwords
- Monitor for suspicious email activity