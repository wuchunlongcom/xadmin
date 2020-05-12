# xadmin  部署正常  
python 版本: 3.7.5  django版本: 2.2.6  xadmin2.0.0


## xadmin修改BUG记录
```

一、解决注销界面关不掉问题 2019.12.20
二、认证和权限。用户中修改组为穿梭框。2019.12.25
三、增加按钮和自定义页面。2019.12.28
四、解决登录慢问题 2019.12.30
五、数据导入（.csv,导入导入英文正常，导入中文出错）、导出，解决csv导出中文乱码问题 2019.12.31
六、图标升级显示  2020.01.03
七、删除记录同时删除上传的文件 2020.03.01
八、自定义页添加缩放按钮
九、自定义页添加Echarts数据可视化，仪表盘模板，采用定时执行任务实现。此种方法缺点是明显的，1、数据库数据更新后，不能立即生效，视定时时间而定；
十、自定义菜单、支持使用模板变量、支持Echarts数据可视化。存在两个问题：1、有一空白行；2、缩放按钮不起作用。2020.03.05
十一、自定义页，支持使用模板变量(实现后台给前端传值)、支持Echarts数据可视化。  支持缩放按钮 2020.03.29
十二、去掉空白行
dashboard_school.html
<!--添加下列语句， 去掉空白行 -->
{% block content-nav %} {% endblock %} 
十三、 xadmin登录。 忘记了您的密码或用户名？ 2020.05.10
修复： xadmin邮件重置密码报错问题,功能正常；
问题原因：django2.1以后， xadmin/plugins/passwords.py 取消了(password_reset_confirm) from django.contrib.auth.views import password_reset_confirm
解决：1、增加文件 xadmin/plugins/password_reset.py
     2、xadmin/plugins/passwords.py 
       #from django.contrib.auth.views import password_reset_confirm # 注释掉
       from .password_reset import password_reset_confirm # 增加

十四、导入、导出数据；全面支持下列格式文件：  2020.05.12
导入数据: xls、xlsl、csv、tsv、 yaml、json
导出数据：xls、xlsl、csv、tsv、 yaml、json、ods、 html 



```
xadmin 功能测试


### 使用 xadmin
```
- 您只需定义您数据的字段等信息，即可即刻获得一个功能全面的管理系统。不仅如此，您还可以方便的扩展更多的定制功能和系统界面。
- 使用系统用户模型 from django.contrib.auth.models import User

```

删除定时任务
python3 mysite/manage.py crontab remove   # python3


## 功能

- 更好的过滤器，日期范围，数量范围等。

- 基于Bootstrap3，支持在多种屏幕上无缝浏览，并支持Bootstrap主题模板

- 内置丰富的插件功能。包括数据导出、书签、图表、数据添加向导及图片相册等多种扩展功能

- 插件开发简单，安装方便。

## 源码下载
- https://github.com/sshwsfc/xadmin
  
## 文档
- [Chinese](https://xadmin.readthedocs.org/en/latest/index.html)


## 在本地运行Demo

```
./start.sh -i
```

http://127.0.0.1:8000

在浏览器中打开 [http://127.0.0.1:8000](http://127.0.0.1:8000/) ，管理员用户密码为admin/admin。

### 问题日记
存在问题： 2020.05.08
python3.7.5 django==2.2.6   
xadmin邮件重置密码，报错
https://tieba.baidu.com/p/6420994580?traceid=

python3.6.6 django==2.0  
xadmin邮件重置密码正常
1、初始化编程实现组添加权限，报错！
2、自定义页面，定时执行任务，异常！

待解决的问题：
python3.7.5 django==2.2.6    
xadmin邮件重置密码，报错问题；问题已经解决

