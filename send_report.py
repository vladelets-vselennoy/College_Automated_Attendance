from generate_report import *
from datetime import datetime
from config import faculty_emails,director_email
import os

from send_email import *
def send_daily_report(img):
    today = datetime.now().date()
    report,sb = generate_daily_report(today)
    report.to_excel(f"daily_report_{today}.xlsx")
    filepath=img
    prefix=str(sb+"_")
    directory = os.path.dirname(filepath)
    filename, extension = os.path.splitext(os.path.basename(filepath))
    
    # Construct the new filename with prefix
    new_filename = f"{prefix}_{filename}{extension}"
    new_filepath = os.path.join(directory, new_filename)
    img=new_filepath
    # Rename the existing file
    os.rename(filepath, new_filepath)
    
    # faculty_emails = ["faculty1@example.com", "faculty2@example.com"]  # Add faculty emails
    # director_email = "director@example.com"
    
    for email in faculty_emails:
        send_email(email, f"Daily Attendance Report - {today}", 
                   "Please find attached the daily attendance report.", 
                   [f"daily_report_{today}.xlsx",img])
    
    send_email(director_email, f"Daily Attendance Report - {today}", 
               "Please find attached the daily attendance report.", 
               [f"daily_report_{today}.xlsx",img])

def send_weekly_report():
    today = datetime.now().date()
    start_of_week = today - timedelta(days=today.weekday())
    end_of_week = start_of_week + timedelta(days=6)
    report = generate_weekly_report(start_of_week, end_of_week)
    report.to_excel(f"weekly_report_{start_of_week}_to_{end_of_week}.xlsx")
    
    # faculty_emails = ["faculty1@example.com", "faculty2@example.com"]  # Add faculty emails
    # director_email = "director@example.com"
    
    for email in faculty_emails:
        send_email(email, f"Weekly Attendance Report - {start_of_week} to {end_of_week}", 
                   "Please find attached the weekly attendance report.", 
                   [f"weekly_report_{start_of_week}_to_{end_of_week}.xlsx"])
    
    send_email(director_email, f"Weekly Attendance Report - {start_of_week} to {end_of_week}", 
               "Please find attached the weekly attendance report.", 
               [f"weekly_report_{start_of_week}_to_{end_of_week}.xlsx"])

def send_monthly_report():
    today = datetime.now().date()
    report = generate_monthly_report(today.year, today.month)
    report.to_excel(f"monthly_report_{today.year}_{today.month}.xlsx")
    
    # faculty_emails = ["faculty1@example.com", "faculty2@example.com"]  # Add faculty emails
    # director_email = "director@example.com"
    
    for email in faculty_emails:
        send_email(email, f"Monthly Attendance Report - {today.year}-{today.month}", 
                   "Please find attached the monthly attendance report.", 
                   [f"monthly_report_{today.year}_{today.month}.xlsx"])
    
    send_email(director_email, f"Monthly Attendance Report - {today.year}-{today.month}", 
               "Please find attached the monthly attendance report.", 
               [f"monthly_report_{today.year}_{today.month}.xlsx"])