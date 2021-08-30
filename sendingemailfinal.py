# this file is the final project with the HTML form, the first file is the most important part of the project.
# projeto final
# foram importado string e o pathlib e o email.set_content modificado
# também foi adicionado o html


import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path


html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'erictestandopython@hotmail.com'
email['to'] = 'estorani_41@hotmail.com'
email['subject'] = 'Email project test'

email.set_content(html.substitute({'name': 'EuMesmo'}), 'html')

with smtplib.SMTP(host='smtp-mail.outlook.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('erictestandopython@hotmail.com', 'Testandopython123')
    smtp.send_message(email)

    print('deu certo')
