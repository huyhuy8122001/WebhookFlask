import requests

# url = "http://127.0.0.1:5000/"

# r = requests.post(url)
# print(r)




url = "http://178.128.110.168:8080/api/database/rows/table/1149/?user_field_names=true"

header = {
    "Authorization": "Token iFgDQSuA9HIKiUyF9G2oo8I099cIaPJu",
    "Content-Type": "application/json"
}

data = { 
    "timestamp": 0,
    "event_name": "string",
    "sender_id": 0,
    "recipient_id": 0,
    "text": "string"
    }

requests.post(
    url,
    headers=header,
    json= data
)
