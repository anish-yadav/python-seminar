import os

import google.oauth2.credentials

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow

# The CLIENT_SECRETS_FILE variable specifies the name of a file that contains
# the OAuth 2.0 information for this application, including its client_id and
# client_secret.
CLIENT_SECRETS_FILE = "client_secret.json"

# This OAuth 2.0 access scope allows for full read/write access to the
# authenticated user's account and requires requests to use an SSL connection.
SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'

def get_authenticated_service():
  flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPES)
  credentials = flow.run_console()
  return build(API_SERVICE_NAME, API_VERSION, credentials = credentials)

def get_trending_list(youtube, **args):

    response = youtube.videos().list(
    **args
    ).execute()

    return response

def print_list(trending_list):
    responses = trending_list['items']
    response_array = []
    response_array_title = []
    for response in responses:
        response_array.append(response)

    for title in response_array:
        response_array_title.append(title['snippet']['title'])

    return response_array_title

youtube = get_authenticated_service()

trending_list = get_trending_list(youtube,
    part='snippet,contentDetails,statistics',
    chart='mostPopular',
    regionCode='IN',
    maxResults = 10
)

trending_title = print_list(trending_list)
print("Top 10 trending videos on Youtube trending list")
for i in range(len(trending_title)):
    print(i+1,'.',trending_title[i])
