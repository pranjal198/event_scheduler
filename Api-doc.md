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
- For logging in user using microsoft account/username & password
- URL for microsoft login
  ```http
  POST apiLogin/
  ```
- URL for password login
  ```http
  POST passwordLogin/
  ```
- Request body structure for microsoft login

  | Parameter | Type | Required | Description |
  | :--- | :--- | :--- | :--- |
  | `token` | `string` | **Required** | token issued by Microsoft Azure |

- Request body structure for password login

  | Parameter | Type | Required | Description |
  | :--- | :--- | :--- | :--- |
  | `username` | `string` | **Required** | username |
  | `password` | `string` | **Required** | password |

- Example Input 1
  ```javascript
  {
    "token":"eyJ0eXAiOiJKV1QiLCJub25jZSI6ImZySTRVSThOSFpvdEZ4MTlvWmpTVFNLSzhUZFJZOFlaRDFJNjdvYTZEN2ciLCJhbGciOiJSUzI1NiIsIng1dCI6Ik1yNS1BVWliZkJpaTdOZDFqQmViYXhib1hXMCIsImtpZCI6Ik1yNS1BVWliZkJpaTdOZDFqQmViYXhib1hXMCJ9.eyJhdWQiOiIwMDAwMDAwMy0wMDAwLTAwMDAtYzAwMC0wMDAwMDAwMDAwMDAiLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC84NTBhYTc4ZC05NGUxLTRiYzYtOWNmMy04YzExYjUzMDcwMWMvIiwiaWF0IjoxNjQyODMzOTQ4LCJuYmYiOjE2NDI4MzM5NDgsImV4cCI6MTY0MjgzNzkyNywiYWNjdCI6MCwiYWNyIjoiMSIsImFpbyI6IkUyWmdZRmhtcWY0bW83WGorOVVWaThyTnZVTlVPS3dQTGVhS1hYNmVxV0JiNUgzeks2Y0EiLCJhbXIiOlsicHdkIl0sImFwcF9kaXNwbGF5bmFtZSI6IkV2ZW50IFNjaCIsImFwcGlkIjoiNTE2MDQzMjItYWM0Yi00YjQ1LWE1ZDEtZDZhOGY3MzcwMzhmIiwiYXBwaWRhY3IiOiIwIiwiZmFtaWx5X25hbWUiOiIyMDAxMDEwMTciLCJnaXZlbl9uYW1lIjoiQU5VUkFHIFJBVkkiLCJpZHR5cCI6InVzZXIiLCJpcGFkZHIiOiIyMDMuODkuOTcuNjciLCJuYW1lIjoiQU5VUkFHIFJBVkkiLCJvaWQiOiI4YzRmMjMyOC1jNDI3LTQyYTEtYWNhYS1mMjZjYWQwN2IyM2YiLCJwbGF0ZiI6IjMiLCJwdWlkIjoiMTAwMzIwMDBGNjdEQ0VGNiIsInJoIjoiMC5BU29BamFjS2hlR1V4a3VjODR3UnRUQndIQ0pEWUZGTHJFVkxwZEhXcVBjM0E0OHFBTDguIiwic2NwIjoib3BlbmlkIHByb2ZpbGUgVXNlci5SZWFkIGVtYWlsIiwic3ViIjoiQWNzRk14TEg3V3BELXR6cl9Tb1doTlhCTE5hUTRZdmRlaVMtb3NiZVZNTSIsInRlbmFudF9yZWdpb25fc2NvcGUiOiJBUyIsInRpZCI6Ijg1MGFhNzhkLTk0ZTEtNGJjNi05Y2YzLThjMTFiNTMwNzAxYyIsInVuaXF1ZV9uYW1lIjoiYW51cmFnLnJhdmlAaWl0Zy5hYy5pbiIsInVwbiI6ImFudXJhZy5yYXZpQGlpdGcuYWMuaW4iLCJ1dGkiOiJnT0w1dzRfZlAwQzdJQWtQeVp4b0FBIiwidmVyIjoiMS4wIiwieG1zX3N0Ijp7InN1YiI6ImtObS1WU1hmWDNzcHBNbUtQNEsycmh6cWpzZ1p0eGRWdFJRdmtQdjh5X2MifSwieG1zX3RjZHQiOjE1MjM1MjYwNzd9.QIYrMUzfSzvEbik3etTLtZpp-H_j4li9gVtY3kCAHVH2oIMs6IAu4-hURnp3o1T9hl_LflpnIJyLWF5Q3TJdnR9D-yera62ob18dUsnclyL9CR-nm4Uv5VC2rR_qGNSWylskCtMSjiL6LYF3NuJfyfiaTZOOm8CJ8KobN7P_ycq1ZnJ4Qtko2ZAO-YEvIkqUolipqh5AME8XAt7VchivDDabWRmzCNu_UngKuhcWKnPoD84saPyMOQIJlH_qeMW9RXNPH_DT5ToUePuemgYKEHz9VwM_V3u_DgpOTZooxBWtbIAGuChvobg6hX6Aahc9HK-AypmVwMKw10sn7cGZWQ"
  }
  ```
- Example Input 2
  ```javascript
  {
    "username": "abcd",
    "password": "efgh"
  }
  ```

- Example Response on success
  ```javascript
  {
    "message": "success",
    "status": 200,
    "jwt":"token....."
  }
  ```
- Remarks:
  - A **jwt token as cookie, header and as a jwt field** is sent along with the **response** which will later be used in all apis to authenticate the user
  - Token will be **Access Token** in case of request from **Frontend Website** and **ID Token** in case of request from **App**
  - In all other api's, request must be sent along with **Authorization** header and its value must be the **jwt token** sent by Login API
  - Example:- **request['Authorization'] = eyJ0eXai...........**


### Event Model
- Event structure

  | Parameter | Type | Required | Description |
  | :--- | :--- | :--- | :--- |
  | `club_name` | `string` | **Required**| Club name |
  | `title` | `string` | **Required**| Event Title |
  | `subtitle` | `string` | **Required**| Event Subtitle |
  | `description` | `string` | **Not Required**| Event Description |
  | `image` | `image` | **Not Required**| Event Image/Logo |
  | `date` | `date` | **Not Required**| Event Starting date |
  | `deadline` | `date` | **Not Required**| Event End date |
  | `time_from` | `time` | **Not Required**| Event Starting Time |
  | `time_to` | `time` | **Not Required**| Event End Time |
  | `remainder` | `string` | **Not Required**| Event Remainder type |
  | `remainder_date` | `time` | **Not Required**| Event Remainder Date |
  | `remainder_time` | `time` | **Not Required**| Event Remainder Time |
  | `host` | `list` | **Not Required**| List of Event Host's profile id |
  | `speaker` | `list` | **Not Required**| List of Event Speaker's profile id |
  | `guests` | `json` | **Not Required**| List of Event Guests |
  | `Location` | `json` | **Not Required**| Object of Event location data |
  | `announcement` | `json` | **Not Required**| Object of Event announcement data |
  | `resources_upload` | `json` | **Not Required**| List of Event resources files |
  | `drive_links` | `json` | **Not Required**| List of Event drive links |
  | `payment` | `json` | **Not Required**| Object of Event payment data |
  | `rsvp_users` | `list` | **Not Required**| List of Event attendee's profile id |
  | `emails` | `json` | **Not Required**| Object of Event email data |
  | `page_view` | `json` | **Not Required**| Object of Event daily traffic data |
  | `feedback` | `json` | **Not Required**| Object of Event feedback data |
- Example event
  ```javascript
  {
      "club_name":"SWC",
      
      "title":"demo event",
      "subtitle":"demo",
      "description":"descriptive",
      "image":"/event-scheduler/media/events/event-1/event_logo.jpg",

      "date":"2022-02-12",
      "deadline":"2022-02-14",
      "time_from": "00:12:00",
      "time_from": "12:12:00",
      "remainder": "Custom",
      "remainder_date": "2022-02-11",
      "remainder_time": "04:44:00",
      
      "host":[1,2,3],
      "speaker":[1,2,3],
      "guests":[
          {
              "id":1,
              "name":"guest 1",
              "email":"abc@gmail.com",
              "designation":"SDE at Microsoft",
              "batch":2014,
          },
          {
              "id":2,
              "name":"guest 2",
              "email":"efg@gmail.com",
              "designation":"Product Manager at Apple",
              "batch":2015,
          }
          ],
      "location":{
          "offline":{
              "latitude":"27.2046° N",
              "longitude":"77.4977° E"
          },
          "online":{
              "meet_url":"meet/google.com/abd-efg-hij",
              "room_id":"abc123",
              "password":"abc@123"
          }
      },
      "announcement":{
          "fixed":[
              {
                  "id":1,
                  "announcement":"all participants must fill the google form"
              },
              {
                  "id":2,
                  "announcement":"share the links to your friends"
              }
          ],
          "dynamic":[
              {
                  "id":1,
                  "date":"2022-02-12",
                  "time":"21:30:00",
                  "announcement":"we will be starting at 10:00 pm"
              },
              {
                  "id":2,
                  "date":"2022-02-12",
                  "time":"23:00:00",
                  "announcement":"please fill the feedback form"
              },
          ],
      },
      "resources_upload":[
            {
                "id": 1,
                "filename": "testfile",
                "url": "/event-scheduler/media/events/event-2/resources/testfile.pdf"
            },
            {
                "id": 2,
                "filename": "rules",
                "url": "/event-scheduler/media/events/event-2/resources/rules.jpeg"
            },
      ]
      "drive_links":[
          {
              "id":1,
              "filename":"guidelines.pdf",
              "link":"drive.google.com/askddhswe/suiojsdoijsddsd"
          },
          {
              "id":2,
              "filename":"results.pdf",
              "link":"drive.google.com/askddhswe/suiojsdoijsddsd"
          },
      ],
      "payment":{
          "paid":true,
          "metadata":{
              "price":499,
              "link":"https://abcd.payment/com/?pay=499"
          }
      },
      
      "rsvp_users":[1,2,3,4,8,9],
      "emails":{
          "registration":{
              "to":["a@gmail.com","b@yahoo.com"],
              "sub":"register now for abc event",
              "body":"abcd",
          },
          "scheduled":[
              {
                  "id":1,
                  "to":["a@gmail.com","b@yahoo.com"],
                  "sub":"hurry up register now for abc event",
                  "body":"abcd",
                  "date":"2022-02-15",
                  "time":"09:00:00",
              },
              {
                  "id":2,
                  "to":["a@gmail.com","b@yahoo.com"],
                  "sub":"join fast",
                  "body":"abcd",
                  "date":"2022-02-15",
                  "time":"10:00:00",
              },
          ]
      },
      
      "page_view":{
          "2022-02-12": [1],
          "2022-02-13": [2,9,45],
          "2022-02-14": [3],
          "2022-02-15": [4,8,9],
          "2022-02-16": [5,2,3,1],
          "2022-02-17": [7,4,5,9,1],
      },
      "feedback":{
          "1":[1,2],
          "2":[3],
          "3":[4],
          "4":[5,6],
          "5":[7,8,9,10],
      }
  }
  ```
- All the operations on nested fields like **guests**, **location**, **announcement**, **drive_links**, **payment**, **emails** and **resources_upload** should be done by **7th, 8th and 9th API** only
- All the lists containing numbers are actually user's profile id
- In **location** field no need to give details of online as well as offline field, any one should work
- **announcements** are of two types
  - **fixed** (visible to all from the time of creation)
  - **dynamic** (visible to all from the time specified)
- **emails** are of two types
  - **registration** (send to all at the time of event announcement)
  - **scheduled** (send to all at the time specified)
- **page_view** contains daily traffic on event's page
- **feedback** contains user feedback after completion of event

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

- Example Input
  ```javascript
  {
   "club_name": "SWC",
   "title": "AP",
   "description": "AAPPA",
  }

  ```
- Example Response on success
  ```javascript
  {
    "id": 7,
    "club_name": "SWC",
    "title": "AP",
    "subtitle": "",
    "description": "AAPPA",
    "image": null,
    "date": "2022-02-12",
    "deadline": "2022-02-12",
    "time_from": "15:42:37",
    "time_to": "15:42:37",
    "remainder": "None",
    "remainder_date": "2022-02-12",
    "remainder_time": "15:42:37",
    "guests": [],
    "location": {
      "offline": {
        "latitude": "",
        "longitude": ""
      },
      "online": {
        "meet_url": "",
        "room_id": "",
        "password": ""
      }
    },
    "announcement": {
      "fixed": [],
      "dynamic": []
    },
    "resources_upload": [],
    "drive_links": [],
    "payment": {
      "paid": false,
      "metadata": {
        "price": 0,
        "link": ""
      }
    },
    "emails": {
      "registration": {
        "to": [],
        "sub": "",
        "body": ""
      },
      "scheduled": []
    },
    "page_view": {},
    "feedback": {
      "1": [],
      "2": [],
      "3": [],
      "4": [],
      "5": []
    },
    "host": [],
    "speaker": [],
    "rsvp_users": []
  }
  ```
- Remarks:
  - The above 3 fields **club_name** , **title** , **description** is always required, along with that you can also send other fields data, but make sure to adhere to the format as of event structure
  - we suggest that, better not provide any other data here and use other api's to perform the other operations
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
  - Other not required field's data:
   - *remainder* field must have following values :
     - *Daily*
     - *Weekly*
     - *Monthly*
     - *Week before*
     - *Custom*
   - *remainder_date* field should only be provided when *remainder* field have the value : *Custom*


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
    "subtitle": "",
    "description": "AAPPA",
    "image": null,
    "date": "2022-02-12",
    "deadline": "2022-02-12",
    "time_from": "15:42:37",
    "time_to": "15:42:37",
    "remainder": "None",
    "remainder_date": "2022-02-12",
    "remainder_time": "15:42:37",
    "guests": [],
    "location": {
      "offline": {
        "latitude": "",
        "longitude": ""
      },
      "online": {
        "meet_url": "",
        "room_id": "",
        "password": ""
      }
    },
    "announcement": {
      "fixed": [],
      "dynamic": []
    },
    "resources_upload": [],
    "drive_links": [],
    "payment": {
      "paid": false,
      "metadata": {
        "price": 0,
        "link": ""
      }
    },
    "emails": {
      "registration": {
        "to": [],
        "sub": "",
        "body": ""
      },
      "scheduled": []
    },
    "page_view": {},
    "feedback": {
      "1": [],
      "2": [],
      "3": [],
      "4": [],
      "5": []
    },
    "host": [],
    "speaker": [],
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
- For updating few selected fields of an event which can't be done using 7th, 8th and 9th api
- URL
  ```http
  PATCH api/task/<int:pk>/edit_few/
  ```
- Request body structure (only these fields must be updated via this api)

  | Parameter | Type | Required | Description |
  | :--- | :--- | :--- | :--- |
  | `field name` | `field type` | | check description in create event api or see demo event object after login api |

- Example Input (**Note:- club_name cannot be a field in the input**)
  ```javascript
    {
     "title": "Updated AP",
     "description": "no desc",
    }

  ```
- Example Response on success
  ```javascript
  {
    "id": 7,
    "club_name": "SWC",
    "title": "Updated AP",
    "subtitle": "",
    "description": "no desc",
    "image": null,
    "date": "2022-02-12",
    "deadline": "2022-02-12",
    "time_from": "15:42:37",
    "time_to": "15:42:37",
    "remainder": "None",
    "remainder_date": "2022-02-12",
    "remainder_time": "15:42:37",
    "guests": [],
    "location": {
      "offline": {
        "latitude": "",
        "longitude": ""
      },
      "online": {
        "meet_url": "",
        "room_id": "",
        "password": ""
      }
    },
    "announcement": {
      "fixed": [],
      "dynamic": []
    },
    "resources_upload": [],
    "drive_links": [],
    "payment": {
      "paid": false,
      "metadata": {
        "price": 0,
        "link": ""
      }
    },
    "emails": {
      "registration": {
        "to": [],
        "sub": "",
        "body": ""
      },
      "scheduled": []
    },
    "page_view": {},
    "feedback": {
      "1": [],
      "2": [],
      "3": [],
      "4": [],
      "5": []
    },
    "host": [],
    "speaker": [],
    "rsvp_users": []
  }
  ```
- Remarks:
  - only send those fields to this api which user wants to be updated with their appropriate format as specified in event creation api or demo event object.

### 6 Update Whole Event
- For updating few fields/whole event
- Make sure to provide data in specified json format only
- URL
  ```http
  PUT api/task/<int:pk>/edit/
  ```

- Example Input
  ```javascript
  {
    "id": 7,
    "club_name": "SWC",
    "title": "updated title",
    "subtitle": "",
    "description": "updated decription",
    "image": null,
    "date": "2022-02-12",
    "deadline": "2022-02-12",
    "time_from": "15:42:37",
    "time_to": "15:42:37",
    "remainder": "None",
    "remainder_date": "2022-02-12",
    "remainder_time": "15:42:37",
    "guests": [],
    "location": {
      "offline": {
        "latitude": "",
        "longitude": ""
      },
      "online": {
        "meet_url": "",
        "room_id": "",
        "password": ""
      }
    },
    "announcement": {
      "fixed": [],
      "dynamic": []
    },
    "resources_upload": [],
    "drive_links": [],
    "payment": {
      "paid": false,
      "metadata": {
        "price": 0,
        "link": ""
      }
    },
    "emails": {
      "registration": {
        "to": [],
        "sub": "",
        "body": ""
      },
      "scheduled": []
    },
    "page_view": {},
    "feedback": {
      "1": [],
      "2": [],
      "3": [],
      "4": [],
      "5": []
    },
    "host": [],
    "speaker": [],
    "rsvp_users": []
  }
  ```
- Example Response on success
  ```javascript
  {
    "id": 7,
    "club_name": "SWC",
    "title": "updated title",
    "subtitle": "",
    "description": "updated description",
    "image": null,
    "date": "2022-02-12",
    "deadline": "2022-02-12",
    "time_from": "15:42:37.071718",
    "time_to": "15:42:37.071718",
    "remainder": "None",
    "remainder_date": "2022-02-12",
    "remainder_time": "15:42:37.072713",
    "guests": [],
    "location": {
      "offline": {
        "latitude": "",
        "longitude": ""
      },
      "online": {
        "meet_url": "",
        "room_id": "",
        "password": ""
      }
    },
    "announcement": {
      "fixed": [],
      "dynamic": []
    },
    "resources_upload": [],
    "drive_links": [],
    "payment": {
      "paid": false,
      "metadata": {
        "price": 0,
        "link": ""
      }
    },
    "emails": {
      "registration": {
        "to": [],
        "sub": "",
        "body": ""
      },
      "scheduled": []
    },
    "page_view": {},
    "feedback": {
      "1": [],
      "2": [],
      "3": [],
      "4": [],
      "5": []
    },
    "host": [],
    "speaker": [],
    "rsvp_users": []
  }
  ```
- Remarks:
  - prefer 4th api if you have to update few fields of an event.
  - prefer 7th,8th and 9th api if you have to update nested json fields of an event.
  
### 7 Add/Update/Delete Nested Fields
- For adding/updating/deleting all the nested fields individually
- URL
  ```http
  PUT api/task/<int:pk>/edit_json/
  ```
- Request body structure

  | Parameter | Type | Required | Description |
  | :--- | :--- | :--- | :--- |
  | `method` | `string` | **Required**| Any one of ADD/UPDATE/DELETE |
  | `field` | `string` | **Required**| Field on which crud operations should be performed  |
  | `mode` | `string` | **Not Required**| This value is required for specific fields, for more details see examples |
  | `id` | `int` | **Not Required**| Only required for UPDATE and DELETE option |
  | `file` | `file` | **Not Required**| Only required for resources_upload field |
  | `data` | `json/string` | **Not Required**| Only required for ADD and UPDATE option |

#### field = guests
  - It is a list of all guest objects
  - Example Input for adding guests
    ```javascript
    {
      "method": "ADD",
      "field": "guests",
      "data": {
                  "name":"guest 1",
                  "email":"abc@gmail.com",
                  "designation":"SDE at Microsoft",
                  "batch":2014,
          }
    }
    ```
  - Example Input for updating guests
    ```javascript
    {
      "method": "UPDATE",
      "field": "guests",
      "id":1,
      "data": {
                  "name":"guest 2",
                  "email":"efg@gmail.com",
                  "designation":"SDE at Google",
                  "batch":2015,
          }
    }
    ```
  - Example Input for deleting guests
    ```javascript
    {
      "method": "DELETE",
      "field": "guests",
      "id":1
    }
    ```

#### field = location
  - It has two types:
    - offline
    - online
  - No **ADD** option for location field
  - Example Input for updating online location
    ```javascript
    {
      "method": "UPDATE",
      "field": "location",
      "mode": "online",
      "data": {
              "meet_url":"meet/google.com/abd-efg-hij",
              "room_id":"abc123",
              "password":"abc@123"
          }
    }
    ```
  - Example Input for updating offline location
    ```javascript
    {
      "method": "UPDATE",
      "field": "location",
      "mode": "offline",
      "data": {
              "latitude":"27.2046° N",
              "longitude":"77.4977° E"
          }
    }
    ```
  - Example Input for deleting online location
    ```javascript
    {
      "method": "DELETE",
      "field": "location",
      "mode": "online"
    }
    ```
  - Example Input for deleting offline location
    ```javascript
    {
      "method": "DELETE",
      "field": "location",
      "mode": "offline"
    }
    ```

#### field = announcement
  - It has two types:
    - fixed
    - dynamic
  - Both types of announcement are list which contain individual announcement object
  - Example Input for adding fixed announcement
    ```javascript
    {
      "method": "ADD",
      "field": "announcement",
      "mode":"fixed",
      "data": {
                  "announcement":"all participants must fill the google form"
          }
    }
    ```
  - Example Input for adding dynamic announcement
    ```javascript
    {
      "method": "ADD",
      "field": "announcement",
      "mode":"dynamic",
      "data": {
                  "date":"2022-02-12",
                  "time":"21:30:00",
                  "announcement":"we will be starting at 10:00 pm"
          }
    }
    ```
  - Example Input for updating fixed announcement
    ```javascript
    {
      "method": "UPDATE",
      "field": "announcement",
      "mode":"fixed",
      "id":1,
      "data": {
                  "announcement":"we will be starting at 10:30 pm"
          }
    }
    ```
  - Example Input for updating dynamic announcement
    ```javascript
    {
      "method": "UPDATE",
      "field": "announcement",
      "mode":"dynamic",
      "id":1,
      "data": {
                  "date":"2022-02-12",
                  "time":"21:30:00",
                  "announcement":"we will be starting at 10:30 pm"
          }
    }
    ```
  - Example Input for deleting fixed/dynamic announcement
    ```javascript
    {
      "method": "DELETE",
      "field": "announcement",
      "mode":"fixed/dynamic",
      "id":1
    }
    ```

#### field = drive_links
  - It is a list of all drive_links objects
  - Example Input for adding drive_links
    ```javascript
    {
      "method": "ADD",
      "field": "drive_links",
      "data": {
                  "filename":"guidelines.pdf",
                  "link":"drive.google.com/askddhswe/suiojsdoijsddsd"
          }
    }
    ```
  - Example Input for updating drive_links
    ```javascript
    {
      "method": "UPDATE",
      "field": "drive_links",
      "id":1,
      "data": {
                  "filename":"rules.pdf",
                  "link":"drive.google.com/123456789/suiojsdoijsddsd"
          }
    }
    ```
  - Example Input for deleting drive_links
    ```javascript
    {
      "method": "DELETE",
      "field": "drive_links",
      "id":1
    }
    ```

#### field = payment
  - It has two types:
    - paid (boolean)
    - metadata (other payment related data)
  - No need to provide values for **paid** parameter, it automatically sets according to method i.e. ADD/UPDATE make it true and DELETE makes it false
  - Example Input for adding payment
    ```javascript
    {
      "method": "ADD",
      "field": "payment",
      "data": {
              "price":499,
              "link":"https://abcd.payment/com/?pay=499"
          }
    }
    ```
  - Example Input for updating payment
    ```javascript
    {
      "method": "UPDATE",
      "field": "payment",
      "data": {
              "price":699,
              "link":"https://efgh.payment/com/?pay=699"
          }
    }
    ```
  - Example Input for deleting payment
    ```javascript
    {
      "method": "DELETE",
      "field": "payment",
    }
    ```

#### field = emails
  - It has two types:
    - registration (single object)
    - scheduled (list of email objects)
    - 
  - Example Input for adding registration emails
    ```javascript
    {
      "method": "ADD",
      "field": "emails",
      "mode":"registration",
      "data": {
                  "to":["a@gmail.com","b@yahoo.com"],
                  "sub":"register now for abc event",
                  "body":"abcd",
          }
    }
    ```
  - Example Input for adding scheduled emails
    ```javascript
    {
      "method": "ADD",
      "field": "emails",
      "mode":"scheduled",
      "data": {
                  "to":["a@gmail.com","b@yahoo.com"],
                  "sub":"join fast",
                  "body":"abcd",
                  "date":"2022-02-15",
                  "time":"10:00:00",
          }
    }
    ```
  - Example Input for updating registration emails
    ```javascript
    {
      "method": "UPDATE",
      "field": "emails",
      "mode":"registration",
      "data": {
                  "to":["a@gmail.com","b@yahoo.com"],
                  "sub":"register now for abc event",
                  "body":"abcd",
          }
    }
    ```
  - Example Input for updating scheduled emails
    ```javascript
    {
      "method": "UPDATE",
      "field": "emails",
      "mode":"scheduled",
      "id":1,
      "data": {
                  "to":["a@gmail.com","b@yahoo.com"],
                  "sub":"join fast",
                  "body":"abcd",
                  "date":"2022-02-15",
                  "time":"10:00:00",
          }
    }
    ```
  - Example Input for deleting registration emails
    ```javascript
    {
      "method": "DELETE",
      "field": "emails",
      "mode":"registration"
    }
    ```
  - Example Input for deleting scheduled emails
    ```javascript
    {
      "method": "DELETE",
      "field": "emails",
      "mode":"scheduled",
      "id":1
    }
    ```

#### field = resources_upload
  - It is a list of all resources objects
  - **file** field can have file of any format
  - **data** field must be a **string**, having filename (without extension)
  - file will be saved as **filename.ext** 
  - no **UPDATE** method available for this option
  - Example Input for adding resources
    ```javascript
    {
      "method": "ADD",
      "field": "resources_upload",
      "file::<file of any format>
      "data": "filename"
    }
    ```
  - Example Input for deleting resources
    ```javascript
    {
      "method": "DELETE",
      "field": "resources_upload",
      "id":1
    }
    ```


- Example response on error
  ```javascript
  {
    "message":"please provide vaild parameters",
    "status":404
  }
  ```
- Remarks:
     - just by providing proper values for **method** and **field** this api can do crud operations for that field successfully.
     - each time on success, the whole event data will be returned through response
  
### 8 Add page view to event analytics data
- For adding views for event page
- URL
  ```http
  GET api/task/<int:pk>/add_view/
  ```
- Request body structure

  | Parameter | Type | Required | Description |
  | :--- | :--- | :--- | :--- |
  | `none` | `none` | **none**| none |

- Example Input
  ```javascript
  {
  }
  ```
- Example Response on success
  ```javascript
  {
    "message": "ok"
  }
  ```
- Remarks:
  - call this api when user visits the event detail page
  
### 9 Adding feedback of user
- For adding feedback of user
- URL
  ```http
  POST api/task/<int:pk>/feedback/
  ```
- Request body structure

  | Parameter | Type | Required | Description |
  | :--- | :--- | :--- | :--- |
  | `rating` | `string` | **Required**| 1 to 5 |

- Example Input
  ```javascript
  {
    "rating": "4"
  }
  ```
- Example Response on success
  ```javascript
  {
    "message": "feedback added"
  }
  ```
- Remarks:
  - please note that **rating** is **string**, not **int**
  - if user has already given feedback then previous feedback will be erasen and current feedback will be added
  
### 10 Deleting an Event
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


### 11 List all RSVPed Events
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


### 12 List all not RSVPed Events
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

### 13 List all RSVPed Events of specific club
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


### 14 List all not RSVPed Events of specific club
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


### 15 Adding RSVP of a user to specific event
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

### 16 Removing RSVP of a user from specific event
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


