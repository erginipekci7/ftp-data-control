import smtplib

MY_ADDRESS='<mail_account>'
PASSWORD = '<password>'
s = smtplib.SMTP(host='<host>', port=<port>)
def set_smtp():
    s.starttls()
    s.login(MY_ADDRESS,PASSWORD)