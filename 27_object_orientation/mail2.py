


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

mail_content = '''Hi,
Please Find attachment for last 7 days moodle certifications report.

Thank You!
Moodle Team.
'''

#The mail addresses and password
sender_address = "jyoti06.dummy@gmail.com"
sender_pass = "zxcasdQWE123"
receiver_address = ["jyoti.kawade@t-systems.com","shubham.yadav@t-systems.com"]


#Setup the MIME
message = MIMEMultipart()
#message['From'] = 'admin@moodle.tsi'
#message['To'] = ['jyoti.kawade@t-systems.com']
#message['Subject'] = 'Moodle Certification Report.'
#The subject line

#The body and the attachments for the mail
message.attach(MIMEText(mail_content, 'plain'))
attach_file_name = 'mail.py'
attach_file = open(r"C:\Users\dkawa\Desktop\python programs\27_object_orientation\mail.py") # Open the file as binary mode
payload = MIMEBase('application', 'octate-stream')
payload.set_payload((attach_file).read())
encoders.encode_base64(payload) #encode the attachment
#add payload header with filename


payload.add_header('Content-Decomposition', 'attachment', filename='mail.py')
message.attach(payload)

#Create SMTP session for sending the mail
session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
session.starttls() #enable security
session.login(sender_address, sender_pass) #login with mail_id and password
print("login successfull")

text = message.as_string()
print(text)
session.sendmail(sender_address, receiver_address, text)
print("done")
session.quit()

