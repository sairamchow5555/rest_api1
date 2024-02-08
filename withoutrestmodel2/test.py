import requests
import json

BASE_URL = 'http://127.0.0.1:8000/'
END_POINT ='api/'
def get_resource(id = None):
    data = {}
    if id is not None:
        data ={
        'id':id
        }
    resp = requests.get(BASE_URL + END_POINT,data = json.dumps(data))
    print(resp.json())
    print(resp.status_code)

# id = input('Enter Id: ')
# get_resource()

def create_resource():
    new_emp ={
    'name':input('Enter Name: '),
    'rollno':int(input('Enter rollno: ')),
    'marks':int(input('Enter Marks: ')),
    'gf':input('Enter GF Name: '),
    'bf':input('Enter BF Name: ')
    }
    resp = requests.post(BASE_URL + END_POINT,data = json.dumps(new_emp))
    print(resp.status_code)
    print(resp.json())

# create_resource()

def update_resource(id):
    new_std ={
    'id':id,
    'marks':int(input('Enter Marks: ')),
    'gf':input('Enter GF ')
    }
    resp = requests.put(BASE_URL + END_POINT,data = json.dumps(new_std))
    print(resp.status_code)
    print(resp.json())

# id = input('Enter Id: ')
# update_resource(id)

def delete_resource(id):
    data={
    'id':id,
    }
    resp = requests.delete(BASE_URL + END_POINT,data = json.dumps(data))
    print(resp.status_code)
    print(resp.json())

# id = input('Enter Id to Delete: ')
# delete_resource(id)


while True:
    print('1. GET')
    print('2. POST')
    print('3. PUT')
    print('4. DELETE')
    print('5. EXIST')
    option = int(input('Select Option :'))
    if option == 1:
        id = input('Enter ID to Detials :')
        get_resource(id)
    if option == 2:
        create_resource()
    if option == 3:
        id = input('Enter ID to Update :')
        update_resource(id)
    if option == 4:
        id = input('Enter Id to Delete :')
        delete_resource(id)
    if option == 5:
        break
    else:
        print('Enter a Valid option')
