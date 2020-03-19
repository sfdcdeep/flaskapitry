import os
import sys
from datetime import datetime
from simple_salesforce import Salesforce
#def sfinsert():
sf = Salesforce(username='abatini27@gmail.com', password='Salesa@112', security_token='', sandbox=False)
Lastname='APJ'
Firstname='Abdhulkalam'
Name = Firstname + " " + Lastname
#NoOfChilds='30'
print("User Name:" + Name)
Accountcreation = sf.Account.create({'Name':Name})
#print("AccountCreated:")
for k, v in Accountcreation.items():
  print(k, v)
#exit()
