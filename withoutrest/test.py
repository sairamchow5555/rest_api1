import requests

BASE_URL = 'http://127.0.0.1:8000/'
END_POINT ='jsoncbv/'
resp = requests.post(BASE_URL + END_POINT)
#print(resp.json())
#print(type(resp.json()))
#print(type(resp))
data = resp.json()
#print('Data from Django Application')
#print('Employee Number:',data['eno'])
#print('Employee Salary:',data['esal'])
#print('Employee Location:',data['eaddr'])
print(data)
