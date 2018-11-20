import xlrd
import csv
import os
import pandas as pd
filename=str('pyexcel.csv')
df = pd.read_csv('/app/'+filename,encoding = "ISO-8859-1")
s=str(os.getcwd())
print(df)
print(s)
print('Text to check if')
"""
def excelcall():
        return str(df)
        comment
"""
