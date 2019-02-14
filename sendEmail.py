from email.message import EmailMessage
import smtplib

def sendEmail(strokesNews):
    #message to be sent
    message = ",".join(strokesNews)
    msg = EmailMessage()
    msg.set_content(message)

    msg['Subject'] = 'Strokes News Update'
    msg['From'] = 'gson.walker@gmail.com'
    msg['To'] = 'gaw3aa@virginia.edu'

    # Send the message via our own SMTP server.
    s = smtplib.SMTP('smtp.gmail.com', 587)
    mail = smtplib.SMTP('smtp.gmail.com', 587)
    mail.ehlo()
    mail.starttls()
    mail.login('*your email here*', '*your password here*')
    mail.send_message(msg)
    mail.quit()

    print("Successfully sent email")
