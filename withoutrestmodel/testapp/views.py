from django.shortcuts import render
from testapp.models import Employee
from django.views.generic import View
import json
from django.http import HttpResponse
from django.core.serializers import serialize
from testapp.mixins import SerializeMixins
from testapp.mixins import HttpResponseMixins
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from testapp.utils import is_json
from testapp.forms import EmployeeForm
# Create your views here.
@method_decorator(csrf_exempt,name = 'dispatch')
class EmployeeCRUDCBV(HttpResponseMixins,SerializeMixins,View):
    def get_object_by_id(self,id):
        try:
            emp = Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            emp = None
        return emp

    def get(self,request,*args,**kwargs):
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            json_data = json.dumps({'msg':'Please send valid data only'})
            return self.render_to_http_response(json_data,status=400)
        pdata = json.loads(data)
        id = pdata.get('id',None)
        if id is not None:
            emp = self.get_object_by_id(id=id)
            if emp is None:
                json_data = json.dumps({'msg':'The requested resource not available with matched id'})
                return self.render_to_http_response(json_data,status=404)
            json_data = self.serialize([emp])
            return self.render_to_http_response(json_data)
        qs = Employee.objects.all()
        json_data = self.serialize(qs)
        return self.render_to_http_response(json_data)

    def post(self,request,*args,**kwargs):
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            json_data = json.dumps({'msg':'Please send valid data only'})
            return self.render_to_http_response(json_data,status=400)
        empdata = json.loads(data)
        form = EmployeeForm(empdata)
        if form.is_valid():
            form.save(commit=True)
            json_data = json.dumps({'msg':'Resource created successfully'})
            return self.render_to_http_response(json_data)
        if form.errors:
            json_data = json.dumps(form.errors)
            return self.render_to_http_response(json_data,status=400)


    def put(self,request,*args,**kwargs):
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            json_data = json.dumps({'msg':'Please send valid data only'})
            return self.render_to_http_response(json_data,status=400)
        pdata = json.loads(data)
        id = pdata.get('id',None)
        if id is None:
            json_data = json.dumps({'msg':'To perform updation id is mandatory, please provide'})
            return self.render_to_http_response(json_data,status=404)
        emp = self.get_object_by_id(id)
        if emp is None:
            json_data = json.dumps({'msg':'No resource with matched is, not possible to perform updation'})
            return self.render_to_http_response(json_data,status=404)
        provided_data = json.loads(data)
        original_data={
        'eno':emp.eno,
        'ename':emp.ename,
        'esal':emp.esal,
        'eaddr':emp.eaddr,
        }
        original_data.update(provided_data)
        form = EmployeeForm(original_data,instance=emp)
        if form.is_valid():
            form.save(commit=True)
            json_data = json.dumps({'msg':'Resource updated successfully'})
            return self.render_to_http_response(json_data)
        if form.errors:
            json_data = json.dumps(form.errors)
            return self.render_to_http_response(json_data,status=400)

    def delete(self,request,*args,**kwargs):
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            json_data = json.dumps({'msg':'Please send valid data only'})
            return self.render_to_http_response(json_data,status=400)
        pdata = json.loads(data)
        id = pdata.get('id',None)
        if id is not None:
            emp = self.get_object_by_id(id)
            if emp is None:
                json_data = json.dumps({'msg':'The required resource not available with matched id'})
                return self.render_to_http_response(json_data,status=404)
            status,deleted_item = emp.delete()
            if status == 1:
                json_data = json.dumps({'msg':'Resource deleted successfully'})
                return self.render_to_http_response(json_data)
            json_data = json.dumps({'msg':'Unable to delete....pls try again'})
            return self.render_to_http_response(json_data)
        json_data = json.dumps({'msg':'To perform deletion id is mandatory'})
        return self.render_to_http_response(json_data,status=404)






@method_decorator(csrf_exempt,name = 'dispatch')
class EmployeeDetailCBV(HttpResponseMixins,SerializeMixins,View):
    def get(self,request,id,*args,**kwargs):
        try:
            emp = Employee.objects.get(id = id)
        except Employee.DoesNotExist:
            json_data = json.dumps({'msg':'The required resource is NOT available'})
            return self.render_to_http_response(json_data,status = 404)
        else:
            json_data = self.serialize([emp,])
        return self.render_to_http_response(json_data)

    def get_object_by_id(self,id):
        try:
            emp = Employee.objects.get(id = id)
        except Employee.DoesNotExist:
            emp = None
        return emp

    def put(self,request,id,*args,**kwargs):
        emp = self.get_object_by_id(id)
        if emp is None:
            json_data = json.dumps({'msg':'No Matched resource found'})
            return self.render_to_http_response(json_data,status = 404)
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            json_data = json.dumps({'msg':'Please send valid data only'})
            return self.render_to_http_response(json_data,status = 400)
        provided_data = json.loads(data)
        original_data = {
        'eno':emp.eno,
        'ename':emp.ename,
        'esal':emp.esal,
        'eaddr':emp.eaddr
        }
        original_data.update(provided_data)
        form = EmployeeForm(original_data,instance=emp)
        if form.is_valid():
            form.save(commit = True)
            json_data = json.dumps({'msg':'Data Updated Successfully'})
            return self.render_to_http_response(json_data)
        if form.errors:
            json_data = json.dumps(form.errors)
            return self.render_to_http_response(json_data,status = 400)

    def delete(self,request,id,*args,**kwargs):
        emp = self.get_object_by_id(id)
        if emp is None:
            json_data = json.dumps({'msg':'No Matched resource found to Delete'})
            return self.render_to_http_response(json_data,status = 404)
        t = emp.delete() #return type of tuple
        #print(t)
        status, deleted_obj = t
        if status == 1:
            json_data = json.dumps({'msg':'Data Deletd Successfully'})
            return self.render_to_http_response(json_data)
        json_data = json.dumps({'msg':'Unable to Delete Data'})
        return self.render_to_http_response(json_data)

#class EmployeeDetailCBV(SerializeMixins,View):
#    def get(self,request,id,*args,**kwargs):
#        emp = Employee.objects.get(id=id)
#        json_data = self.serialize([emp,])
#        return HttpResponse(json_data,content_type='application/json')

@method_decorator(csrf_exempt,name = 'dispatch')
class EmployeeListCBV(HttpResponseMixins,SerializeMixins,View):
    def get(self,request,*args,**kwargs):
        qs = Employee.objects.all()
        json_data = self.serialize(qs)
        return HttpResponse(json_data,content_type='application/json')

    def post(self,request,*args,**kwargs):
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            json_data = json.dumps({'msg':'Please send valid data only'})
            return self.render_to_http_response(json_data,status = 400)
        emp_data = json.loads(data)
        form = EmployeeForm(emp_data)
        if form.is_valid():
            form.save(commit = True)
            json_data = json.dumps({'msg':'The data inserted Successfully'})
            return self.render_to_http_response(json_data)
        if form.errors:
            json_data = json.dumps(form.errors)
            return self.render_to_http_response(json_data,status = 400)
