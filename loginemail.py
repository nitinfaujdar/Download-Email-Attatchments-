import imaplib
import getpass
import email
import os

userName = input('Enter the username: ')
userpassword = getpass.getpass('Enter the password: ')
m = imaplib.IMAP4_SSL('imap.gmail.com')           
accountlogin = m.login(userName, userpassword)     # Email Login

m.select('Inbox')                     # Moving to the Inbox
resp, items = m.search(None, "ALL")
items = items[0].split()                        # split items

for emailID in items:
    resp, data = m.fetch(emailID, "RFC822")   # fetching mail, 'RFC822' getting the whole stuff
    raw_email = data[0][1]
    raw_email_string = raw_email.decode('utf-8')
    email_message = email.message_from_string(raw_email_string)
for part in email_message.walk():             # Walking through the mail content
    fileName = part.get_filename()        
    if bool(fileName):
            filePath = os.path.join('/home/bluepi', fileName)
            if not os.path.isfile(filePath) :
                fp = open(filePath, 'wb')
                fp.write(part.get_payload(decode=True))
                fp.close()
            
