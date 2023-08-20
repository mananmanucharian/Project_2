import subprocess
import smtplib
from email.message import EmailMessage


def get_current_iptables():
    result = subprocess.run(['iptables', '-L', '-n'], stdout=subprocess.PIPE, text=True)
    return result.stdout


def send_email(subject, body):
    email_sender = 'mananmanucharian@gmail.com'
    email_password = 'bjkuzoxvsoetct'
    email_receiver = 'manucharyanmanan6@gmail.com'

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.login(email_sender, email_password)
        smtp.send_message(em)


previous_iptables_file = 'previous_iptables.txt'

try:
   
    with open(previous_iptables_file, 'r') as file:
        previous_iptables = file.read()
except FileNotFoundError:
  


current_iptables = get_current_iptables()


if current_iptables != previous_iptables:
    
    subject = "IP Tables Change Detected"
    body = "New IP tables configuration:\n\n" + current_iptables
    send_email(subject, body)

    
    with open(previous_iptables_file, 'w') as file:
        file.write(current_iptables)
