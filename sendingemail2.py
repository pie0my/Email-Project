import smtplib
import ssl
from email.mime.text import MIMEText

sender = 'erictestandopython@hotmail.com'
receivers = ['estorani_41@hotmail.com']
body_of_email = 'segunda tentativa, vamos la'

msg = MIMEText(body_of_email, 'html')
msg['Subject'] = 'projeto email segunda tentativa'
msg['From'] = sender
msg['To'] = ','.join(receivers)

s = smtplib.SMTP_SSL(host='smtp-mail.outlook.com', port=465)
s.login(user='erictestandopython@hotmail.com', password='Testandopython123')
s.sendmail(sender, receivers, msg.as_string())
s.quit()

#it doesnt work! the first one is the one which words
#mudei o from
