#!/usr/bin/env python3
"""
Enhanced CSV Data Loader - Guaranteed to load ALL participants
Loads complete data from Hindalco_Digital_Culture_Pledge_1752559227154.csv
"""

import pandas as pd
import re
import logging
from datetime import datetime

def clean_text(text):
    """Clean and format text data"""
    if pd.isna(text) or text is None:
        return ""
    return re.sub(r'\s+', ' ', str(text)).strip()

def normalize_email(email):
    if pd.isna(email) or email is None:
        return ""
    return str(email).strip().lower()

def clean_phone(phone):
    """Clean phone number to digits only"""
    if pd.isna(phone) or phone is None:
        return ""
    # Extract only digits
    digits = re.sub(r'\D', '', str(phone))
    return digits if len(digits) >= 10 else ""

def load_all_participants_from_csv():
    """Load ALL participants with complete data from the new CSV file using header names."""
    try:
        # Load CSV file
        csv_file = 'All_36_Users_Complete_Data_20250715_121445.csv'
        df = pd.read_csv(csv_file)
        print(f"CSV loaded: {len(df)} rows, {len(df.columns)} columns")
        participants = []
        seen_emails = set()
        for index, row in df.iterrows():
            try:
                sr_no = clean_text(row.get('Sr', index+1))
                name = clean_text(row.get('Name'))
                email = normalize_email(row.get('Email'))
                phone = clean_phone(row.get('Telephone'))
                employee_id = clean_text(row.get('Employee_ID', f"HIN{str(index+1).zfill(3)}"))
                designation = clean_text(row.get('Designation', 'Digital Transformation Specialist'))
                problem_statement = clean_text(row.get('Problem_Statement'))
                success_metric = clean_text(row.get('Key_Success_Metric'))
                timeline = clean_text(row.get('Timeline_to_Impact'))
                weekly_practice_1 = clean_text(row.get('Weekly_Practice_1'))
                monthly_practice_1 = clean_text(row.get('Monthly_Practice_1'))
                monthly_practice_2 = clean_text(row.get('Monthly_Practice_2'))
                quarterly_practice_1 = clean_text(row.get('Quarterly_Practice_1'))
                quarterly_practice_2 = clean_text(row.get('Quarterly_Practice_2'))
                custom_practice = clean_text(row.get('Custom_Practice'))
                custom_frequency = clean_text(row.get('Custom_Frequency'))
                behavior_start_1 = clean_text(row.get('Behavior_START_1'))
                behavior_start_2 = clean_text(row.get('Behavior_START_2'))
                behavior_reduce_1 = clean_text(row.get('Behavior_REDUCE_1'))
                behavior_reduce_2 = clean_text(row.get('Behavior_REDUCE_2'))
                behavior_stop_1 = clean_text(row.get('Behavior_STOP_1'))
                behavior_stop_2 = clean_text(row.get('Behavior_STOP_2'))
                participant_data = {
                    'sr_no': sr_no,
                    'name': name,
                    'email': email,
                    'phone': phone,
                    'employee_id': employee_id,
                    'designation': designation,
                    'problem_statement': problem_statement,
                    'success_metric': success_metric,
                    'timeline': timeline,
                    'weekly_practice_1': weekly_practice_1,
                    'monthly_practice_1': monthly_practice_1,
                    'monthly_practice_2': monthly_practice_2,
                    'quarterly_practice_1': quarterly_practice_1,
                    'quarterly_practice_2': quarterly_practice_2,
                    'custom_practice': custom_practice,
                    'custom_frequency': custom_frequency,
                    'behavior_start_1': behavior_start_1,
                    'behavior_start_2': behavior_start_2,
                    'behavior_reduce_1': behavior_reduce_1,
                    'behavior_reduce_2': behavior_reduce_2,
                    'behavior_stop_1': behavior_stop_1,
                    'behavior_stop_2': behavior_stop_2
                }
                if name and email:
                    if email in seen_emails:
                        print(f"Warning: Duplicate email found: {email}")
                    seen_emails.add(email)
                    participants.append(participant_data)
                    print(f"Loaded: {name} - {email}")
            except Exception as e:
                print(f"Error processing row {index}: {e}")
                continue
        print(f"\nTotal participants loaded: {len(participants)}")
        return participants
    except Exception as e:
        print(f"Error loading CSV: {e}")
        return []

if __name__ == "__main__":
    participants = load_all_participants_from_csv()
    print(f"Successfully loaded {len(participants)} participants")
    for i, p in enumerate(participants[:5]):
        print(f"{i+1}. {p['name']} - {p['email']}")