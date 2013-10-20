
import datetime
import os
import smtplib


from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def sendEmails(subject, fromAddress, emailHtml, emailText, member_data):

    member_info = member_data.values()
    
    username = 'givecamp2013@tbanks.org'
    password = '54I7zU4cVDJqAVAAoudnjg'
    s = smtplib.SMTP('smtp.mandrillapp.com', 587)
    s.login(username, password)
    fileName = 'senders_list_' + datetime.datetime.today().strftime('%x').replace('/','_') + '.txt'
    logFile = open(fileName, 'w')
    for member in member_info:
        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['From']    = fromAddress 
        text = emailText.replace('{{name}}', member['first'])
        html = emailHtml.replace('{{name}}', member['first'])
        part1 = MIMEText(text, 'plain')
        part2 = MIMEText(html, 'html')
        msg.attach(part1)
        msg.attach(part2)
        msg['To'] = member['email']
        logFile.write(msg['To'] + ' ' + member['first'] + '\n')
        #logFile.write(member['email'], member['first'])
        #print part2, msg
        #testAddress = 'givecamp2013@tbanks.org'
        #logFile.write('\n' + msg.as_string() + '\n') 
        s.sendmail(msg['From'], msg['To'], msg.as_string())

    logFile.close()
    s.quit()



