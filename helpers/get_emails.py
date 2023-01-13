import pdb
import re
import time
from datetime import datetime, date
from dateutil.tz import gettz
import requests
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pickle
import os.path
# import base64
# import email
# from bs4 import BeautifulSoup
from google.oauth2.credentials import Credentials
import json

# Define the SCOPES. If modifying it, delete the token.pickle file.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']


def otp_func(choose_drive):
    """

    Args:
        choose_drive: online drives names or any other company mail content filtration

    Returns: opt or filtered value

    """
    selected_drive = choose_drive.strip('\"')
    if selected_drive == 'hubspot':
        try:
            otp = re.findall(r'(\d{6})', body)[0]
        except TypeError:
            otp = 'OTP not received'
    elif selected_drive == 'dropbox':
        otp = re.findall(r'(\d{6})', subject)[0]
    else:
        otp = ''
    return otp


def getEmails(choose_drive, currenttime, todaydate, starttime):
    # Variable creds will store the user access token. If no valid token found, we will create one.
    global subject, sender, date_time, txt, body
    sender = None
    subject = None
    body = None
    creds = None
    # Check if it exists
    if os.path.exists(os.getcwd() + '/assets/token.json'):
        creds = Credentials.from_authorized_user_file(os.getcwd() + '/assets/token.json', SCOPES)
    # If credentials are not available or are invalid, ask the user to log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(os.getcwd() + '/assets/stucreds2.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the access token in token.json file for the next run
    with open(os.getcwd() + '/assets/token.json', 'w') as token:
        token.write(creds.to_json())
    # Connect to the Gmail API
    service = build('gmail', 'v1', credentials=creds)
    # request a list of all the messages max last 5 messages
    selected_drive = choose_drive.strip('\"')
    if selected_drive == 'dropbox':
        email_from = 'Dropbox <no-reply@dropbox.com>'
    elif selected_drive == 'hubspot':
        email_from = 'HubSpot <noreply@hubspot.com>'
    else:
        email_from = ''
    current_time = currenttime
    today_date = todaydate
    start_time = starttime
    while ((bool(email_from) is True) and (time.time() <= start_time + 160)) is True:
        result = service.users().messages().list(maxResults=2, userId='me').execute()
        messages = result.get('messages')
        # iterate through all the messages
        for msg in messages:
            # Get the message from its id
            txt = service.users().messages().get(userId='me', id=msg['id']).execute()
            payload = txt['payload']
            headers = payload['headers']
            # Look for Subject, date and Sender Email in the headers
            for d in headers:
                if d['name'] == 'Date':
                    date_time = d['value']
                    email_time = date_time.split(",")[1].split(" ")[4]
                    email_date = date_time.split(",")[1].split(" ")[1:4]
                    email_date_str = '-'.join(email_date)
                    if (email_time >= current_time and email_date_str == today_date) is True:
                        for e in headers:
                            if e['name'] == 'From':
                                if e['value'] == email_from:
                                    sender = e['value']
                                else:
                                    continue
                                for f in headers:
                                    if f['name'] == 'Subject':
                                        subject = f['value']
                                        body = txt['snippet']
                                        otp = otp_func(choose_drive)
                                        return sender, subject, body, otp
                    else:
                        continue
        else:
            print(f'OTP mail of {email_from} is not received')
            continue
    otp = otp_func(choose_drive)
    return sender, subject, body, otp

# # uncomment it to run the file directly
# current_time = str(datetime.now(gettz('America/New_York'))).split(".")[0].split(" ")[1]
# today_date = str(datetime.now(gettz('America/New_York')).strftime("%d-%b-%Y")).lstrip("0")
# start_time = time.time()
# sender, subject, body, otp = getEmails('hubspot', current_time, today_date, start_time)
# print(sender + '\n' + subject + '\n' + body + '\n' + otp)
