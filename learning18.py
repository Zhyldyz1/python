import shutil
import smtplib
from email.mime.text import MIMEText

# Configuration
THRESHOLD_PERCENT = 80  # alert if disk usage is above this %
EMAIL_SENDER = 'you@example.com'
EMAIL_RECEIVER = 'admin@example.com'
SMTP_SERVER = 'smtp.example.com'
SMTP_PORT = 587
SMTP_USER = 'you@example.com'
SMTP_PASSWORD = 'yourpassword'  # Store securely in real use

def check_disk_usage(path='/'):
    total, used, free = shutil.disk_usage(path)
    percent_used = (used / total) * 100
    return percent_used

def send_alert(usage):
    subject = "Disk Space Alert"
    body = f"Warning: Disk usage is at {usage:.2f}%"
    
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = EMAIL_SENDER
    msg['To'] = EMAIL_RECEIVER

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SMTP_USER, SMTP_PASSWORD)
        server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, msg.as_string())
        print("Alert sent!")

def main():
    usage = check_disk_usage()
    print(f"Current disk usage: {usage:.2f}%")
    if usage > THRESHOLD_PERCENT:
        send_alert(usage)

if __name__ == "__main__":
    main()
