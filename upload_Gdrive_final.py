#!/usr/bin/env python
# coding: utf-8

# In[ ]:


pip install PyDrive


# In[ ]:


import os
os.getcwd()
os.chdir('/Users/enyuchou/Desktop')


# In[ ]:


from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from pydrive.files import GoogleDriveFileList


# In[ ]:


gauth = GoogleAuth()
gauth.LocalWebserverAuth()


# In[ ]:


drive = GoogleDrive(gauth)


# In[ ]:


fileList = drive.ListFile({'q': "'1WMXBRUCsRgPrVgiWT0C_7P58-04p1F6a' in parents and trashed=false", 'corpora': 'teamDrive', 'teamDriveId': '0AGywRDwXWRm1Uk9PVA', 'includeTeamDriveItems': True, 'supportsTeamDrives': True}).GetList()
## drive.ListFile({'q':"'<Team_Drive_Id_Or_Folder_Id>' in parents and trashed=false", 'corpora': 'teamDrive', 'teamDriveId': '<Team_Drive_Id>', 'includeTeamDriveItems': True, 'supportsTeamDrives': True}).GetList()
dic_fid = {}
for file in fileList:
    print('Title: %s, ID: %s' % (file['title'], file['id']))
    dic_fid.setdefault(file['title'], file['id'])
print(dic_fid)


# In[ ]:


merchants_soa_id = '1WMXBRUCsRgPrVgiWT0C_7P58-04p1F6a'

for file in os.listdir():
    if file.endswith('.xlsx'):
        file1 = os.path.splitext(file)[0]
        filename = file1[:-15]
        if filename in dic_fid.keys():
            fid = dic_fid[filename]
            f = drive.CreateFile({
                'title': file, 
                'parents': [{
                    'kind': 'drive#fileLink', 
                    'teamDriveId': merchants_soa_id,
                    'id': fid
                }]
            })
            f.SetContentFile(file)
            f.Upload(param={'supportsTeamDrives': True})
            print(filename + ' uploaded!')
            os.remove(file)
        else:
            folder_metadata = {'title': filename, 'mimeType': 'application/vnd.google-apps.folder'}
            newfolder = drive.CreateFile(folder_metadata)
            newfolder.Upload()
            print('Create a new folder ' + filename)
            fid = newfolder.get('id')
            f = drive.CreateFile({'parents': [{'kind': 'drive#fileLink', 'id': fid}]})
            f.SetContentFile(file)
            f.Upload()
            print(filename + ' uploaded!')
            os.remove(file)





