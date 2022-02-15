import smtplib
import imghdr
from email.message import EmailMessage

EMAIL_ADDRESS = input("Enter the email address:")
RECEIVER_EMAIL_ADDRESS = input("Enter the receiver email address:")
EMAIL_PASS = input("Enter the password:")

msg = EmailMessage()
msg['Subject'] = 'Cppsecrets logo'
msg['From'] = EMAIL_ADDRESS
msg['To'] = RECEIVER_EMAIL_ADDRESS
msg.set_content('Image attached through Python')

my_list = ['logo.png', 'ice_cream.jpg']

for image in my_list:
    with open(image, 'rb') as f:
        file = f.read()
        file_type = imghdr.what(f.name)
        file_name = f.name

    msg.add_attachment(file, maintype='image', subtype=file_type, filename=f.name)

with smtplib.SMTP('localhost', 1025) as smtp:
    smtp.send_message(msg)
