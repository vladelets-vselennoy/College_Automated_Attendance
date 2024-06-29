import schedule
import time
from datetime import datetime, timedelta
from send_report import *
from Attendance_update_db import process_group_image
def job():
    process_group_image(r"C:\all\Internships\infosys springboard\10-30-00.jpeg")
    today = datetime.now().date()
    send_daily_report()
    
    if today.weekday() == 6:  # Sunday
        send_weekly_report()
    
    if today.day == 1:  # First day of the month
        send_monthly_report()
    print(" email sent succesfully")

# Schedule the job to run daily at 11:59 PM
schedule.every().day.at("23:59").do(job)
# schedule.every().day.at("21:32").do(job)
# schedule.every().day.at("21:22").do(job)
# schedule.every().day.at("20:34").do(job)

while True:
    schedule.run_pending()
    time.sleep(60)  # Wait one minute