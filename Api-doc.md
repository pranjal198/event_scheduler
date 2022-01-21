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

### 1 Create new Event
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
  | `remainder_date` | `date` | **Required**| Event Remainder date |
  | `remainder_time` | `time` | **Required**| Event Remainder time |
  | `announcements` | `string` | **Not Required**| Event Announcements |
  | `resources_upload` | `files` | **Not Required**| Event Resources |
  | `author` | `int` | **Not Required**| Event Author |
  | `rsvp_users` | `list` | **Required**| Subscribed users |

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
    - *SWC*
    - *SWC*
    - *SWC*
  - *remainder* field must have following values :
    - *Daily*
    - *Weekly*
    - *Monthly*
    - *Week before*
    - *Custom*
  - *remainder_date* field should only be provided when *remainder* field have the value : *Custom*
  - *resources_upload* field can contain files of any format

### 2 Get Event detail
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

### 3 Get All Events
- For getting all event's data
- URL
  ```http
  GET 'api/task/all
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

### 4 Update Few Details of Events
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

### 5 Update Whole Event
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
  | `remainder_date` | `date` | **Required**| Event Remainder date |
  | `remainder_time` | `time` | **Required**| Event Remainder time |
  | `announcements` | `string` | **Not Required**| Event Announcements |
  | `resources_upload` | `files` | **Not Required**| Event Resources |
  | `author` | `int` | **Not Required**| Event Author |
  | `rsvp_users` | `list` | **Required**| Subscribed users |

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
  
### 6 Deleting an Event
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


### 7 List all RSVPed Events
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


### 8 List all not RSVPed Events
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

### 9 List all RSVPed Events of specific club
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


### 10 List all not RSVPed Events of specific club
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


### 11 Adding RSVP of a user to specific event
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

### 12 Removing RSVP of a user from specific event
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


