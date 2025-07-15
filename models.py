from datetime import datetime
from app import db

class HindalcoPledge(db.Model):
    __tablename__ = 'hindalco_pledges'
    
    id = db.Column(db.Integer, primary_key=True)
    sr_no = db.Column(db.Integer)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False)
    employee_id = db.Column(db.String(50))
    phone = db.Column(db.String(50))
    
    # Digital North Star
    problem_statement = db.Column(db.Text)
    success_metric = db.Column(db.Text)
    timeline = db.Column(db.String(100))
    
    # Weekly Practices
    weekly_practice_1 = db.Column(db.Text)  # Use Dashboards as a Management Habit
    weekly_practice_2 = db.Column(db.Text)  # Embed Digital in Team Routines
    weekly_practice_3 = db.Column(db.Text)  # Celebrate Small but Smart Digital Wins
    
    # Monthly Practices
    monthly_practice_1 = db.Column(db.Text)  # Make Data-Driven Decision-Making the Norm
    monthly_practice_2 = db.Column(db.Text)  # Drive Digital Fluency Through Team Upskilling
    monthly_practice_3 = db.Column(db.Text)  # Lead Narrative Change Around Digital
    monthly_practice_4 = db.Column(db.Text)  # Mentor Younger Talent on Digital Initiatives
    
    # Quarterly Practices
    quarterly_practice_1 = db.Column(db.Text)  # Set a Digital Ambition for Your Function
    quarterly_practice_2 = db.Column(db.Text)  # Sponsor 1-2 Digital Experiments Per Quarter
    quarterly_practice_3 = db.Column(db.Text)  # Create a Cross-Functional Digital Anchor Group
    quarterly_practice_4 = db.Column(db.Text)  # Insist on Digital Alternatives for Manual Processes
    
    # Custom Digital Habit (Section C)
    custom_practice = db.Column(db.Text)  # Practice I will develop additionally
    custom_frequency = db.Column(db.String(50))  # Weekly/Monthly/Quarterly
    custom_success_measure = db.Column(db.Text)  # How I will measure success
    
    # Behaviors from CSV
    behavior_start_1 = db.Column(db.Text)  # First START behavior
    behavior_start_2 = db.Column(db.Text)  # Second START behavior
    behavior_reduce_1 = db.Column(db.Text)  # First REDUCE behavior
    behavior_reduce_2 = db.Column(db.Text)  # Second REDUCE behavior  
    behavior_stop_1 = db.Column(db.Text)  # First STOP behavior
    behavior_stop_2 = db.Column(db.Text)  # Second STOP behavior
    
    # Review and Sign-off Section
    review_date_1 = db.Column(db.Date)  # First review date
    review_date_2 = db.Column(db.Date)  # Second review date
    review_date_3 = db.Column(db.Date)  # Final review date
    designation = db.Column(db.String(200))  # User's designation/role
    signature_date = db.Column(db.Date)  # Signature date
    pledge_agreement = db.Column(db.Boolean)  # Agreement checkbox
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationship with survey responses
    survey_responses = db.relationship('SurveyResponse', backref='user', lazy=True)
    
    def __repr__(self):
        return f'<HindalcoPledge {self.name}>'

class SurveyResponse(db.Model):
    __tablename__ = 'survey_responses'
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('hindalco_pledges.id'), nullable=False)
    response_data = db.Column(db.Text, nullable=False)  # JSON string containing all survey responses
    expert_comments = db.Column(db.Text)  # Expert feedback comments from admin
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self):
        return f'<SurveyResponse {self.id}>'

class AdminUser(db.Model):
    __tablename__ = 'admin_users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<AdminUser {self.username}>'
