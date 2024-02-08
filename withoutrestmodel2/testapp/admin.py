from django.contrib import admin
from testapp.models import Student
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_diplay = ['name','rollno','marks','gf','bf']
admin.site.register(Student,StudentAdmin)
