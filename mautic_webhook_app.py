from flask import Flask, request, logging, Response
import requests
import json

DATABASE_TOKEN = "iFgDQSuA9HIKiUyF9G2oo8I099cIaPJu"

def create_row_baserow(submission_id, contact_id, date_submitted, ip_address, vi_tri_ung_tuyen, ho_ten, sdt, email, gioi_thieu_ban_than, cv_file, chinh_sach_va_dieu_khoan):
    url = "http://178.128.110.168:8080/api/database/rows/table/1156/?user_field_names=true"

    header = {
        "Authorization": f"Token {DATABASE_TOKEN}",
        "Content-Type": "application/json"
    }

    data = { 
        "Submission ID": submission_id,
        "Contact ID": contact_id,
        "Date Submitted": date_submitted,
        "IP address": ip_address,
        "Vị trí ứng tuyển": vi_tri_ung_tuyen,
        "Họ tên đầy đủ của bạn": ho_ten,
        "Số di động của bạn": sdt,
        "Email nhận kết quả tuyển": email,
        "Giới thiệu bản thân (không bắt buộc)": gioi_thieu_ban_than,
        "CV của bạn": cv_file,
        "Chính sách và điều khoản": chinh_sach_va_dieu_khoan
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
    
    form_on_submit = request_data_dict['mautic.form_on_submit'][0]['submission']
    
    submission_id = form_on_submit['id']
    contact_id = form_on_submit['lead']['id']
    date_submitted = form_on_submit['dateSubmitted']
    ip_address = form_on_submit['ipAddress']['ipAddress']
    vi_tri_ung_tuyen = form_on_submit['results']['vi_tri_ung_tuyen2']
    ho_ten = form_on_submit['results']['ho_ten_day_du_cua_ban']
    sdt = form_on_submit['results']['so_di_dong_cua_ban']
    email = form_on_submit['results']['email_nhan_ket_qua_tuyen']
    gioi_thieu_ban_than = form_on_submit['results']['gioi_thieu_ban_than_khong']
    cv_file = form_on_submit['results']['cv_cua_ban']
    chinh_sach_va_dieu_khoan = form_on_submit['results']['label']
    
    create_row_baserow(submission_id, contact_id, date_submitted, ip_address, vi_tri_ung_tuyen, ho_ten, sdt, email, gioi_thieu_ban_than, cv_file, chinh_sach_va_dieu_khoan)
    
    return "Hello World"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
