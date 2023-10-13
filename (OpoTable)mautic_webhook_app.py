from flask import Flask, request, logging, Response
import requests
import json

DATABASE_TOKEN = "iFgDQSuA9HIKiUyF9G2oo8I099cIaPJu"

def create_row_baserow(contact_id, full_name, firstname, lastname, mobile, phone, email, last_active, points, stage, company, position, website, comment):
    url = "http://178.128.110.168:8080/api/database/rows/table/1160/?user_field_names=true"

    header = {
        "Authorization": f"Token {DATABASE_TOKEN}",
        "Content-Type": "application/json"
    }

    data = { 
        "ID": contact_id,
        "points": points,
        "last_active": last_active,
        "firstname": firstname,
        "lastname": lastname,
        "company": company,
        "position": position,
        "email": email,
        "phone": phone,
        "mobile": mobile,
        "website": website,
        "full_name": full_name,
        "comment": comment,
        "Stage": stage,
    }

    requests.post(
        url,
        headers=header,
        json= data
    )

def create_row_baserow_opportunities_table(submission_id, opportunitie_name,contact_id, comment, dateSubmitted):
    url = "http://178.128.110.168:8080/api/database/rows/table/1165/?user_field_names=true"

    header = {
        "Authorization": f"Token {DATABASE_TOKEN}",
        "Content-Type": "application/json"
    }

    data = { 
        "ID": submission_id,
        "Date Submitted": dateSubmitted,
        "ghi chú": comment,
        "Contact": [
            contact_id
        ],
        "Opportunitie name": opportunitie_name,
    }

    requests.post(
        url,
        headers=header,
        json= data
    )

app = Flask(__name__)

@app.route("/", methods=["POST"])
def hook():
    request_data = request.data
    print(request_data)
    print(type(request_data))
    request_data_dict = json.loads(request_data.decode('utf-8'))
    print(type(request_data_dict))
    
    if list(request_data_dict.keys())[0] == "mautic.lead_post_save_new":
    
        contact_data = request_data_dict['mautic.lead_post_save_new'][0]['contact']
        
        contact_id = contact_data['id']
        full_name = contact_data['fields']['core']['full_name']['value']
        firstname = contact_data['fields']['core']['firstname']['value']
        lastname = contact_data['fields']['core']['lastname']['value']
        mobile = contact_data['fields']['core']['mobile']['value']
        phone = contact_data['fields']['core']['phone']['value']
        email = contact_data['fields']['core']['email']['value']
        last_active = contact_data['lastActive']
        points = contact_data['points']
        stage = contact_data['stage']
        company = contact_data['fields']['core']['company']['value']
        position = contact_data['fields']['core']['position']['value']
        website = contact_data['fields']['core']['website']['value']
        comment = contact_data['fields']['core']['comment']['value']
        
        #create_row_baserow(submission_id, contact_id, date_submitted, ip_address, vi_tri_ung_tuyen, ho_ten, sdt, email, gioi_thieu_ban_than, cv_file, chinh_sach_va_dieu_khoan)
        create_row_baserow(contact_id, full_name, firstname, lastname, mobile, phone, email, last_active, points, stage, company, position, website, comment)
        
    elif list(request_data_dict.keys())[0] == "mautic.form_on_submit":
        
        form_on_submit = request_data_dict['mautic.form_on_submit'][0]['submission']
        
        submission_id = form_on_submit['id']
        opportunitie_name = form_on_submit['results']['chon_loai']
        contact_id = form_on_submit['lead']['id']
        comment = form_on_submit['lead']['id']['comment']['value']
        dateSubmitted = form_on_submit['dateSubmitted']
        
        create_row_baserow_opportunities_table(submission_id, opportunitie_name, contact_id, comment, dateSubmitted)
        
    return "Hello World"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
