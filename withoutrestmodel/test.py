import requests
import json

#BASE_URL = 'http://127.0.0.1:8000/'
#END_POINT ='api/'
#def get_response(id):
#    resp = requests.get(BASE_URL + END_POINT + id)
    #if resp.status_code in range(200,300):
    #if resp.status_code == requests.codes.ok:
    #    print(f'Status Code: ',resp.status_code)
    #    print(resp.json())
    #else:
    #    print(f'Status Code: ',resp.status_code)
    #    print('The required resource is NOT available')
#    print(resp.status_code)
#    print(resp.json())
#id = input('Enter Id :')
#get_response(id)

#def get_all():
#    resp = requests.get(BASE_URL + END_POINT)
#    print(f'Status Code: ',resp.status_code)
#    print(resp.json())
#get_all()

#def create_resource():
#    new_emp = {
#    'eno':106,
#    'esal': 20000,
#    'eaddr': 'Vadlamuru'
#    }
#    resp = requests.post(BASE_URL + END_POINT, data = json.dumps(new_emp))
#    print(resp.status_code)
#    print(resp.json())

#create_resource()

#def update_resource(id):
#    new_emp = {
#    'esal': 5555,
#    'eaddr': 'UK'
#    }
#    resp = requests.put(BASE_URL + END_POINT + str(id) + '/', data = json.dumps(new_emp))
#    print(resp.status_code)
#    print(resp.json())
#id = input('Enter id to Update:')
#update_resource(id)

#def delete_resource(id):
#    resp = requests.delete(BASE_URL + END_POINT + str(id) + '/')
#    print(f'Status Code: ',resp.status_code)
#    print(resp.json())

#    id = input('Enter id to Delete:')
#    delete_resource(id)

BASE_URL = 'http://127.0.0.1:8000/'
END_POINT ='api2/'
def get_resource(id = None):
    data = {}
    if id is not None:
        data ={
        'id':id
        }
    resp = requests.get(BASE_URL + END_POINT,data = json.dumps(data))
    print(resp.json())
    print(resp.status_code)

#id = input('Enter Id: ')
#get_resource(id)

def create_resource():
    new_emp ={
    'eno':108,
    'ename':'Ramu',
    'esal':7500,
    'eaddr':'UDA',
    }
    resp = requests.post(BASE_URL + END_POINT,data = json.dumps(new_emp))
    print(resp.status_code)
    print(resp.json())

#create_resource()

def update_resource(id):
    new_emp ={
    'id':id,
    'esal':9999,
    'eaddr':'Delhi',
    }
    resp = requests.put(BASE_URL + END_POINT,data = json.dumps(new_emp))
    print(resp.status_code)
    print(resp.json())

#id = input('Enter Id: ')
#update_resource(id)

def delete_resource(id):
    data={
    'id':id,
    }
    resp = requests.delete(BASE_URL + END_POINT,data = json.dumps(data))
    print(resp.status_code)
    print(resp.json())

id = input('Enter Id to Delete: ')
delete_resource(id)
