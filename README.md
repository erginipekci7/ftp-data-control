# FTP Data Control

###### It checks whether there are files by connecting to the specified FTP

- FTP connection is made in file_control.py
- Mail content is included in the message.txt
- The Mailing List (To) is included in the contact.txt (! It must contain maximum 4 mail addresses.)
- CC must be specified in py_mail (! It must contain maximum 3 mail addresses.)
- The program writes the presence or absence of the file into the log.txt file.

contact.txt Format
The name must be in the form of mailadress (If more than one name, there should be no space between them)
The program runs on py_mail.py.

FTP Connection, Mail (To, CC) and SMTP information should be written before running the program
- pysftp module must be installed
`pip install 'pysftp==0.2.8'`   
