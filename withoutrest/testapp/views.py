from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def emp_data_view(request):
    emp_data ={
    'eno':101,
    'ename':'Sunny',
    'esal':12000,
    'eaddr':'Mumbai',
    }
    resp = '<h1>Employee Number:{}<br>Employee Name:{}<br>Employee Salary:{}<br>Employee Address:{}</h1>'.format(emp_data['eno'],emp_data['ename'],emp_data['esal'],emp_data['eaddr'])
    return HttpResponse(resp)

import json
def emp_data_jsonview(request):
    emp_data ={
    'eno':101,
    'ename':'Bunny',
    'esal':15000,
    'eaddr':'Delhi',
    }
    json_data = json.dumps(emp_data)
    return HttpResponse(json_data,content_type='application/json')

from django.http import JsonResponse
def emp_data_jsonview2(request):
    emp_data ={
    'eno':101,
    'ename':'Punny',
    'esal':18000,
    'eaddr':'Hyd',
    }
    return JsonResponse(emp_data)

from django.views.generic import View
from testapp.mixins import HttpResponseMixins
class JsonCBV(HttpResponseMixins,View):
    def get(self,request,*arg,**kwarg):
        json_data = json.dumps({'msg':'This is from get method'})
        return self.render_to_http_response(json_data)

    def post(self,request,*arg,**kwarg):
        json_data = json.dumps({'msg':'This is from post method'})
        return self.render_to_http_response(json_data)

    def put(self,request,*arg,**kwarg):
        json_data = json.dumps({'msg':'This is from put method'})
        return self.render_to_http_response(json_data)

    def delete(self,request,*arg,**kwarg):
        json_data = json.dumps({'msg':'This is from delete method'})
        return self.render_to_http_response(json_data)
