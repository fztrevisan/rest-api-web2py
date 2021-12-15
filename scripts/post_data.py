import requests
from requests.auth import HTTPBasicAuth 
# import jwt

payload = {
    "id": 1
}
auth=HTTPBasicAuth('trevisan.fernando@gmail.com', '123456')
tablename = "person"

r = requests.post(f"http://127.0.0.1:8000/myapp/default/api/{tablename}", data=payload, auth=auth)
print(r.status_code, r.reason)
print(r.content)