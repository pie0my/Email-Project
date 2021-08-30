import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'erictestandopython@hotmail.com'
email['to'] = 'estorani_41@hotmail.com'
email['subject'] = 'Email project test'

email.set_content('conteudo do email, vamos ver')

with smtplib.SMTP(host='smtp-mail.outlook.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('erictestandopython@hotmail.com', 'Testandopython123')
    smtp.send_message(email)

    print('deu certo')


# first attep fail
# quando eu mudei do email['from'] para um email funcionou, quando colocava meu nome, nao funcionava
