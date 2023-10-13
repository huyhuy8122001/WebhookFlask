import re
import json
import requests

request_data = b"{
  "mautic.lead_post_save_new": [
    {
      "contact": {
        "isPublished": true,
        "dateAdded": "2023-10-12T23:00:14+07:00",
        "dateModified": "2023-10-12T23:00:14+07:00",
        "createdBy": null,
        "createdByUser": null,
        "modifiedBy": 27,
        "modifiedByUser": "Huy Nguyen",
        "id": 333337,
        "points": 0,
        "color": null,
        "fields": {
          "core": {
            "thiet_bi_dau_cuoi": {
              "id": 61,
              "group": "core",
              "label": "Thi\\u1ebft b\\u1ecb \\u0111\\u1ea7u cu\\u1ed1i",
              "alias": "thiet_bi_dau_cuoi",
              "type": "text",
              "properties": [],
              "value": "",
              "normalizedValue": ""
            },
            "vai_tro": {
              "id": 60,
              "group": "core",
              "label": "Vai tr\\u00f2",
              "alias": "vai_tro",
              "type": "multiselect",
              "properties": {
                "list": [
                  {
                    "label": "Ng\\u01b0\\u1eddi quy\\u1ebft",
                    "value": "Ng\\u01b0\\u1eddi quy\\u1ebft"
                  },
                  {
                    "label": "Ng\\u01b0\\u1eddi quy\\u1ebft &#38; duy\\u1ec7t",
                    "value": "Ng\\u01b0\\u1eddi quy\\u1ebft &#38; duy\\u1ec7t"
                  },
                  {
                    "label": "Ng\\u01b0\\u1eddi duy\\u1ec7t",
                    "value": "Ng\\u01b0\\u1eddi duy\\u1ec7t"
                  },
                  {
                    "label": "Ng\\u01b0\\u1eddi x\\u00e9t",
                    "value": "Ng\\u01b0\\u1eddi x\\u00e9t"
                  },
                  {
                    "label": "Ng\\u01b0\\u1eddi d\\u00f9ng",
                    "value": "Ng\\u01b0\\u1eddi d\\u00f9ng"
                  }
                ]
              },
              "value": "",
              "normalizedValue": ""
            },
            "cv1": {
              "id": 59,
              "group": "core",
              "label": "CV1",
              "alias": "cv1",
              "type": "url",
              "properties": [],
              "value": "",
              "normalizedValue": ""
            },
            "vitriungtuyen": {
              "id": 58,
              "group": "core",
              "label": "V\\u1ecb tr\\u00ed \\u1ee9ng tuy\\u1ec3n",
              "alias": "vitriungtuyen",
              "type": "text",
              "properties": [],
              "value": "",
              "normalizedValue": ""
            },
            "cv": {
              "id": 56,
              "group": "core",
              "label": "CV",
              "alias": "cv",
              "type": "text",
              "properties": [],
              "value": "",
              "normalizedValue": ""
            },
            "comment": {
              "id": 55,
              "group": "core",
              "label": "Comment",
              "alias": "comment",
              "type": "text",
              "properties": [],
              "value": "",
              "normalizedValue": ""
            },
            "full_name": {
              "id": 53,
              "group": "core",
              "label": "Full Name",
              "alias": "full_name",
              "type": "text",
              "properties": [],
              "value": "Huy Quang Quang",
              "normalizedValue": "Huy Quang Quang"
            },
            "role": {
              "id": 52,
              "group": "core",
              "label": "Role",
              "alias": "role",
              "type": "select",
              "properties": {
                "list": [
                  {
                    "label": "Individual Contributor",
                    "value": "Individual Contributor"
                  },
                  {
                    "label": "Manager",
                    "value": "Manager"
                  },
                  {
                    "label": "Director",
                    "value": "Director"
                  },
                  {
                    "label": "Executive",
                    "value": "Executive"
                  },
                  {
                    "label": "Consultant",
                    "value": "Consultant"
                  }
                ]
              },
              "value": "",
              "normalizedValue": ""
            },
            "nps__recommend": {
              "id": 51,
              "group": "core",
              "label": "NPS - Recommend",
              "alias": "nps__recommend",
              "type": "number",
              "properties": {
                "roundmode": "3",
                "scale": ""
              },
              "value": "",
              "normalizedValue": ""
            },
            "products": {
              "id": 50,
              "group": "core",
              "label": "Products",
              "alias": "products",
              "type": "select",
              "properties": {
                "list": [
                  {
                    "label": "CCALL PRO",
                    "value": "CCALL PRO"
                  },
                  {
                    "label": "CCALL Business",
                    "value": "CCALL Business"
                  },
                  {
                    "label": "special",
                    "value": "special"
                  },
                  {
                    "label": "12 thang",
                    "value": "12 thang"
                  },
                  {
                    "label": "24 thang",
                    "value": "24 thang"
                  }
                ]
              },
              "value": "",
              "normalizedValue": ""
            },
            "date_last_active": {
              "id": 48,
              "group": "core",
              "label": "Date Last Active",
              "alias": "date_last_active",
              "type": "datetime",
              "properties": [],
              "value": "",
              "normalizedValue": ""
            },
            "haspurchased": {
              "id": 47,
              "group": "core",
              "label": "hasPurchased",
              "alias": "haspurchased",
              "type": "boolean",
              "properties": {
                "no": "No",
                "yes": "Yes"
              },
              "value": "",
              "normalizedValue": ""
            },
            "subscription_status": {
              "id": 46,
              "group": "core",
              "label": "Subscription Status",
              "alias": "subscription_status",
              "type": "select",
              "properties": {
                "list": [
                  {
                    "label": "New",
                    "value": "New"
                  },
                  {
                    "label": "Existing",
                    "value": "Existing"
                  },
                  {
                    "label": "Former",
                    "value": "Former"
                  }
                ]
              },
              "value": "",
              "normalizedValue": ""
            },
            "prospect_or_customer": {
              "id": 45,
              "group": "core",
              "label": "Prospect or Customer",
              "alias": "prospect_or_customer",
              "type": "select",
              "properties": {
                "list": [
                  {
                    "label": "Prospect",
                    "value": "Prospect"
                  },
                  {
                    "label": "Customer",
                    "value": "Customer"
                  }
                ]
              },
              "value": "",
              "normalizedValue": ""
            },
            "b2b_or_b2c": {
              "id": 44,
              "group": "core",
              "label": "B2B or B2C",
              "alias": "b2b_or_b2c",
              "type": "select",
              "properties": {
                "list": [
                  {
                    "label": "B2B",
                    "value": "B2B"
                  },
                  {
                    "label": "B2C",
                    "value": "B2C"
                  }
                ]
              },
              "value": "",
              "normalizedValue": ""
            },
            "title": {
              "id": 1,
              "group": "core",
              "label": "Title",
              "alias": "title",
              "type": "lookup",
              "properties": {
                "list": [
                  "Mr",
                  "Mrs",
                  "Miss"
                ]
              },
              "value": "",
              "normalizedValue": ""
            },
            "firstname": {
              "id": 2,
              "group": "core",
              "label": "First Name",
              "alias": "firstname",
              "type": "text",
              "properties": [],
              "value": "Huy",
              "normalizedValue": "Huy"
            },
            "lastname": {
              "id": 3,
              "group": "core",
              "label": "Last Name",
              "alias": "lastname",
              "type": "text",
              "properties": [],
              "value": "Quang Nguyen Test 6",
              "normalizedValue": "Quang Nguyen Test 6"
            },
            "company": {
              "id": 4,
              "group": "core",
              "label": "Primary company",
              "alias": "company",
              "type": "text",
              "properties": [],
              "value": "",
              "normalizedValue": ""
            },
            "position": {
              "id": 5,
              "group": "core",
              "label": "Position",
              "alias": "position",
              "type": "text",
              "properties": [],
              "value": "",
              "normalizedValue": ""
            },
            "email": {
              "id": 6,
              "group": "core",
              "label": "Email",
              "alias": "email",
              "type": "email",
              "properties": [],
              "value": "nguyenquanghuytest6@gmail.com",
              "normalizedValue": "nguyenquanghuytest6@gmail.com"
            },
            "mobile": {
              "id": 7,
              "group": "core",
              "label": "Mobile",
              "alias": "mobile",
              "type": "tel",
              "properties": [],
              "value": "0889920135",
              "normalizedValue": "0889920135"
            },
            "phone": {
              "id": 8,
              "group": "core",
              "label": "Phone",
              "alias": "phone",
              "type": "tel",
              "properties": [],
              "value": "",
              "normalizedValue": ""
            },
            "points": {
              "id": 9,
              "group": "core",
              "label": "Points",
              "alias": "points",
              "type": "number",
              "properties": [],
              "value": 0,
              "normalizedValue": 0
            },
            "fax": {
              "id": 10,
              "group": "core",
              "label": "Fax",
              "alias": "fax",
              "type": "tel",
              "properties": [],
              "value": "",
              "normalizedValue": ""
            },
            "address1": {
              "id": 11,
              "group": "core",
              "label": "Address Line 1",
              "alias": "address1",
              "type": "text",
              "properties": [],
              "value": "783 Tran Xuan Soan",
              "normalizedValue": "783 Tran Xuan Soan"
            },
            "address2": {
              "id": 12,
              "group": "core",
              "label": "Address Line 2",
              "alias": "address2",
              "type": "text",
              "properties": [],
              "value": "",
              "normalizedValue": ""
            },
            "city": {
              "id": 13,
              "group": "core",
              "label": "City",
              "alias": "city",
              "type": "text",
              "properties": [],
              "value": "Ho Chi Minh City",
              "normalizedValue": "Ho Chi Minh City"
            },
            "state": {
              "id": 14,
              "group": "core",
              "label": "State",
              "alias": "state",
              "type": "region",
              "properties": [],
              "value": "",
              "normalizedValue": ""
            },
            "zipcode": {
              "id": 15,
              "group": "core",
              "label": "Zip Code",
              "alias": "zipcode",
              "type": "text",
              "properties": [],
              "value": "32000",
              "normalizedValue": "32000"
            },
            "country": {
              "id": 16,
              "group": "core",
              "label": "Country",
              "alias": "country",
              "type": "country",
              "properties": [],
              "value": "Vietnam",
              "normalizedValue": "Vietnam"
            },
            "preferred_locale": {
              "id": 17,
              "group": "core",
              "label": "Preferred Locale",
              "alias": "preferred_locale",
              "type": "locale",
              "properties": [],
              "value": "",
              "normalizedValue": ""
            },
            "timezone": {
              "id": 18,
              "group": "core",
              "label": "Preferred Timezone",
              "alias": "timezone",
              "type": "timezone",
              "properties": [],
              "value": "",
              "normalizedValue": ""
            },
            "last_active": {
              "id": 19,
              "group": "core",
              "label": "Date Last Active",
              "alias": "last_active",
              "type": "datetime",
              "properties": [],
              "value": "",
              "normalizedValue": ""
            },
            "attribution_date": {
              "id": 20,
              "group": "core",
              "label": "Attribution Date",
              "alias": "attribution_date",
              "type": "datetime",
              "properties": [],
              "value": "",
              "normalizedValue": ""
            },
            "attribution": {
              "id": 21,
              "group": "core",
              "label": "Attribution",
              "alias": "attribution",
              "type": "number",
              "properties": {
                "roundmode": 4,
                "scale": 2
              },
              "value": "",
              "normalizedValue": ""
            },
            "website": {
              "id": 22,
              "group": "core",
              "label": "Website",
              "alias": "website",
              "type": "url",
              "properties": [],
              "value": "",
              "normalizedValue": ""
            }
          },
          "social": {
            "facebook": {
              "id": 23,
              "group": "social",
              "label": "Facebook",
              "alias": "facebook",
              "type": "text",
              "properties": [],
              "value": "",
              "normalizedValue": ""
            },
            "foursquare": {
              "id": 24,
              "group": "social",
              "label": "Foursquare",
              "alias": "foursquare",
              "type": "text",
              "properties": [],
              "value": "",
              "normalizedValue": ""
            },
            "instagram": {
              "id": 25,
              "group": "social",
              "label": "Instagram",
              "alias": "instagram",
              "type": "text",
              "properties": [],
              "value": "",
              "normalizedValue": ""
            },
            "linkedin": {
              "id": 26,
              "group": "social",
              "label": "LinkedIn",
              "alias": "linkedin",
              "type": "text",
              "properties": [],
              "value": "",
              "normalizedValue": ""
            },
            "skype": {
              "id": 27,
              "group": "social",
              "label": "Skype",
              "alias": "skype",
              "type": "text",
              "properties": [],
              "value": "",
              "normalizedValue": ""
            },
            "twitter": {
              "id": 28,
              "group": "social",
              "label": "Twitter",
              "alias": "twitter",
              "type": "text",
              "properties": [],
              "value": "",
              "normalizedValue": ""
            }
          },
          "personal": [],
          "professional": []
        },
        "lastActive": null,
        "owner": {
          "createdByUser": "Th\\u1ea3o Nguy\\u1ec5n",
          "modifiedByUser": null,
          "id": 27,
          "username": "HuyNguyen",
          "firstName": "Huy",
          "lastName": "Nguyen"
        },
        "ipAddresses": [],
        "tags": [],
        "utmtags": null,
        "stage": null,
        "dateIdentified": "2023-10-12T23:00:14+07:00",
        "preferredProfileImage": "gravatar",
        "doNotContact": [],
        "frequencyRules": []
      },
      "timestamp": "2023-10-12T23:00:14+07:00"
    }
  ]}"

# print(type(request_data))

# request_data_replace_null = re.sub(b"null", b'None', request_data) 

# request_data_dict = json.loads(request_data.decode('utf-8'))

# form_on_submit = request_data_dict['mautic.form_on_submit'][0]['submission']

# submission_id = form_on_submit['id']
# contact_id = form_on_submit['lead']['id']
# date_submitted = form_on_submit['dateSubmitted']
# ip_address = form_on_submit['ipAddress']['ipAddress']
# vi_tri_ung_tuyen = form_on_submit['results']['vi_tri_ung_tuyen2']
# ho_ten = form_on_submit['results']['ho_ten_day_du_cua_ban']
# sdt = form_on_submit['results']['so_di_dong_cua_ban']
# email = form_on_submit['results']['email_nhan_ket_qua_tuyen']
# gioi_thieu_ban_than = form_on_submit['results']['gioi_thieu_ban_than_khong']
# cv_file = form_on_submit['results']['cv_cua_ban']
# chinh_sach_va_dieu_khoan = form_on_submit['results']['label']

# print(submission_id)
# print(contact_id)
# print(date_submitted)
# print(ip_address)
# print(vi_tri_ung_tuyen)


DATABASE_TOKEN = "iFgDQSuA9HIKiUyF9G2oo8I099cIaPJu"

contact_id = contact_data['id']
full_name = contact_data['fields']['core']['full_name']['value']
firstname = contact_data['fields']['core']['firstname']['value']
lastname = contact_data['fields']['core']['lastname']['value']
mobile = contact_data['fields']['core']['mobile']['value']
phone = contact_data['fields']['core']['phone']['value']
email = contact_data['fields']['core']['email']['value']
last_active = contact_data['fields']['core']['last_active']['value']
points = contact_data['points']
stage = contact_data['stage']
company = contact_data['fields']['core']['company']['value']
position = contact_data['fields']['core']['position']['value']
website = contact_data['fields']['core']['website']['value']
comment = contact_data['fields']['core']['comment']['value']


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

#create_row_baserow(submission_id, contact_id, date_submitted, ip_address, vi_tri_ung_tuyen, ho_ten, sdt, email, gioi_thieu_ban_than, cv_file, chinh_sach_va_dieu_khoan)