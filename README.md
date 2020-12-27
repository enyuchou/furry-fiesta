# furry-fiesta

Hello!

This side project was done during my internship from Jan to Mar 2020. The object of the project is to improve the effieciecy and the accuracy of administrative work. <br><br/>

We had more than 100 business partners, and each of them required their own monthly statement of accounting. Usually, we sent the files through email and archived the documents by uploading to Google Drive. As the work was manually done and usually took a lot of time to ensure the accuracy, I did research and built a Python system to automate and optimize the process. The python modules I used are Simple Mail Transfer Protocol (SMTP) and PyDrive. The python script, _"SMTP - Automatic email sending system"_, describes how I developed an automated email sending system that can customize the email content and attachment. On the other hand, _"upload_Gdrive_final"_ showcases how to automatically upload the files from the local device to Google Drive. The script also includes the solution of uploading the file to the particular folder when there are multiple team drives. Moreover, for those new merchants, the system will also create new folders in the team drive. <br><br/>

The most important thing of building this Python system is the consistency of the data. Take the SMTP system for example, the file name and the merchant name should always be consistent so that the system won't fail or send the accounting document to the wrong receivers. GDrive system is also the same thing that data should be well managed, otherwise, files cannot be uploaded susccessfully. These are a brief introduction and important notes to my first Python side project. Hope this can help the administrative work if there is a need. Happy coding! 
