from flask import Flask, request, logging, Response
import requests
import json

DATABASE_TOKEN = "A2WseJWQzGQmTKWv540A1PnsJp3PU7ms"

host = "http://report.hq-devlab.cloud:8080"
table_id = 836
field_id = 'field_7506'

def search_row_id(contact_id):
    url = f"{host}/api/database/rows/table/{table_id}/?user_field_names=true&filter__{field_id}__equal={contact_id}"

    header = {
        "Authorization": f"Token {DATABASE_TOKEN}",
        "Content-Type": "application/json"
    }

    data = requests.get(
        url,
        headers=header
    )

    data_dict = data.json()
    
    row_id = data_dict['results'][0]['id']
    return row_id



def update_row(row_id, points, last_active):

    url = f"{host}/api/database/rows/table/{table_id}/{row_id}/?user_field_names=true"

    header = {
        "Authorization": f"Token {DATABASE_TOKEN}",
        "Content-Type": "application/json"
    }

    body = {
        "points": points,
        "last_active": last_active
    }

    data = requests.patch(
        url,
        headers=header,
        json=body
    )

    return data.json()


update_row(row_id=search_row_id(28580), last_active="2023-10-20T09:47:14Z", points=37)

