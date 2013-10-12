import os
import smtplib
import jinja2

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def sendEmails(subject, fromAddress, email_template, email_params, member_data):
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From']    = fromAddress 
    member_info = member_data.values()
    env = jinja2.Environment()
    
    username = 'givecamp2013@tbanks.org'
    password = '54I7zU4cVDJqAVAAoudnjg'
    s = smtplib.SMTP('smtp.mandrillapp.com', 587)
    s.login(username, password)
    
    for member in member_info:
        context = {}
        for param in email_params:
            context[param] = member[param]
        text = html = env.from_string(email_template).render(context)    
        part1 = MIMEText(text, 'plain')
        part2 = MIMEText(html, 'html')
        msg.attach(part1)
        msg.attach(part2)
        msg['To'] = member['email']
        s.sendmail(msg['From'], msg['To'], msg.as_string())
        
    s.quit()


