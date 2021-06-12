from flask import Flask,request,render_template
import pickle
from googleapiclient.discovery import build
from google.oauth2 import service_account
import os
from twilio.rest import Client
import itertools  
import time

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("test.html")

@app.route('/calling',methods=['POST','GET'])
def contact():
    if request.method == 'POST':

        if request.form['submit_button'] == 'For an updated accurate evaluation':

            SERVICE_ACCOUNT_FILE = 'f1-realtor-bot-c805c85fc894.json'
            SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
            creds = None
            creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
            # The ID and range of a sample spreadsheet.
            SAMPLE_SPREADSHEET_ID = '1WtIqtJ9nSj8qTY4GdhmpYz5WR5OUELrrLzQneaijmWg'
            service = build('sheets', 'v4', credentials=creds)
            sheet = service.spreadsheets()
            result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,range="recording1!B2:B100").execute()
            value= result.get('values')
            number=value
            number = list(itertools.chain(*number))
            print(number)
            for sublist in number:
                print(sublist)
                print("calling")
                account_sid = "AC751e0389d2e3b5ff16bc8af1a1b5e073"
                auth_token = "4948ea0d071dabdf3555ac5439d6a019"
                client = Client(account_sid, auth_token)
                call = client.calls.create(
                                        
                                        twiml='<Response><Say>Hi, This is John Hill calling from retail investment group. I saw that you are the owner of retail property. The reason i am calling is I thought you might want an updated accurate evaluation of your propety free of charge. If you could return my call at 5 4 1 2 1 3 9 3 3 8, once again that 5 4 1 2 1 3 9 3 3 8. Or you can also text interested.</Say></Response>',
                                        to=sublist,
                                        from_='+16504407682'
                                    )
                print(call.sid)
                time.sleep(105)
                print("its time to call for 2nd no")
            return 'Done with calling to all numbers on sheet1' 

        if request.form['submit_button'] == 'To reach out to similar property owners': 

            SERVICE_ACCOUNT_FILE = 'f1-realtor-bot-c805c85fc894.json'
            SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
            creds = None
            creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
            service = build('sheets', 'v4', credentials=creds)          
            # The ID and range of a sample spreadsheet.
            SAMPLE_SPREADSHEET_ID = '1WtIqtJ9nSj8qTY4GdhmpYz5WR5OUELrrLzQneaijmWg'
            sheet = service.spreadsheets()
            result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,range="recording2!B2:B100").execute()
            value= result.get('values')
            number=value
            number = list(itertools.chain(*number))
            print(number)
            for sublist in number:
                print(sublist)
                print("calling")
                account_sid = "AC751e0389d2e3b5ff16bc8af1a1b5e073"
                auth_token = "4948ea0d071dabdf3555ac5439d6a019"
                client = Client(account_sid, auth_token)

                call = client.calls.create(
                                        
                                        twiml='<Response><Say>Hi, My name is John Hill calling from retail investment group I saw that you are the owner of a Dennys property. The reason i am calling is we just sold a Dennys property in Glendale arizona I like to reach out to similar property owners to let them know that this property has been sold I also thought that you might want an updated accurate evaluation of your propety free of charge. If you could please return my call at 5 4 1 2 1 3 9 3 3 8, once again that 5 4 1 2 1 3 9 3 3 8. Or you can also text interested.</Say></Response>',
                                        to=sublist,
                                        from_='+12408984424'
                                    )
                print(call.sid)
                time.sleep(105)
                print("its time to call for 2nd no")
            return 'Done with calling to all numbers on sheet2' 

                
            """
            if i < len(number):
                return 'calls done'
                """ 

if __name__ == '__main__':
    app.run(debug=True, port=5000)