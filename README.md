# furry-fiesta

Hello!

This mini project is the first step that I switched from accounting to programming and data science, and it was also a practice of my Python skill.

The project was done during my internship from Jan to Mar 2020. 
I was responsible to send out the statements of accounting to our over 100 business partners through email and archive those accounting documents to our team's Google Drive. 
Since most of the work was manually done and usually cost a lot of time, I tried to build a Python system to automate and optimize the process.

The two python scripts, _"SMTP - Automatic email sending system"_ and _"upload_Gdrive_final"_, shows the administrative part of my work.  <br><br/>


## SMTP - Automatic email sending system

Simple Mail Transfer Protocol (SMTP) is the Python module that can automatically send out emails to multiple receivers. More information can refer to Real Python artical _"Sending Emails with Python"_, in which it teaches Python learners how to build an automated email sending system.  <br><br/>

As mentioned above, the aim of my work was to send different files to different business partners, so the most important thing is to align the partners' names. The main logic of automatically sending out the different files is to make sure your file name and the merchants' names are exactly the same. Below two blocks showcase how I match the excel file that I intend to sent oud to the particular receivers. <br><br/>

##### Create a list that includes all the file names. 

```py
file_list = []

for file in os.listdir():
    if file.endswith('.xlsx'):
        merchant = os.path.splitext(file)[0]
        extention = os.path.splitext(file)[1]
        file_new = merchant + 'DATE' + extention
        os.rename(file, file_new)
        file_list.append(file_new)
```
<br><br/>

##### Matching of the merchants names and the file names
```py
for i in file_list:
    filename = file_list[n]

    with open('contacts_file.csv', 'r') as file0:
        reader0 = csv.reader(file0)
        next(reader0)
        for name0, email0 in reader0:
            subject_merchant = name0
            name1 = name0.replace(' ', '') + 'DATE' + '.xlsx'
```
