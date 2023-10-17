import re
import json
import requests

request_data_dict = {
  "mautic.form_on_submit": [
    {
      "submission": {
        "id": 1026,
        "ipAddress": {
          "ipAddress": "2001:ee0:d748:6240:aa90:868d:a4fb:ce4c",
          "id": 46517,
          "ipDetails": {
            "city": "Ho Chi Minh City",
            "region": "Ho Chi Minh",
            "zipcode": None,
            "country": "Vietnam",
            "latitude": 10.822,
            "longitude": 106.6257,
            "isp": "",
            "organization": "",
            "timezone": "Asia\\/Ho_Chi_Minh",
            "extra": ""
          }
        },
        "form": {
          "id": 38,
          "name": "Form \\u0111\\u0103ng k\\u00fd (D\\u00f9ng th\\u1eed, T\\u01b0 v\\u1ea5n)",
          "alias": "dang_ky_tr",
          "category": None
        },
        "lead": {
          "id": 335253,
          "points": 0,
          "color": None,
          "fields": {
            "core": {
              "thiet_bi_dau_cuoi": {
                "id": 61,
                "group": "core",
                "label": "Thi\\u1ebft b\\u1ecb \\u0111\\u1ea7u cu\\u1ed1i",
                "alias": "thiet_bi_dau_cuoi",
                "type": "text",
                "properties": [],
                "value": None,
                "normalizedValue": None
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
                "value": None,
                "normalizedValue": ""
              },
              "cv1": {
                "id": 59,
                "group": "core",
                "label": "CV1",
                "alias": "cv1",
                "type": "url",
                "properties": [],
                "value": None,
                "normalizedValue": None
              },
              "vitriungtuyen": {
                "id": 58,
                "group": "core",
                "label": "V\\u1ecb tr\\u00ed \\u1ee9ng tuy\\u1ec3n",
                "alias": "vitriungtuyen",
                "type": "text",
                "properties": [],
                "value": None,
                "normalizedValue": None
              },
              "cv": {
                "id": 56,
                "group": "core",
                "label": "CV",
                "alias": "cv",
                "type": "text",
                "properties": [],
                "value": None,
                "normalizedValue": None
              },
              "comment": {
                "id": 55,
                "group": "core",
                "label": "Comment",
                "alias": "comment",
                "type": "text",
                "properties": [],
                "value": "Ghi ch\\u00fa",
                "normalizedValue": "Ghi ch\\u00fa"
              },
              "full_name": {
                "id": 53,
                "group": "core",
                "label": "Full Name",
                "alias": "full_name",
                "type": "text",
                "properties": [],
                "value": "Nguyen Quang Huy test form 23",
                "normalizedValue": "Nguyen Quang Huy test form 23"
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
                "value": None,
                "normalizedValue": None
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
                "value": None,
                "normalizedValue": None
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
                "value": None,
                "normalizedValue": None
              },
              "date_last_active": {
                "id": 48,
                "group": "core",
                "label": "Date Last Active",
                "alias": "date_last_active",
                "type": "datetime",
                "properties": [],
                "value": None,
                "normalizedValue": None
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
                "value": None,
                "normalizedValue": None
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
                "value": None,
                "normalizedValue": None
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
                "value": None,
                "normalizedValue": None
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
                "value": None,
                "normalizedValue": None
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
                "value": None,
                "normalizedValue": None
              },
              "firstname": {
                "id": 2,
                "group": "core",
                "label": "First Name",
                "alias": "firstname",
                "type": "text",
                "properties": [],
                "value": None,
                "normalizedValue": None
              },
              "lastname": {
                "id": 3,
                "group": "core",
                "label": "Last Name",
                "alias": "lastname",
                "type": "text",
                "properties": [],
                "value": None,
                "normalizedValue": None
              },
              "company": {
                "id": 4,
                "group": "core",
                "label": "Primary company",
                "alias": "company",
                "type": "text",
                "properties": [],
                "value": "test com23",
                "normalizedValue": "test com23"
              },
              "position": {
                "id": 5,
                "group": "core",
                "label": "Position",
                "alias": "position",
                "type": "text",
                "properties": [],
                "value": None,
                "normalizedValue": None
              },
              "email": {
                "id": 6,
                "group": "core",
                "label": "Email",
                "alias": "email",
                "type": "email",
                "properties": [],
                "value": "Nguyenquangtest23@gmail.com",
                "normalizedValue": "Nguyenquangtest23@gmail.com"
              },
              "mobile": {
                "id": 7,
                "group": "core",
                "label": "Mobile",
                "alias": "mobile",
                "type": "tel",
                "properties": [],
                "value": "889920201",
                "normalizedValue": "889920201"
              },
              "phone": {
                "id": 8,
                "group": "core",
                "label": "Phone",
                "alias": "phone",
                "type": "tel",
                "properties": [],
                "value": None,
                "normalizedValue": None
              },
              "points": {
                "id": 9,
                "group": "core",
                "label": "Points",
                "alias": "points",
                "type": "number",
                "properties": [],
                "value": None,
                "normalizedValue": None
              },
              "fax": {
                "id": 10,
                "group": "core",
                "label": "Fax",
                "alias": "fax",
                "type": "tel",
                "properties": [],
                "value": None,
                "normalizedValue": None
              },
              "address1": {
                "id": 11,
                "group": "core",
                "label": "Address Line 1",
                "alias": "address1",
                "type": "text",
                "properties": [],
                "value": None,
                "normalizedValue": None
              },
              "address2": {
                "id": 12,
                "group": "core",
                "label": "Address Line 2",
                "alias": "address2",
                "type": "text",
                "properties": [],
                "value": None,
                "normalizedValue": None
              },
              "city": {
                "id": 13,
                "group": "core",
                "label": "City",
                "alias": "city",
                "type": "text",
                "properties": [],
                "value": None,
                "normalizedValue": None
              },
              "state": {
                "id": 14,
                "group": "core",
                "label": "State",
                "alias": "state",
                "type": "region",
                "properties": [],
                "value": None,
                "normalizedValue": None
              },
              "zipcode": {
                "id": 15,
                "group": "core",
                "label": "Zip Code",
                "alias": "zipcode",
                "type": "text",
                "properties": [],
                "value": None,
                "normalizedValue": None
              },
              "country": {
                "id": 16,
                "group": "core",
                "label": "Country",
                "alias": "country",
                "type": "country",
                "properties": [],
                "value": None,
                "normalizedValue": None
              },
              "preferred_locale": {
                "id": 17,
                "group": "core",
                "label": "Preferred Locale",
                "alias": "preferred_locale",
                "type": "locale",
                "properties": [],
                "value": None,
                "normalizedValue": None
              },
              "timezone": {
                "id": 18,
                "group": "core",
                "label": "Preferred Timezone",
                "alias": "timezone",
                "type": "timezone",
                "properties": [],
                "value": None,
                "normalizedValue": None
              },
              "last_active": {
                "id": 19,
                "group": "core",
                "label": "Date Last Active",
                "alias": "last_active",
                "type": "datetime",
                "properties": [],
                "value": None,
                "normalizedValue": None
              },
              "attribution_date": {
                "id": 20,
                "group": "core",
                "label": "Attribution Date",
                "alias": "attribution_date",
                "type": "datetime",
                "properties": [],
                "value": None,
                "normalizedValue": None
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
                "value": None,
                "normalizedValue": None
              },
              "website": {
                "id": 22,
                "group": "core",
                "label": "Website",
                "alias": "website",
                "type": "url",
                "properties": [],
                "value": None,
                "normalizedValue": None
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
                "value": None,
                "normalizedValue": None
              },
              "foursquare": {
                "id": 24,
                "group": "social",
                "label": "Foursquare",
                "alias": "foursquare",
                "type": "text",
                "properties": [],
                "value": None,
                "normalizedValue": None
              },
              "instagram": {
                "id": 25,
                "group": "social",
                "label": "Instagram",
                "alias": "instagram",
                "type": "text",
                "properties": [],
                "value": None,
                "normalizedValue": None
              },
              "linkedin": {
                "id": 26,
                "group": "social",
                "label": "LinkedIn",
                "alias": "linkedin",
                "type": "text",
                "properties": [],
                "value": None,
                "normalizedValue": None
              },
              "skype": {
                "id": 27,
                "group": "social",
                "label": "Skype",
                "alias": "skype",
                "type": "text",
                "properties": [],
                "value": None,
                "normalizedValue": None
              },
              "twitter": {
                "id": 28,
                "group": "social",
                "label": "Twitter",
                "alias": "twitter",
                "type": "text",
                "properties": [],
                "value": None,
                "normalizedValue": None
              }
            },
            "personal": [],
            "professional": []
          }
        },
        "trackingId": None,
        "dateSubmitted": "2023-10-17T14:27:08+07:00",
        "referer": "https:\\/\\/am.epacific.net\\/s\\/forms\\/preview\\/38",
        "page": None,
        "results": {
          "ten": "Nguyen Quang Huy test form 23",
          "so_dien_thoai": 889920201,
          "email": "Nguyenquangtest23@gmail.com",
          "ten_cong_ty_to_chuc": "test com23",
          "chon_loai": "reg-consultancy",
          "ghi_chu": "Ghi ch\\u00fa",
          "xac_nhan1": "T\\u00f4i x\\u00e1c nh\\u1eadn"
        }
      },
      "timestamp": "2023-10-17T14:27:13+07:00"
    }
  ]
}

form_id = request_data_dict['mautic.form_on_submit'][0]['submission']['form']['id']
print(form_id)
if form_id == 38:

    print(form_id)

elif form_id == 1:

    print(form_id)