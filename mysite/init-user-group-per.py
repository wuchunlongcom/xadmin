# -*- coding: utf-8 -*-

# 编程实现添加用户、组、权限

import os
import sys
import  django
print('python 版本: %s。\ndjango版本: %s。'%(sys.version, django.get_version()))

if __name__ == "__main__":
    
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
    django.setup()

    from django.contrib.auth.models import User, Group, Permission    
    from app.models import School, Threshold,CustomPage
    
    print('start create all user and group and permission')
            
    
    # 邮箱必须为真实的邮箱，xadmin登录时， 忘记了您的密码或用户名？ 找回密码用
    
    if not User.objects.filter(username = 'admin'): # 创建超级用户 
        User.objects.create_superuser('admin', 'wcl6005@126.com','admin')
    else:
        user = User.objects.get(username='admin')
        user.set_password('admin')
        user.save()

    user = User.objects.create_user('www', 'wwwchunlong@126.com','www')  # 创建普通用户
    user.is_staff = True # 允许登录后台，但你无权修改任何东西。 默认user.is_staff = False 不能登录后台。
    user.save()
    
    
    # 组Operator 添加School 增、删、改权限
    operatorGroup = Group.objects.create(name='Operator')
    operatorGroup.permissions.add(
        Permission.objects.get(name='Can add 学校'),   # 模型中定义的 ‘学校’
        Permission.objects.get(name='Can delete 学校'),
        Permission.objects.get(name='Can change 学校'), 
        Permission.objects.get(name='Can view 学校')   
    )
    operatorGroup.save()
     
    # 组Customer 添加 增、删、改权限
    customerGroup = Group.objects.create(name='Customer')
    customerGroup.permissions.add(
        Permission.objects.get(name='Can add 自定义页面，定时执行任务'),   # 模型中定义的 ‘自定义页面，定时执行任务’
        Permission.objects.get(name='Can delete 自定义页面，定时执行任务'),
        Permission.objects.get(name='Can change 自定义页面，定时执行任务'),
        Permission.objects.get(name='Can view 自定义页面，定时执行任务'),            
    )
    customerGroup.save()

    
    # 创建2个普通用户,添加组operatorGroup
    USER_NUM = 2
    for i in range(USER_NUM):
        user = User.objects.create_user('wj%s' % i, 'wj%s@test.com' % i,'123')
        user.is_staff = True # 允许登录后台, 但你无权修改任何东西。 默认user.is_staff = False 不能登录后台。
        user.is_superuser = False  # 超级管理员
        user.groups.add(operatorGroup) # 用户添加组
        user.save()          

    # 创建10个普通用户,添加组customerGroup
    USER_NUM = 10
    for i in range(USER_NUM):
        user = User.objects.create_user('wu%s' % i, 'wu%s@test.com' % i,'123')
        user.is_staff = True
        user.is_superuser = False
        user.groups.add(customerGroup)
        user.save()          
    
    print('end create all user and group and permission')
    
    
    from basedao import BaseDAO 
       
    items = {'name':'北京大学','address':'北京','num':10,'per':60}
    BaseDAO(School).save(items)

    items = [{'name':'清华大学','address':'北京','num':20,'per':30}, {'name':'复旦大学','address':'上海','num':30,'per':55}]
    BaseDAO(School).save_batch(items)


"""     
    items = [{'per':20}, {'per':50}]
    BaseDAO(Threshold).save_batch(items)
        
   
    # 创建4个普通用户，默认user.is_staff = False  不允许登录后台
    items = ['wj','kever','wcl6005','wu6005']
    items = [User.objects.create_user(username=i, password="123") for i in items]    
    #组添加用户   
    operatorGroup.user_set.set(items[:2]) 
    customerGroup.user_set.set(items[2:4]) 
"""    
