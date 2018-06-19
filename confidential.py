import shutil
import requests
import gspread
import os
from oauth2client.service_account import ServiceAccountCredentials

def run():
    # Credentials
    os.chdir('C:\\Users\\xburn\\PycharmProjects\\GSpreadFA')
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('clientsecret.json', scope)
    client = gspread.authorize(creds)
    sheet = client.open('BGMDL').sheet1
    BGMDL = sheet.get_all_records()
    return sheet
    # Credentials


