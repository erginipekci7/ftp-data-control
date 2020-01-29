import os.path
from datetime import date,datetime, timedelta
from ftplib import FTP
import pysftp
f = open("log.txt","a",encoding='utf-8')
now = datetime.now() # current date and time
date_time = now.strftime("%Y%m%d_%I00%p")
files_in_ftp = []
filesNotFound = []

fileName = [date_time+'_fileprefix',False]

#sftp connect and get data
with pysftp.Connection(host='<host_url>', username='<username>', password='<password>') as sftp:
    # Switch to a remote directory
    sftp.cwd('</customer/path/>')

    # Obtain structure of the remote directory 
    directory_structure = sftp.listdir_attr()

    # Print data
    for attr in directory_structure:        
        if ((now.strftime("%Y") in attr.filename):
            files_in_ftp.append(attr.filename)


def FileControl():
    if (fileName[0] in files_in_ftp):
        print (date_time+"_fileprefix exists")
        fileName[1]=True
    else:
        print (date_time+"_fileprefix not exist")
        filesNotFound.append(fileName[0])

def WriteLog():
    print ("on WriteLog()")
    if(len(filesNotFound)==0):
        print("All files are exists")
        f.write(now.strftime("%Y/%m/%d - %I:%M %p") + " There is no missing file in the system in time")
        f.write("\n")        
    else:
        f.write(now.strftime("%Y/%m/%d - %I:%M %p") + " Missing files in the system in time")
        f.write("\n")
        for files in filesNotFound:
            f.write(files)
            f.write("\n")
    print ("Written to log.txt")