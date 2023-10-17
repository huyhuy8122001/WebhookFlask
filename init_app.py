from flask import Flask, request, logging, Response
import requests
import json

# DATABASE_TOKEN = "iFgDQSuA9HIKiUyF9G2oo8I099cIaPJu"

# def create_row_baserow(timestamp, event_name, sender_id, recipient_id, text):
#     url = "http://178.128.110.168:8080/api/database/rows/table/1149/?user_field_names=true"

#     header = {
#         "Authorization": "Token iFgDQSuA9HIKiUyF9G2oo8I099cIaPJu",
#         "Content-Type": "application/json"
#     }

#     data = { 
#         "timestamp": timestamp,
#         "event_name": event_name,
#         "sender_id": sender_id,
#         "recipient_id": recipient_id,
#         "text": text
#         }

#     requests.post(
#         url,
#         headers=header,
#         json= data
#     )


app = Flask(__name__)

@app.route("/", methods=["POST"])
def hook():
    request_data = request.data
    print(request_data)
    print(type(request_data))
    # request_data_dict = json.loads(request_data.decode('utf-8'))
    # print(type(request_data_dict))
    
    return "Hello World"

if __name__ == "__main__":
    #app.run(host='0.0.0.0')
    app.run()