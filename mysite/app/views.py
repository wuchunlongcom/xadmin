# users/views.py
import json
from django.shortcuts import render
from .models import School

def SchoolItemsView(request):
        items = sum(School.objects.values_list('per', flat=True))//School.objects.all().count()         
        return render(request, 'my-define/dashboard_school.html', context=locals()) 




'''
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.base import View
from django.contrib.auth.decorators import login_required

from .models import School
class SchoolItemsView(View):
                
    def get(self, request):
        items = sum(School.objects.values_list('per', flat=True))//School.objects.all().count() 
        
        return render(request, 'my-define/dashboard_school.html', context=locals()) 
    
from myAPI.fileAPI import read_txt, write_txt

def dashboard_temp(mode, field, label):
    """
    1、获取数据库中，某个整形字段的平均值；
    2、读模板文件，获得读模板文件字符串
    3、替换字符串
    4、将替换过的字符串，写入到新的模板文件
    """
    c = mode.objects.all().count()
    items = sum(mode.objects.values_list(field, flat=True))//c if c else 0 
        
    print('============',items)
           
    template_file = 'xadmin/templates/my-define/dashboard_template.html'
    OBJECT_TEMPLATE = "my-define/dashboard.html"     
    new_template_file = 'xadmin/templates/%s' %OBJECT_TEMPLATE
    
    text = read_txt(template_file)
    if not text:
        return '' 
    text = text.replace('disk_total_json',label)
    text = text.replace('disk_val',str(items))
    if not write_txt(new_template_file, text):
        return ''
    return OBJECT_TEMPLATE

'''