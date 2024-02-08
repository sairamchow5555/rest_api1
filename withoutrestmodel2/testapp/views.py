from django.shortcuts import render
from django.views.generic import View
from testapp.utils import is_json
from testapp.mixins import *
from testapp.models import  *
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from testapp.forms import *
# Create your views here.

@method_decorator(csrf_exempt,name = 'dispatch')
class StudentCRUDCBV(HttpResponseMixins,SerializeMixins,View):
    def get_object_by_id(self,id):
        try:
            s = Student.objects.get(id = id)
        except Student.DoesNotExist:
            s = None
        return s

    def get(self,request,*args,**kwargs):
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            return self.render_to_http_response(json.dumps({'msg':'Provide valid Json data'}),status = 404)
        py_data = json.loads(data)
        id = py_data.get('id',None)
        if id is not None:
            std = self.get_object_by_id(id)
            if std is None:
                return self.render_to_http_response(json.dumps({'msg':'No Matched data is found'}),status = 404)
            json_data = self.serialize([std,])
            return self.render_to_http_response(json_data)
        qs = Student.objects.all()
        json_data = self.serialize(qs)
        return self.render_to_http_response(json_data)

    def post(self,request,*args,**kwargs):
        data = request.body
        valid_json = is_json(data)
        if not valid_json:
            return self.render_to_http_response(json.dumps({'msg':'Provide valid Json Data'}),status=400)
        std_data = json.loads(data)
        form = StudentForm(std_data)
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
            return self.render_to_http_response(json.dumps({'msg':'Provide valid Json Data'}),status=400)
        pdata = json.loads(data)
        id = pdata.get('id',None)
        if id is None:
            return self.render_to_http_response(json.dumps({'msg':'To perform updation id is mandatory, please provide'}),status=404)
        std = self.get_object_by_id(id)
        if std is None:
            return self.render_to_http_response(json.dumps({'msg':'No resource with matched id, not possible to perform updation'}),status=404)
        provided_data = json.loads(data)
        original_data={
        'name':std.name,
        'rollno':std.rollno,
        'marks':std.marks,
        'gf':std.gf,
        'bf':std.bf
        }
        original_data.update(provided_data)
        form = StudentForm(original_data,instance=std)
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
            return self.render_to_http_response(json.dumps({'msg':'Please send valid data only'}),status=400)
        pdata = json.loads(data)
        id = pdata.get('id',None)
        if id is not None:
            std = self.get_object_by_id(id)
            if std is None:
                return self.render_to_http_response(json.dumps({'msg':'The required resource not available with matched id'}),status=404)
            status,deleted_item = std.delete()
            if status == 1:
                return self.render_to_http_response(json.dumps({'msg':'Resource deleted successfully'}))
            return self.render_to_http_response(json.dumps({'msg':'Unable to delete....pls try again'}))
        return self.render_to_http_response(json.dumps({'msg':'To perform deletion id is mandatory, please provide'}),status=404)
