import os
import sys
from datetime import datetime
from simple_salesforce import Salesforce
sf = Salesforce(username='abatini27@gmail.com', password='Salesa@1212', security_token='', sandbox=False)
Lastname='Python'
Firstname='SFDC'
Name = Firstname + " " + Lastname
Accountcreation = sf.Account.create({'Name':Name})
for k, v in Accountcreation.items():
  print(k, v)
