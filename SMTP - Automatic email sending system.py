#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
os.getcwd()


# In[2]:


import pandas as pd
import csv
import email, smtplib, ssl


# In[3]:


from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# In[4]:


# Create a list incluing all the merchants' file intending to be sent
file_list = []

for file in os.listdir():
    if file.endswith('.xlsx'):
        merchant = os.path.splitext(file)[0]
        extention = os.path.splitext(file)[1]
        file_new = merchant + 'DATE' + extention
        os.rename(file, file_new)
        file_list.append(file_new)


# In[5]:


password = input('Type your password and press enter: ')

n = 0

for i in file_list:
    filename = file_list[n]

    with open('contacts_file.csv', 'r') as file0:
        reader0 = csv.reader(file0)
        next(reader0)
        for name0, email0 in reader0:
            subject_merchant = name0
            name1 = name0.replace(' ', '') + 'DATE' + '.xlsx'
            if name1 == filename:
                rcpt = email0.split(',')
                
                subject = subject_merchant + 'SUBJECT' ## customized subject
                body = 'CONTENT'
                sender_email = 'SENDER EMAIL'
                cc_email = 'CC EMAIL'
                
                # Send to all the receivers
                receiver_email = rcpt + [cc_email]
                
                # Create a multipart message and set headers
                message = MIMEMultipart()
                message['From'] = sender_email
                message['To'] = email0
                message['Cc'] = cc_email
                message['Subject'] = subject
                    
                # Add body to email
                message.attach(MIMEText(body, "plain"))
                    
                with open(filename, 'rb') as attachment:
                    # Add file as application/octet-stream
                    # Email client can usually download this automatically as attachment
                    part = MIMEBase("application", "octet-stream")
                    part.set_payload(attachment.read())
    
                # Encode file in ASCII characters to send by email    
                encoders.encode_base64(part)
            
                # Add header as key/value pair to attachment part
                part.add_header(
                "Content-Disposition",
                f"attachment; filename= {filename}",
                )
    
                # Add attachment to message and convert message to string
                message.attach(part)
                text = message.as_string()
                    
                # Log in to server using secure context and send email
                context = ssl.create_default_context()
                with smtplib.SMTP_SSL("smtp.gmail.com", 465, context = context) as server:
                    server.login(sender_email, password)
                    server.sendmail(sender_email, receiver_email, text)

    n = n + 1

