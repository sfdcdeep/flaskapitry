
#read the csv and create the user
import xlrd
import csv
import os
import pandas as pd
filename=str('ikuuseronboarding.csv')
df = pd.read_csv('/app/'+filename,encoding = "ISO-8859-1")
s=str(os.getcwd())
print(df)
print(s)

import numpy as np
from datetime import datetime
from simple_salesforce import Salesforce 
sf = Salesforce(username='mballani@celgene.com.ikudev1', password='Celgene123', security_token='', sandbox=True)


n = len(df)

print(n)
for i in range(n):
    if(str(df["Form Status"][i])=="In Progress"):
        print('the value of the status is:'+str(df["Form Status"][i]))
        if(str(df["OnBehalfOf Name"][i])!="nan"):
            Name=str(df["OnBehalfOf Name"][i])
            print('name:'+Name)
            Namesplit=Name.split(' ')
            firstname=str(Namesplit[0])
            lastname=Name.split(' ')
            del lastname[0]
            lastnamelist=lastname
            LastName=''
            Lastnamesplit=len(lastname)
            for val in  range(Lastnamesplit):
                LastName+=lastnamelist[val]+' '
                print('name after split'+LastName)
            email=str(df["On Behalf Of Email"][i])
            username=email
        elif(str(df["OnBehalfOf Name"][i])=="nan"):
             Name=str(df["Requestor Name"][i])
             Namesplit=Name.split(' ')
             firstname=str(Namesplit[0])
             lastname=Name.split(' ')
             del lastname[0]             
             lastnamelist=lastname
             LastName=''
             Lastnamesplit=len(lastname)
             for val in  range(Lastnamesplit):
                LastName+=lastnamelist[val]+' '
                print('name after split'+LastName)
             email=str(df["Requestor Email"][i])
             username=email
        print('username:'+username+'email:'+email)
        profile="Celgene IKU KM Platform"
        ProfileId=sf.query("SELECT Id FROM Profile WHERE Name='"+profile+"'")
        print('profileid is:',ProfileId['records'][0]['Id'])
        role=str(df["SERole Assigned"][i])
        UserRoleId=sf.query("SELECT Id FROM UserRole WHERE Name like '"+role+"'")
        print('roleid is:',UserRoleId['records'][0]['Id'])
        permissionsettemp=df["Rule Assigned"][i]
        perm_temp = permissionsettemp.split("\n")
        del perm_temp[0]
        print('the value of perm_temp is:',perm_temp)
        timezone='America/Chicago'
        print('firstname[0:1]+LastName[0:3] is'+firstname[0:1]+LastName[0:3])
        ssopermissionset="SSO for Platform Users"
        if (perm_temp[0]=='SSO Permission'):
            perm_temp[0]=ssopermissionset
            print('the value of perm_temp after is:',perm_temp)
            pstr="SELECT Id FROM PermissionSet where Label IN{}".format(tuple(perm_temp))
            permissionid=sf.query(pstr)           
            print('the value of permission is',permissionid)
        
        usr = sf.User.create({'LastName': LastName,
        'FirstName': firstname,
        'Email' : email,
        'Alias' : firstname[0:1]+LastName[0:3],
        'UserName' : email,                     
        'FederationIdentifier' :email,
        'UserRoleId' :UserRoleId['records'][0]['Id'],
        'ProfileId' : ProfileId['records'][0]['Id'],
        'EmailEncodingKey' : 'UTF-8',
        'LanguageLocaleKey' : 'en_US',
        'LocaleSidKey' : 'en_US',                     
        'TimeZoneSidKey' :timezone                  
        })
        userid = usr["id"]
        print('userid'+userid)
        useriddetails=[]
        useriddetails.append(userid)
        #str = "SELECT Id, Email, FirstName, LastName FROM User WHERE "+ " Id"+"= '"  + userid +"'"
        createdusr = sf.query("SELECT Id, Email, FirstName, LastName FROM User WHERE "+ " Id"+"= '"  + userid +"'")
        print('the createduser is',createdusr)
        for num in useriddetails:
            per=1
            print('the value of usercreated[num] is'+num)
            for per in range(len(permissionid)-1):
                print('the value of permissionid before assigning is is'+permissionid['records'][per]['Id'])
                userpermission=sf.PermissionsetAssignment.create({'AssigneeId': num,'PermissionSetId': permissionid['records'][per]['Id']})
                userpermissionid=userpermission["id"]
                print("userpermissionidis:"+userpermissionid)
      
    
