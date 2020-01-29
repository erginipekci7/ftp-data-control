import smtplib
import time
import file_control as fc
from datetime import date,datetime,timedelta
from string import Template
import setup_smtp as sm
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def get_contacts(filename):
    names = []
    emails = []
    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            names.append(a_contact.split()[0])
            emails.append(a_contact.split()[1])
    return names, emails

def read_template(filename):  
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

def main():
    names, emails = get_contacts('contact.txt') # read contacts
    message_template = read_template('message.txt')
    fc.FileControl()
    fc.WriteLog()
    # set up the SMTP server
    s= sm.s
    sm.set_smtp()
    mailListLength=len(emails)
    maillist = ""
    for index,email in enumerate(emails):
        message = message_template.substitute(file_not_found=fc.filesNotFound)

        # setup the parameters of the message
        maillist += email
        if(index+1 != mailListLength):
            maillist += ';'        
    send_mail(message,maillist,s)

def send_mail(message,maillist,s):    
    msg = MIMEMultipart()
    msg['From']=sm.MY_ADDRESS
    msg['To']=maillist
    msg['Cc']='<mail_adress>;<mail_adress>'
    msg['Subject']="FTP Missing File"
    
    # add in the message body
    msg.attach(MIMEText(message, 'plain'))
    if(len(fc.filesNotFound)==0):
        return      	
    s.send_message(msg)
    fc.f.write("mail sent")
    fc.f.write("\n")
    del msg
    
    # Terminate the SMTP session and close the connection
    s.quit()
    
if __name__ == '__main__':
    main()