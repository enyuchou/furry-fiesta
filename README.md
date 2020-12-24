# furry-fiesta

Hello!

This mini project is the first step that I switched from accounting to programming and data science, and it was also a practice of my Python skill.

The project was done during my internship from Jan to Mar 2020. 
I was responsible to send out the statements of accounting to our over 100 business partners through email and archive those accounting documents to our team's Google Drive. 
Since most of the work was manually done and usually cost a lot of time, I tried to build a Python system to automate and optimize the process.

The two python scripts, _"SMTP - Automatic email sending system"_ and _"upload_Gdrive_final"_, shows the administrative part of my work. 


## SMTP - Automatic email sending system

Simple Mail Transfer Protocol (SMTP) is the Python module that can automatically send out emails to multiple receivers. More information can refer to Real Python artical _"Sending Emails with Python"_, in which it teaches Python learners how to build an automated email sending system. 

As mentioned above, the aim of my work was to send different files to different business partners, the first step was to manage the database. 

```py
file_list = []

for file in os.listdir():
    if file.endswith('.xlsx'):
        merchant = os.path.splitext(file)[0]
        extention = os.path.splitext(file)[1]
        file_new = merchant + 'DATE' + extention
        os.rename(file, file_new)
        file_list.append(file_new)
```py
