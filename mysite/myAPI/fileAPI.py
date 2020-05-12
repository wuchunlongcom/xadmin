# -*- coding: utf-8 -*-
import os
import datetime
#from .listdictAPI import  listdictAPI

imgExt = ['.bmp', '.gif', '.jpg', '.pic', '.png', '.tif', '.jpeg', '.php',\
          '.BMP', '.GIF', '.JPG', '.PIC', '.PNG', '.TIF', '.JPEG', '.PHP']


# html可以直接下载的文件类型
ExtDown = ['.zip', '.doc','.docx','.xls','.xlsx', '.rmvb', '.wmv']
   
# html可以直接打开浏览、播放的文件类型
ExtOpen = ['.txt', '.mp4','.pdf']
ExtOpen.append(imgExt)

class MyFile:
    """
        from myAPI.fileAPI import MyFile
        myfile = MyFile('blog/static/img/', ['.jpg'])
        imgs = myfile.toNameList()    
    """
    def __init__(self, dirpath, extlist):#extlist ＝［］获得指定目录下,全部目录名、文件名
        self.dirPath = dirpath # 目录路径 dirpath = '.../edustack/upvideo/testMyFile'
        self.extList = extlist # 指定类型的文件名列表extlist = ［'.txt'］获得全部扩展名为.txt文件名
        
    # 以列表形式，获得指定目录下，指定类型的全部文件名。extlist ＝［］获得指定目录下,全部目录名、文件名.    
    def toNameList(self):
        try:
            # 列表形式，返回指定目录下所有的文件和目录名（不含路径的短文件名）
            fileNames = os.listdir(self.dirPath)       
        except Exception as ex:
            """
            print(any([''])) # False
            print(any(['1'])) #True
            """
            print('Error execute: {}'.format(ex))
            # raise
            return ['']  # L1 = []与 L2 = [''] 区别：L1[0] 出错；L2[0] 不出错 2018.10.28    
        if (len(self.extList) > 0):
             fileNames = [fileName for fileName in fileNames 
                         if listdictAPI(self.extList, fileName).isListInStr()]
        filepathList = [os.path.join(self.dirPath, i) for i in fileNames 
                    if (not '._' in i)&(not '.DS' in i)] #（含路径的文件名）2016.10.24
        if filepathList == []:
            filepathList = ['']            
        return filepathList


def readtxt_to_list(filename):
    """
        功能：读文本文件（抛弃空行，删除左边空格），返回列表    
    """
    try:
        with open(filename,'r') as f:
            lines = f.readlines()
            return [l  for l in lines if l.strip()] # 抛弃空行 
    except Exception as ex:
        #print('err: %s' %ex)
        return ['']
        
def read_txt(filename):
    """
    功能：读文本文件（抛弃空行），返回字符串
    BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    template_file = os.path.join(BASE_DIR, \
            'xadmin/templates/my-define/dashboard_template.html').replace('\\','/')
    text = read_txt(template_file)    
    print(text)
    ('{% extends \'xadmin/base_site.html\' %}\n{% load i18n %}\n{% block content %}\n  <div class="col-md-1 content-toolbar btn-toolbar pull-right clearfix">    \n    <div class="btn-group layout-btns" data-toggle="buttons-checkbox">\n      <button type="button" class="btn btn-default btn-sm layout-full">\n      <i class="fa fa-expand"></i></button>      \n    </div>    \n  </div>\n    <div class="col-md-6 column">  \n        <div>\xe6\x9c\x80\xe6\x96\xb0\xe4\xb8\x80\xe5\x91\xa8\xe6\x96\xb0\xe5\xa2\x9e\xe7\x94\xa8\xe6\x88\xb7</div>\n        <div style="min-height: 280px;">\n          <div id="main1"  style="height: 300px;"></div>\n        </div>\n    </div>\n    <div class="col-md-5 column">\n        <div>\xe6\x9c\x80\xe6\x96\xb0\xe4\xb8\x80\xe5\x91\xa8PV/UV\xe9\x87\x8f</div>\n        <div style="min-height: 280px;">\n          <div id="main2"  style="height: 300px;"></div>\n        </div>\n    </div>\n    <div class="col-md-6 column">\n        <div>\xe7\x94\xa8\xe6\x88\xb7\xe6\x9d\xa5\xe6\xba\x90</div>\n        <div style="min-height: 280px;">\n          <div id="main3" style="height: 300px;"></div>\n        </div>\n    </div>\n    <div class="col-md-6 column">\n        <div>{{ \'disk_total_json\' }}</div>\n        <div style="min-height: 280px;">\n          <div id="main4" style="height: 300px;"></div>\n        </div>\n    </div>\n    <script src="https://cdn.bootcss.com/echarts/4.2.1-rc1/echarts.min.js"></script>\n    <script type="text/javascript">\n        // \xe5\x9f\xba\xe4\xba\x8e\xe5\x87\x86\xe5\xa4\x87\xe5\xa5\xbd\xe7\x9a\x84dom\xef\xbc\x8c\xe5\x88\x9d\xe5\xa7\x8b\xe5\x8c\x96echarts\xe5\xae\x9e\xe4\xbe\x8b\n        var myChart = echarts.init(document.getElementById(\'main1\'));\n        // \xe6\x8c\x87\xe5\xae\x9a\xe5\x9b\xbe\xe8\xa1\xa8\xe7\x9a\x84\xe9\x85\x8d\xe7\xbd\xae\xe9\xa1\xb9\xe5\x92\x8c\xe6\x95\xb0\xe6\x8d\xae\n        var option = {\n            grid: {\n                top: \'5%\',\n                right: \'1%\',\n                left: \'1%\',\n                bottom: \'10%\',\n                containLabel: true\n            },\n            tooltip: {\n                trigger: \'axis\'\n            },\n            xAxis: {\n                type: \'category\',\n                data: [\'\xe5\x91\xa8\xe4\xb8\x80\',\'\xe5\x91\xa8\xe4\xba\x8c\',\'\xe5\x91\xa8\xe4\xb8\x89\',\'\xe5\x91\xa8\xe5\x9b\x9b\',\'\xe5\x91\xa8\xe4\xba\x94\',\'\xe5\x91\xa8\xe5\x85\xad\',\'\xe5\x91\xa8\xe6\x97\xa5\']\n            },\n            yAxis: {\n                type: \'value\'\n            },\n            series: [{\n                name:\'\xe7\x94\xa8\xe6\x88\xb7\xe9\x87\x8f\',\n                data: [820, 932, 901, 934, 1290, 1330, 1320],\n                type: \'line\',\n                smooth: true\n            }]\n        };\n        // \xe4\xbd\xbf\xe7\x94\xa8\xe5\x88\x9a\xe6\x8c\x87\xe5\xae\x9a\xe7\x9a\x84\xe9\x85\x8d\xe7\xbd\xae\xe9\xa1\xb9\xe5\x92\x8c\xe6\x95\xb0\xe6\x8d\xae\xe6\x98\xbe\xe7\xa4\xba\xe5\x9b\xbe\xe8\xa1\xa8\xe3\x80\x82\n        myChart.setOption(option);\n        // \xe5\x9f\xba\xe4\xba\x8e\xe5\x87\x86\xe5\xa4\x87\xe5\xa5\xbd\xe7\x9a\x84dom\xef\xbc\x8c\xe5\x88\x9d\xe5\xa7\x8b\xe5\x8c\x96echarts\xe5\xae\x9e\xe4\xbe\x8b\n        var myChart = echarts.init(document.getElementById(\'main2\'));\n        // \xe6\x8c\x87\xe5\xae\x9a\xe5\x9b\xbe\xe8\xa1\xa8\xe7\x9a\x84\xe9\x85\x8d\xe7\xbd\xae\xe9\xa1\xb9\xe5\x92\x8c\xe6\x95\xb0\xe6\x8d\xae\n        var option = {\n            tooltip : {\n                trigger: \'axis\',\n                axisPointer: {\n                    type: \'cross\',\n                    label: {\n                        backgroundColor: \'#6a7985\'\n                    }\n                }\n            },\n            grid: {\n                top: \'5%\',\n                right: \'2%\',\n                left: \'1%\',\n                bottom: \'10%\',\n                containLabel: true\n            },\n            xAxis : [\n                {\n                    type : \'category\',\n                    boundaryGap : false,\n                    data : [\'\xe5\x91\xa8\xe4\xb8\x80\',\'\xe5\x91\xa8\xe4\xba\x8c\',\'\xe5\x91\xa8\xe4\xb8\x89\',\'\xe5\x91\xa8\xe5\x9b\x9b\',\'\xe5\x91\xa8\xe4\xba\x94\',\'\xe5\x91\xa8\xe5\x85\xad\',\'\xe5\x91\xa8\xe6\x97\xa5\']\n                }\n            ],\n            yAxis : [\n                {\n                    type : \'value\'\n                }\n            ],\n            series : [\n                {\n                    name:\'PV\',\n                    type:\'line\',\n                    areaStyle: {normal: {}},\n                    data:[120, 132, 101, 134, 90, 230, 210],\n                    smooth: true\n                },\n                {\n                    name:\'UV\',\n                    type:\'line\',\n                    areaStyle: {normal: {}},\n                    data:[45, 182, 191, 234, 290, 330, 310],\n                    smooth: true,\n                }\n            ]\n        };\n        // \xe4\xbd\xbf\xe7\x94\xa8\xe5\x88\x9a\xe6\x8c\x87\xe5\xae\x9a\xe7\x9a\x84\xe9\x85\x8d\xe7\xbd\xae\xe9\xa1\xb9\xe5\x92\x8c\xe6\x95\xb0\xe6\x8d\xae\xe6\x98\xbe\xe7\xa4\xba\xe5\x9b\xbe\xe8\xa1\xa8\xe3\x80\x82\n        myChart.setOption(option);\n        // \xe5\x9f\xba\xe4\xba\x8e\xe5\x87\x86\xe5\xa4\x87\xe5\xa5\xbd\xe7\x9a\x84dom\xef\xbc\x8c\xe5\x88\x9d\xe5\xa7\x8b\xe5\x8c\x96echarts\xe5\xae\x9e\xe4\xbe\x8b\n        var myChart = echarts.init(document.getElementById(\'main3\'));\n        // \xe6\x8c\x87\xe5\xae\x9a\xe5\x9b\xbe\xe8\xa1\xa8\xe7\x9a\x84\xe9\x85\x8d\xe7\xbd\xae\xe9\xa1\xb9\xe5\x92\x8c\xe6\x95\xb0\xe6\x8d\xae\n        var option = {\n            tooltip : {\n                trigger: \'item\',\n                formatter: "{a} <br/>{b} : {c} ({d}%)"\n            },\n            legend: {\n                orient: \'vertical\',\n                left: \'left\',\n                data: [\'\xe7\x9b\xb4\xe6\x8e\xa5\xe8\xae\xbf\xe9\x97\xae\',\'\xe9\x82\xae\xe4\xbb\xb6\xe8\x90\xa5\xe9\x94\x80\',\'\xe8\x81\x94\xe7\x9b\x9f\xe5\xb9\xbf\xe5\x91\x8a\',\'\xe8\xa7\x86\xe9\xa2\x91\xe5\xb9\xbf\xe5\x91\x8a\',\'\xe6\x90\x9c\xe7\xb4\xa2\xe5\xbc\x95\xe6\x93\x8e\']\n            },\n            series : [\n                {\n                    name: \'\xe8\xae\xbf\xe9\x97\xae\xe6\x9d\xa5\xe6\xba\x90\',\n                    type: \'pie\',\n                    radius : \'55%\',\n                    center: [\'50%\', \'60%\'],\n                    data:[\n                        {value:335, name:\'\xe7\x9b\xb4\xe6\x8e\xa5\xe8\xae\xbf\xe9\x97\xae\'},\n                        {value:310, name:\'\xe9\x82\xae\xe4\xbb\xb6\xe8\x90\xa5\xe9\x94\x80\'},\n                        {value:234, name:\'\xe8\x81\x94\xe7\x9b\x9f\xe5\xb9\xbf\xe5\x91\x8a\'},\n                        {value:135, name:\'\xe8\xa7\x86\xe9\xa2\x91\xe5\xb9\xbf\xe5\x91\x8a\'},\n                        {value:1548, name:\'\xe6\x90\x9c\xe7\xb4\xa2\xe5\xbc\x95\xe6\x93\x8e\'}\n                    ],\n                    itemStyle: {\n                        emphasis: {\n                            shadowBlur: 10,\n                            shadowOffsetX: 0,\n                            shadowColor: \'rgba(0, 0, 0, 0.5)\'\n                        }\n                    }\n                }\n            ]\n        };\n        //var disk_usage = {{ disk_usage|safe }};\n        //var \xe7\xa1\xac\xe7\x9b\x98\xe4\xbd\xbf\xe7\x94\xa8\xe6\x83\x85\xe5\x86\xb5 = {{ \xe7\xa1\xac\xe7\x9b\x98\xe4\xbd\xbf\xe7\x94\xa8\xe6\x83\x85\xe5\x86\xb5|safe }}\n        // \xe4\xbd\xbf\xe7\x94\xa8\xe5\x88\x9a\xe6\x8c\x87\xe5\xae\x9a\xe7\x9a\x84\xe9\x85\x8d\xe7\xbd\xae\xe9\xa1\xb9\xe5\x92\x8c\xe6\x95\xb0\xe6\x8d\xae\xe6\x98\xbe\xe7\xa4\xba\xe5\x9b\xbe\xe8\xa1\xa8\xe3\x80\x82\n        myChart.setOption(option);\n         // \xe5\x9f\xba\xe4\xba\x8e\xe5\x87\x86\xe5\xa4\x87\xe5\xa5\xbd\xe7\x9a\x84dom\xef\xbc\x8c\xe5\x88\x9d\xe5\xa7\x8b\xe5\x8c\x96echarts\xe5\xae\x9e\xe4\xbe\x8b\n        var myChart = echarts.init(document.getElementById(\'main4\'));\n        // \xe6\x8c\x87\xe5\xae\x9a\xe5\x9b\xbe\xe8\xa1\xa8\xe7\x9a\x84\xe9\x85\x8d\xe7\xbd\xae\xe9\xa1\xb9\xe5\x92\x8c\xe6\x95\xb0\xe6\x8d\xae\n        var option = {\n            tooltip : {\n                formatter: "{a} <br/>{b} : {c}%"\n            },\n            series: [\n                {\n                    name: \'disk_total_json\',\n                    type: \'gauge\',\n                    detail: {formatter:\'{value}%\'},\n                    data: [{value: \'disk_val\', name: \'\xe5\xb7\xb2\xe4\xbd\xbf\xe7\x94\xa8\'}]\n                }\n            ]\n        };\n        // \xe4\xbd\xbf\xe7\x94\xa8\xe5\x88\x9a\xe6\x8c\x87\xe5\xae\x9a\xe7\x9a\x84\xe9\x85\x8d\xe7\xbd\xae\xe9\xa1\xb9\xe5\x92\x8c\xe6\x95\xb0\xe6\x8d\xae\xe6\x98\xbe\xe7\xa4\xba\xe5\x9b\xbe\xe8\xa1\xa8\xe3\x80\x82\n        myChart.setOption(option);\n    </script>\n{% endblock %}\n')
        
    """
    return ''.join(readtxt_to_list(filename))


def write_txt(filename, txt): 
    """
    功能：保存文本文件，适用于小文本文件
    w+ 打开一个文件用于读写。如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件。
    """   
    ret = False
    with open(filename,'w+') as f:
        f.write(txt)
        ret = True
    return ret




def upfile_save(mode, filepath):
    """
        保存上传文件：上传文件同名会覆盖
    """
    filename = os.path.join(filepath, mode.name)
    return savefile(mode, filename)

def upfile_save_2(upfile, filename1, filename2):
    """
        为了确保本地运行和部署后都能显示图像文件，上传文件到两个目录        
    """
    res1 = upfile_save(upfile, filename1) # 保存上传文件，供部署后，显示图像文件
    res2 = upfile_save(upfile, filename2) # 保存上传文件，供本地运行时，显示图像文件         
    return '%s. %s'%(res1,res2)

def upfile_save_time(mode, filepath):
    """
        保存上传文件：上传文件名添加当前时间，上传文件不会覆盖
    """
    name, etx = os.path.splitext(mode.name)
    filename = '%s-%s%s' %(name, datetime.datetime.now().strftime('%Y%m%d[%H:%M:%S]'), etx)  
    filename = os.path.join(filepath, filename)
    return savefile(mode, filename)
    
def savefile(mode, filename):    
    try:
        f = open(filename, 'wb+')  # 打开特定的文件进行二进制的写操作
        for chunk in mode.chunks():  # 分块写入文件  
            f.write(chunk)      
    except Exception as ex:
        return str(ex)    
    f.close() 
    return 'UpFile: %s. add nowTime. UpFile Success!' %(filename)  
    
def file_iterator(file_name, chunk_size=512):
    try:
        with open(file_name, 'rb') as f:   #python3   'rb'读二进制文件
            while True:
                c = f.read(chunk_size)
                if c: 
                    yield c                   
                else: 
                    break #return  okokok   
    except Exception as ex:
        yield ''      