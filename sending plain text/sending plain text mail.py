import smtplib

EMAIL_ADDRESS = input("Enter the email address:")
EMAIL_PASS = input("Enter the password:")
with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(EMAIL_ADDRESS, EMAIL_PASS)
    subject = 'Hello this is Python'
    body = 'Message sent by Python'

    msg = f'subject: {subject}\n\n{body}'
    smtp.sendmail(EMAIL_ADDRESS, 'RECEIVER MAIL ADDRESS', msg)