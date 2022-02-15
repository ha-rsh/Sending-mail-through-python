import smtplib

EMAIL_ADDRESS = input("Enter the email address:")
EMAIL_PASS = input("Enter the password:")
with smtplib.SMTP('localhost', 1025) as smtp:

    subject = 'Hello this is Python'
    body = 'Message sent by Python'

    msg = f'subject: {subject}\n\n{body}'
    smtp.sendmail(EMAIL_ADDRESS, 'randompika123@gmail.com', msg)