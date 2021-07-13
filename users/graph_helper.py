import requests
import json

from requests_oauthlib import OAuth2Session

graph_url = 'https://graph.microsoft.com/v1.0'

def get_user(token):
  # Send GET to /me
  user = requests.get(
    '{0}/me'.format(graph_url),
    headers={
      'Authorization': 'Bearer {0}'.format(token)
    },
    params={
      '$select': 'displayName,mail,mailboxSettings,userPrincipalName'
    })
  # Return the JSON result
  return user.json()

#This get_user function method makes a GET request to Microsoft Graph/me endpoint to get user profie using access token we save previously.




def get_calendar_events(token, start, end, timezone):
  # Set headers
  headers = {
    'Authorization': 'Bearer {0}'.format(token),
    'Prefer': 'outlook.timezone="{0}"'.format(timezone)
  }

  # Configure query parameters to
  # modify the results
  query_params = {
    'startDateTime': start,
    'endDateTime': end,
    '$select': 'subject,organizer,start,end',
    '$orderby': 'start/dateTime',
    '$top': '50'
  }



  # Send GET to /me/events
  events = requests.get('{0}/me/calendarview'.format(graph_url),
    headers=headers,
    params=query_params)

  # Return the JSON result
  return events.json()



def get_mail(token, timezone, start):
  # Set headers
  headers = {
    'Authorization': 'Bearer {0}'.format(token),
    'Prefer': 'outlook.timezone="{0}"'.format(timezone)
  }

  # Configure query parameters to
  # modify the results
  query_params = {
    'startDateTime': start,
    '$select': 'subject,organizer,start',
    '$orderby': 'start/dateTime',
    '$top': '50'
  }



  # Send GET to /me/events
  events = requests.get('{0}/me/mailFolders'.format(graph_url),
    headers=headers,
    params=query_params)

  # Return the JSON result
  return events.json()


# Basic lookup for mapping Windows time zone identifiers to
# IANA identifiers
# Mappings taken from
# https://github.com/unicode-org/cldr/blob/master/common/supplemental/windowsZones.xml
zone_mappings = {'India Standard Time': 'Asia/Calcutta'
}

def get_iana_from_windows(windows_tz_name):
  if windows_tz_name in zone_mappings:
    return zone_mappings[windows_tz_name]
  else:
    # Assume if not found value is
    # already an IANA name
    return windows_tz_name



def create_event(token, subject, start, end, attendees=None, body=None, timezone='UTC'):
  # Create an event object
  # https://docs.microsoft.com/graph/api/resources/event?view=graph-rest-1.0
  new_event = {
    'subject': subject,
    'start': {
      'dateTime': start,
      'timeZone': timezone
    },
    'end': {
      'dateTime': end,
      'timeZone': timezone
    }
  }

  if attendees:
    attendee_list = []
    for email in attendees:
      # Create an attendee object
      # https://docs.microsoft.com/graph/api/resources/attendee?view=graph-rest-1.0
      attendee_list.append({
        'type': 'required',
        'emailAddress': { 'address': email }
      })

    new_event['attendees'] = attendee_list

  if body:
    # Create an itemBody object
    # https://docs.microsoft.com/graph/api/resources/itembody?view=graph-rest-1.0
    new_event['body'] = {
      'contentType': 'text',
      'content': body
    }

  # Set headers
  headers = {
    'Authorization': 'Bearer {0}'.format(token),
    'Content-Type': 'application/json'
  }

  requests.post('{0}/me/events'.format(graph_url),
    headers=headers,
    data=json.dumps(new_event))



def get_mails(token):
  graph_client=OAuth2Session(token=token)
  users=graph_client.get('{0}/me/messages/AAMkADhMGAAA='.format(graph_url))
  return users.json()
