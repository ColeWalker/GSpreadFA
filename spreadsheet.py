import shutil
import requests
import gspread
import os
from oauth2client.service_account import ServiceAccountCredentials
import pprint
import json
import confidential
import config

sheet = confidential.run()

# Reads and parses data from "freeagency.txt", appends that data to the excel document.
freeAgentFile = open(config.free_agency_doc, 'r+')
for line in freeAgentFile:
    person,offer,time=line.split('\t')
    person = str(person)
    offer = str(offer)
    rt = time.split('.')
    rt = str(rt)
    rt = rt[2:21]
    rowData = [person, offer, rt]
    sheet.append_row(rowData)

#Opens data, appends it to a json dictionary
with open('bgmdl.json','r') as f:
    dataF = f.read()

dict = json.loads(dataF)

#Backs up file using incremental naming convention
shutil.copy(config.free_agency_doc, config.backup_doc.format(dict['data']['backup']))

#updates json name save
dict['data']['backup'] += 1
save = json.dumps(dict)


with open ('bgmdl.json' ,'w') as f:
    f.write(save)

#delets old file contents
with open (config.free_agency_doc,'w') as f:
    f.truncate()