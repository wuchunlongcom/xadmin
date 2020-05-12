# users/views.py


def work():
    from .models import School  
    dashboard_temp(School, 'per', '升学率统计') # 仪表盘模板 
    

def dashboard_temp(mode, field, label):
    """ 仪表盘模板
    1、获取数据库中，某个整形字段的平均值；
    2、读模板文件，获得读模板文件字符串；
    3、替换字符串；
    4、将替换过的字符串，写入到新的模板文件；
    5、读写文件，文件必须用全路径；
    备注：
    1、定时器不起作用时，应检查文件 mysite/app/statefile.txt是否存在,若存在就该删除！
    2、数据库数据更新后，不能立即生效，视定时时间而定；
    """
    import os
    from .adminx import OBJECT_TEMPLATE    
    from myAPI.fileAPI import read_txt, write_txt
    from mysite.settings import BASE_DIR
        
    STATEFILE = os.path.join(BASE_DIR, 'app', 'statefile.txt') # 状态文件
    c = mode.objects.all().count()
    items = sum(mode.objects.values_list(field, flat=True))//c if c else 0 
    
    
    if not os.path.isfile(STATEFILE):
       
        with open(STATEFILE,'w+') as f:
            f.write('0')
                   
        template_file = os.path.join(BASE_DIR, \
            'xadmin/templates/my-define/dashboard_template.html').replace('\\','/')
        new_template_file = os.path.join(BASE_DIR, \
            'xadmin/templates', OBJECT_TEMPLATE).replace('\\','/')
    
        text = read_txt(template_file)        
        text = text.replace('disk_total_json',label)
        text = text.replace('disk_val',str(items))

        write_txt(new_template_file, text)
        
        if os.path.isfile(STATEFILE): #判断文件
            os.remove(STATEFILE) 
        
        #  print('ok') print在此不起作用的   
    