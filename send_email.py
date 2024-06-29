# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from email.mime.application import MIMEApplication
# from config import EMAIL_CONFIG

# def send_email(recipient, subject, body, attachment=None):
#     sender_email = EMAIL_CONFIG['sender_email']
#     sender_password = EMAIL_CONFIG['sender_password']

#     message = MIMEMultipart()
#     message["From"] = sender_email
#     message["To"] = recipient
#     message["Subject"] = subject
#     message.attach(MIMEText(body, "plain"))

#     if attachment:
#         with open(attachment, "rb") as file:
#             part = MIMEApplication(file.read(), Name=attachment.split("/")[-1])
#         part['Content-Disposition'] = f'attachment; filename="{attachment.split("/")[-1]}"'
#         message.attach(part)

#     # with smtplib.SMTP_SSL('smtp.office365.com', 465) as server:
#     #         server.login(sender_email, sender_password)
#     #         server.sendmail(sender_email, recipient, message.as_string())
      
   

#     # with smtplib.SMTP_SSL("smtp.office365.com", 465) as server:
#         # server.starttls()  # This line is crucial
#         # server.login(sender_email, sender_password)
#         # server.sendmail(sender_email, recipient, msg.as_string())
#         # # server.send_message(message)

#     with smtplib.SMTP_SSL("smtp.office365.com", 587) as server:
#         server.login(sender_email, sender_password)
#         server.send_message(message)








import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from config import EMAIL_CONFIG

def send_email(recipient, subject, body, attachment=None):
    sender_email = EMAIL_CONFIG['sender_email']
    sender_password = EMAIL_CONFIG['sender_password']

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = recipient
    message["Subject"] = subject
    message.attach(MIMEText(body, "plain"))

    if attachment:
        with open(attachment, "rb") as file:
            part = MIMEApplication(file.read(), Name=attachment.split("/")[-1])
        part['Content-Disposition'] = f'attachment; filename="{attachment.split("/")[-1]}"'
        message.attach(part)

    # Using port 587 with starttls
    with smtplib.SMTP("smtp.office365.com", 587) as server:
        server.starttls()  # Upgrade the connection to secure
        server.login(sender_email, sender_password)
        server.send_message(message)