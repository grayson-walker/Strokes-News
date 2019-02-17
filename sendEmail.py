from email.message import EmailMessage
import smtplib

def sendEmail(strokes_news):
    #message to be sent
    message = ",".join(strokes_news)
    msg = EmailMessage()
    msg.set_content(message)

    
    #Input your to/from here
    msg['Subject'] = 'Strokes News Update'
    msg['From'] = ''
    msg['To'] = ''

    # Send the message via SMTP server.
    s = smtplib.SMTP('smtp.gmail.com', 587)
    mail = smtplib.SMTP('smtp.gmail.com', 587)
    mail.ehlo()
    mail.starttls()
    mail.login('*your email here*', '*your password here*')
    mail.send_message(msg)
    mail.quit()

    print("Successfully sent email")
