import smtplib, ssl
## email.mime subclasses
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
### Add new subclass for adding attachments
##############################################################
from email.mime.application import MIMEApplication
##############################################################
## The pandas library is only for generating the current date, which is not necessary for sending emails
import pandas as pd

def attach_file_to_email(email_message, filename):
    # Open the attachment file for reading in binary mode, and make it a MIMEApplication class
    with open(filename, "rb") as f:
        file_attachment = MIMEApplication(f.read())
    # Add header/name to the attachments    
    file_attachment.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )
    # Attach the file to the message
    email_message.attach(file_attachment)
    
    
    
email_from = 'donotreply@lognormal.io'
password = 'Sag73665'
email_to = 'saiteja.reddy@lognormal.io'

# Generate today's date to be included in the email Subject
date_str = pd.Timestamp.today().strftime('%Y-%m-%d')

# Create a MIMEMultipart class, and set up the From, To, Subject fields
email_message = MIMEMultipart()
email_message['From'] = email_from
email_message['To'] = email_to
email_message['Subject'] = f'Report email - {"testmail"}'

# Attach the html doc defined earlier, as a MIMEText html content type to the MIME message
#email_message.attach(MIMEText(html.read(), "html"))
#email_message.attach(MIMEText(body, "html"))

# Attach more (documents)
##############################################################
#attach_file_to_email(email_message, attachement)
#attach_file_to_email(email_message, 'excel_report.xlsx')
#attach_file_to_email(email_message, 'fpdf_pdf_report.pdf')
##############################################################
# Convert it as a string
email_string = email_message.as_string()


server = smtplib.SMTP('smtp.outlook.com',587)
server.starttls()
server.login('donotreply@lognormal.io', "Sag73665")
server.sendmail(email_from, email_to, email_string)
server.quit()
