# users/views.py
import json
from django.shortcuts import render
from .models import School

from xadmin.views import CommAdminView
 
class SchoolView(CommAdminView):
    def get(self, request):
        context = super().get_context()   # 这一步是关键
        title = "自定义子菜单"     # 定义面包屑变量
        context["breadcrumbs"].append({'url': '/cwyadmin/', 'title': title})   
        context["title"] = title   
        
        # 从数据库获得数据，添加到context
        items = sum(School.objects.values_list('per', flat=True))//School.objects.all().count()
        name = '学校升学率统计'
        context.update({'tab':name, 'name':json.dumps(name), 'items':json.dumps(items)})
         
        return render(request, 'my-define/dashboard_school.html', context)  

