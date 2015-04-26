import gnomekeyring
import smtplib
import urllib
import tkMessageBox
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def get_my_ip_address():
    what_is_my_ip = 'http://www.whatismyip.com/automation/n09230945.asp'
    return urllib.urlopen(what_is_my_ip).readlines()[0]
 

def get_password():
    for keyring in gnomekeyring.list_keyring_names_sync():
        for id in gnomekeyring.list_item_ids_sync(keyring):
            item = gnomekeyring.item_get_info_sync(keyring, id)
            if item.get_display_name() == 'Mail':
                return item.get_secret()

 
def send_mail():
    mail_from = '@gmail.com'
    mail_to = '@gmail.com'
    mail_cc = '@gmx.de'

    msg = MIMEMultipart()
    msg['Subject'] = 'Hilfe Anforderung'
    msg['From'] = mail_from
    msg['To'] = mail_to
    msg['Cc'] = mail_cc

    msg_text = 'Hallo Martin,\n\nIch brauche deine Hilfe. '
    msg_text += 'Meine IP ist %s.' % get_my_ip_address()

    msg.attach(MIMEText(msg_text))

    username = ''
    password = get_password()

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username, password)
    server.sendmail(mail_from, mail_to, msg.as_string())
    server.quit()


if __name__ == '__main__':
    send_mail()
    tkMessageBox.showinfo('Hilfe kommt!',
                          'Deine Anfrage wurde erfolgreich gesendet.')
