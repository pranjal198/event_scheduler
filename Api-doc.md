<div align="center">

# Event Scheduler

A web solution for organising and managing all Events
<br/>

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![React](https://img.shields.io/badge/react-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB) <br/>

![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![Postman](https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white)
[![Visual Studio Code](https://img.shields.io/badge/--007ACC?logo=visual%20studio%20code&logoColor=ffffff)](https://code.visualstudio.com/)
[![GitHub](https://img.shields.io/badge/--181717?logo=github&logoColor=ffffff)](https://github.com/pranjal198/event_scheduler)

<br/>

# Api Documentation:
</div>

## Endpoints:-

### 1 Login Api
- For logging in user using microsoft account
- URL
  ```http
  GET apiLogin/
  ```
- Request body structure

  | Parameter | Type | Required | Description |
  | :--- | :--- | :--- | :--- |
  | `token` | `string` | **Required** | Access token issued by Microsoft Azure |

- Example Input
  ```javascript
  {
    "token":"eyJ0eXAiOiJKV1QiLCJub25jZSI6ImZySTRVSThOSFpvdEZ4MTlvWmpTVFNLSzhUZFJZOFlaRDFJNjdvYTZEN2ciLCJhbGciOiJSUzI1NiIsIng1dCI6Ik1yNS1BVWliZkJpaTdOZDFqQmViYXhib1hXMCIsImtpZCI6Ik1yNS1BVWliZkJpaTdOZDFqQmViYXhib1hXMCJ9.eyJhdWQiOiIwMDAwMDAwMy0wMDAwLTAwMDAtYzAwMC0wMDAwMDAwMDAwMDAiLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC84NTBhYTc4ZC05NGUxLTRiYzYtOWNmMy04YzExYjUzMDcwMWMvIiwiaWF0IjoxNjQyODMzOTQ4LCJuYmYiOjE2NDI4MzM5NDgsImV4cCI6MTY0MjgzNzkyNywiYWNjdCI6MCwiYWNyIjoiMSIsImFpbyI6IkUyWmdZRmhtcWY0bW83WGorOVVWaThyTnZVTlVPS3dQTGVhS1hYNmVxV0JiNUgzeks2Y0EiLCJhbXIiOlsicHdkIl0sImFwcF9kaXNwbGF5bmFtZSI6IkV2ZW50IFNjaCIsImFwcGlkIjoiNTE2MDQzMjItYWM0Yi00YjQ1LWE1ZDEtZDZhOGY3MzcwMzhmIiwiYXBwaWRhY3IiOiIwIiwiZmFtaWx5X25hbWUiOiIyMDAxMDEwMTciLCJnaXZlbl9uYW1lIjoiQU5VUkFHIFJBVkkiLCJpZHR5cCI6InVzZXIiLCJpcGFkZHIiOiIyMDMuODkuOTcuNjciLCJuYW1lIjoiQU5VUkFHIFJBVkkiLCJvaWQiOiI4YzRmMjMyOC1jNDI3LTQyYTEtYWNhYS1mMjZjYWQwN2IyM2YiLCJwbGF0ZiI6IjMiLCJwdWlkIjoiMTAwMzIwMDBGNjdEQ0VGNiIsInJoIjoiMC5BU29BamFjS2hlR1V4a3VjODR3UnRUQndIQ0pEWUZGTHJFVkxwZEhXcVBjM0E0OHFBTDguIiwic2NwIjoib3BlbmlkIHByb2ZpbGUgVXNlci5SZWFkIGVtYWlsIiwic3ViIjoiQWNzRk14TEg3V3BELXR6cl9Tb1doTlhCTE5hUTRZdmRlaVMtb3NiZVZNTSIsInRlbmFudF9yZWdpb25fc2NvcGUiOiJBUyIsInRpZCI6Ijg1MGFhNzhkLTk0ZTEtNGJjNi05Y2YzLThjMTFiNTMwNzAxYyIsInVuaXF1ZV9uYW1lIjoiYW51cmFnLnJhdmlAaWl0Zy5hYy5pbiIsInVwbiI6ImFudXJhZy5yYXZpQGlpdGcuYWMuaW4iLCJ1dGkiOiJnT0w1dzRfZlAwQzdJQWtQeVp4b0FBIiwidmVyIjoiMS4wIiwieG1zX3N0Ijp7InN1YiI6ImtObS1WU1hmWDNzcHBNbUtQNEsycmh6cWpzZ1p0eGRWdFJRdmtQdjh5X2MifSwieG1zX3RjZHQiOjE1MjM1MjYwNzd9.QIYrMUzfSzvEbik3etTLtZpp-H_j4li9gVtY3kCAHVH2oIMs6IAu4-hURnp3o1T9hl_LflpnIJyLWF5Q3TJdnR9D-yera62ob18dUsnclyL9CR-nm4Uv5VC2rR_qGNSWylskCtMSjiL6LYF3NuJfyfiaTZOOm8CJ8KobN7P_ycq1ZnJ4Qtko2ZAO-YEvIkqUolipqh5AME8XAt7VchivDDabWRmzCNu_UngKuhcWKnPoD84saPyMOQIJlH_qeMW9RXNPH_DT5ToUePuemgYKEHz9VwM_V3u_DgpOTZooxBWtbIAGuChvobg6hX6Aahc9HK-AypmVwMKw10sn7cGZWQ"
  }
  ```
- Example Response on success
  ```javascript
  {
    "message": "success",
    "status": 200
  }
  ```
- Remarks:
  - a jwt cookie is sent along with the request which will later be used in all apis to authenticate the user


### 2 Create new Event
- For creating a new event
- URL
  ```http
  POST api/task/new/
  ```
- Request body structure

  | Parameter | Type | Required | Description |
  | :--- | :--- | :--- | :--- |
  | `club_name` | `string` | **Required**| Club name |
  | `title` | `string` | **Required**| Event Title |
  | `description` | `string` | **Required**| Event Description |
  | `date` | `date` | **Required**| Event Date |
  | `deadline` | `date` | **Not Required**| Event Deadline |
  | `time_from` | `time` | **Required**| Event Start time |
  | `time_to` | `time` | **Required**| Event End time |
  | `remainder` | `string` | **Required**| Event Remainder type |
  | `remainder_date` | `date` | **Not Required**| Event Remainder date |
  | `remainder_time` | `time` | **Not Required**| Event Remainder time |
  | `announcements` | `string` | **Not Required**| Event Announcements |
  | `resources_upload` | `files` | **Not Required**| Event Resources |
  | `author` | `int` | **Not Required**| Event Author |
  | `rsvp_users` | `list` | **Not Required**| Subscribed users |

- Example Input
  ```javascript
  {
   "club_name": "SWC",
   "title": "AP",
   "description": "AAPPA",
   "date": "2022-01-12",
   "deadline": "2022-01-13",
   "time_from": "00:12:00",
   "time_to": "12:12:00",
   "remainder": "Daily",
   "remainder_time": "04:44:00",
   "announcements": "",
   "resources_upload": null,
   "author": null
  }

  ```
- Example Response on success
  ```javascript
  {
    "id": 7,
    "club_name": "SWC",
    "title": "AP",
    "description": "AAPPA",
    "date": "2022-01-12",
    "deadline": "2022-01-13",
    "time_from": "00:12:00",
    "time_to": "12:12:00",
    "remainder": "Daily",
    "remainder_date": "2022-01-21",
    "remainder_time": "04:44:00",
    "announcements": "",
    "resources_upload": null,
    "author": null,
    "rsvp_users": []
  }
  ```
- Remarks:
  - *club_name* field must have following values : 
    - *SWC*
    - *CODING CLUB*
    - *AERO CLUB*
    - *ASTRO CLUB*
    - *CA CLUB*
    - *EE CLUB*
    - *PRAKRITI CLUB*
    - *FNC CLUB*
    - *ROBOTICS CLUB*
    - *ED CLUB*
    - *UG CLUB*
    - *ALCHER CLUB*
    - *TECHNICHE CLUB*
    - *SAIL CLUB*
    - *AI CLUB*
    - *CCD CLUB*
    - *OTHER CLUB*
  - *remainder* field must have following values :
    - *Daily*
    - *Weekly*
    - *Monthly*
    - *Week before*
    - *Custom*
  - *remainder_date* field should only be provided when *remainder* field have the value : *Custom*
  - *resources_upload* field can contain files of any format

### 3 Get Event detail
- For getting info of event
- URL
  ```http
  GET api/task/<int:pk>/
  ```
- Request body structure

  | Parameter | Type | Required | Description |
  | :--- | :--- | :--- | :--- |
  | `none` | `none` | | none |

- Example Input
  ```javascript
  {}
  ```
- Example Response on success
  ```javascript
  {
    "id": 7,
    "club_name": "SWC",
    "title": "AP",
    "description": "AAPPA",
    "date": "2022-01-12",
    "deadline": "2022-01-13",
    "time_from": "00:12:00",
    "time_to": "12:12:00",
    "remainder": "Daily",
    "remainder_date": "2022-01-21",
    "remainder_time": "04:44:00",
    "announcements": "",
    "resources_upload": null,
    "author": null,
    "rsvp_users": []
  }
  ```
- Example Response on Wrong Event id
  ```javascript
    {
      "detail": "Not found."
    }
  ```

### 4 Get All Events
- For getting all event's data
- URL
  ```http
  GET api/task/all
  ```
- Request body structure

  | Parameter | Type | Required | Description |
  | :--- | :--- | :--- | :--- |
  | `none` | `none` | | none |

- Example Input
  ```javascript
  {}
  ```
- Example Response on success
  ```javascript
  [
      {
          <individual event data 1>
      },
      {
          <individual event data 2>
      },
      {
          <individual event data 3>
      }
  ]
  ```
- Remarks:
  - it send all events even user subscribed that event or not.

### 5 Update Few Details of Events
- For updating few selected fields of an event
- URL
  ```http
  PATCH api/task/<int:pk>/edit_few/
  ```
- Request body structure

  | Parameter | Type | Required | Description |
  | :--- | :--- | :--- | :--- |
  | `field name` | `field type` | | check description in create event api |

- Example Input
  ```javascript
    {
     "club_name": "CODING CLUB",
     "title": "Updated AP",
     "description": "no desc",
    }

  ```
- Example Response on success
  ```javascript
  {
    "id": 7,
    "club_name": "CODING CLUB",
    "title": "Updated AP",
    "description": "no desc",
    "date": "2022-01-12",
    "deadline": "2022-01-13",
    "time_from": "00:12:00",
    "time_to": "12:12:00",
    "remainder": "Daily",
    "remainder_date": "2022-01-21",
    "remainder_time": "04:44:00",
    "announcements": "",
    "resources_upload": null,
    "author": null,
    "rsvp_users": []
  }
  ```
- Remarks:
  - only send those fields to this api which user wants to be updated with their appropriate format as specified in event creation api.

### 6 Update Whole Event
- For updating few fields/whole event
- URL
  ```http
  PUT api/task/<int:pk>/edit/
  ```
- Request body structure

  | Parameter | Type | Required | Description |
  | :--- | :--- | :--- | :--- |
  | `club_name` | `string` | **Required**| Club name |
  | `title` | `string` | **Required**| Event Title |
  | `description` | `string` | **Required**| Event Description |
  | `date` | `date` | **Required**| Event Date |
  | `deadline` | `date` | **Not Required**| Event Deadline |
  | `time_from` | `time` | **Required**| Event Start time |
  | `time_to` | `time` | **Required**| Event End time |
  | `remainder` | `string` | **Required**| Event Remainder type |
  | `remainder_date` | `date` | **Not Required**| Event Remainder date |
  | `remainder_time` | `time` | **Not Required**| Event Remainder time |
  | `announcements` | `string` | **Not Required**| Event Announcements |
  | `resources_upload` | `files` | **Not Required**| Event Resources |
  | `author` | `int` | **Not Required**| Event Author |
  | `rsvp_users` | `list` | **Not Required**| Subscribed users |

- Example Input
  ```javascript
  {
    "club_name": "SWC",
    "title": "AP",
    "description": "AAPPA",
    "date": "2022-01-12",
    "deadline": "2022-01-13",
    "time_from": "00:12:00",
    "time_to": "12:12:00",
    "remainder": "Daily",
    "remainder_date": "2022-01-21",
    "remainder_time": "04:44:00",
    "announcements": "",
    "resources_upload": null,
    "author": null,
    "rsvp_users": [
        1
    ]
  }
  ```
- Example Response on success
  ```javascript
  {
    "id": 7,
    "club_name": "SWC",
    "title": "AP",
    "description": "AAPPA",
    "date": "2022-01-12",
    "deadline": "2022-01-13",
    "time_from": "00:12:00",
    "time_to": "12:12:00",
    "remainder": "Daily",
    "remainder_date": "2022-01-21",
    "remainder_time": "04:44:00",
    "announcements": "",
    "resources_upload": null,
    "author": null,
    "rsvp_users": [
        1
    ]
  }
  ```
- Remarks:
  - prefer 4th api if you have to update few fields of a event.
  
### 7 Deleting an Event
- For deleting an event
- URL
  ```http
  DELETE api/task/<int:pk>/delete/
  ```
- Request body structure

  | Parameter | Type | Required | Description |
  | :--- | :--- | :--- | :--- |
  | `none` | `none` | | none |

- Example Input
  ```javascript
  {}
  ```
- Example Response on success
  ```javascript
  {}
  ```
- Remarks:
  - it only deletes the event if the request is sent by event creator or staff user.


### 8 List all RSVPed Events
- For Listing all the events on which user has clicked RSVP
- URL
  ```http
  GET rsvp/all/
  ```
- Request body structure

  | Parameter | Type | Required | Description |
  | :--- | :--- | :--- | :--- |
  | `none` | `none` |  | none |

- Example Input
  ```javascript
  {}
  ```
- Example Response on success and 0 events found
  ```javascript
  []
  ```
- Example Response on success and some events found
  ```javascript
  [
      { event 1},
      { event 2},
      { event 3}
  ]
  ```
- Example Response on Error
  ```javascript
  {
      "message":"no rsvp tasks"
  }
  ```
- Remarks:
  - event 1,2,3 above means a whole structure of event as per event create api.


### 9 List all not RSVPed Events
- For Listing all the events on which user has not clicked RSVP
- URL
  ```http
  GET rsvp/allother/
  ```
- Request body structure

  | Parameter | Type | Required | Description |
  | :--- | :--- | :--- | :--- |
  | `none` | `none` |  | none |

- Example Input
  ```javascript
  {}
  ```
- Example Response on success and 0 events found
  ```javascript
  []
  ```
- Example Response on success and some events found
  ```javascript
  [
      { event 1},
      { event 2},
      { event 3}
  ]
  ```
- Example Response on Error
  ```javascript
  {
      "message":"no new rsvp tasks"
  }
  ```
- Remarks:
  - event 1,2,3 above means a whole structure of event as per event create api.

### 10 List all RSVPed Events of specific club
- For Listing all the events of a club on which user has clicked RSVP
- URL
  ```http
  GET rsvp/allclub/<str:club_name>/
  ```
- Request body structure

  | Parameter | Type | Required | Description |
  | :--- | :--- | :--- | :--- |
  | `none` | `none` |  | none |

- Example Input
  ```javascript
  {}
  ```
- Example Response on success and 0 events found
  ```javascript
  []
  ```
- Example Response on success and some events found
  ```javascript
  [
      { event 1},
      { event 2},
      { event 3}
  ]
  ```
- Example Response on Error
  ```javascript
  {
      "message":"no rsvp tasks for club"
  }
  ```
- Remarks:
  - event 1,2,3 above means a whole structure of event as per event create api.


### 11 List all not RSVPed Events of specific club
- For Listing all the events of a club on which user has not clicked RSVP yet
- URL
  ```http
  GET rsvp/newclub/<str:club_name>/
  ```
- Request body structure

  | Parameter | Type | Required | Description |
  | :--- | :--- | :--- | :--- |
  | `none` | `none` |  | none |

- Example Input
  ```javascript
  {}
  ```
- Example Response on success and 0 events found
  ```javascript
  []
  ```
- Example Response on success and some events found
  ```javascript
  [
      { event 1},
      { event 2},
      { event 3}
  ]
  ```
- Example Response on Error
  ```javascript
  {
      "message":"no rsvp tasks for club"
  }
  ```
- Remarks:
  - event 1,2,3 above means a whole structure of event as per event create api.


### 12 Adding RSVP of a user to specific event
- For adding rsvp of a user to specific event
- URL
  ```http
  GET rsvp/event/<int:pk>
  ```
- Request body structure

  | Parameter | Type | Required | Description |
  | :--- | :--- | :--- | :--- |
  | `none` | `none` |  | none |

- Example Input
  ```javascript
  {}
  ```
- Example Response on success
  ```javascript
  {
      'message':'event rsvped'
  }
  ```
- Remarks:
  - this api will add the user in the list of interested people in event.

### 13 Removing RSVP of a user from specific event
- For removing rsvp of a user from specific event
- URL
  ```http
  GET unsubscribe/event/<int:pk>
  ```
- Request body structure

  | Parameter | Type | Required | Description |
  | :--- | :--- | :--- | :--- |
  | `none` | `none` |  | none |

- Example Input
  ```javascript
  {}
  ```
- Example Response on success
  ```javascript
  {
      'message':'event unsubscribed'
  }
  ```
- Remarks:
  - this api will remove the user from the list of interested people in event.


