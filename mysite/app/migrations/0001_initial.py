# Generated by Django 2.2.6 on 2020-03-04 15:52

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccessRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='日期')),
                ('user_count', models.IntegerField(verbose_name='用户数量')),
                ('view_count', models.IntegerField(verbose_name='查看数量')),
            ],
            options={
                'verbose_name': '访问记录 图表',
                'verbose_name_plural': '访问记录 图表',
            },
        ),
        migrations.CreateModel(
            name='CustomPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': '自定义页面',
                'verbose_name_plural': '自定义页面',
            },
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Host名称')),
                ('nagios_name', models.CharField(blank=True, max_length=64, null=True, verbose_name='Nagios Host ID')),
                ('ip', models.GenericIPAddressField(blank=True, null=True, verbose_name='ip')),
                ('internal_ip', models.GenericIPAddressField(blank=True, null=True, verbose_name='内部ip')),
                ('user', models.CharField(max_length=64, verbose_name='用户')),
                ('password', models.CharField(max_length=128, verbose_name='密码')),
                ('ssh_port', models.IntegerField(blank=True, null=True, verbose_name='ssh_port')),
                ('status', models.SmallIntegerField(choices=[(0, 'Normal'), (1, 'Down'), (2, 'No Connect'), (3, 'Error')], default=0, verbose_name='状态')),
                ('brand', models.CharField(choices=[('DELL', 'DELL'), ('HP', 'HP'), ('Other', 'Other')], max_length=64, verbose_name='品牌')),
                ('model', models.CharField(choices=[('台式机', '台式机'), ('笔记本', '笔记本'), ('其他', '其他')], max_length=64, verbose_name='样式')),
                ('cpu', models.CharField(choices=[('586', '586'), ('686', '686')], max_length=64, verbose_name='CPU')),
                ('core_num', models.SmallIntegerField(blank=True, choices=[(2, '2 Cores'), (4, '4 Cores'), (6, '6 Cores'), (8, '8 Cores'), (10, '10 Cores'), (12, '12 Cores'), (14, '14 Cores'), (16, '16 Cores'), (18, '18 Cores'), (20, '20 Cores'), (22, '22 Cores'), (24, '24 Cores'), (26, '26 Cores'), (28, '28 Cores')], null=True, verbose_name='CoreNum')),
                ('hard_disk', models.IntegerField(blank=True, null=True, verbose_name='硬盘')),
                ('memory', models.IntegerField(blank=True, null=True, verbose_name='内存')),
                ('system', models.CharField(choices=[('CentOS', 'CentOS'), ('FreeBSD', 'FreeBSD'), ('Ubuntu', 'Ubuntu')], max_length=32, verbose_name='System OS')),
                ('system_version', models.CharField(choices=[('1.00', '1.00'), ('2.10', '2.10'), ('3.3.8', '3.3.8')], max_length=32)),
                ('system_arch', models.CharField(choices=[('x86_64', 'x86_64'), ('i386', 'i386')], max_length=32)),
                ('create_time', models.DateField(auto_now=True, verbose_name='创建日期')),
                ('guarantee_date', models.DateField(auto_now=True, verbose_name='担保日期')),
                ('service_type', models.CharField(choices=[('moniter', 'Moniter'), ('lvs', 'LVS'), ('db', 'Database'), ('analysis', 'Analysis'), ('admin', 'Admin'), ('storge', 'Storge'), ('web', 'WEB'), ('email', 'Email'), ('mix', 'Mix')], default='moniter', max_length=32, verbose_name='服务类型')),
                ('description', models.TextField(verbose_name='描述')),
                ('administrator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Admin')),
            ],
            options={
                'verbose_name': 'Host 柱状图 表',
                'verbose_name_plural': 'Host 柱状图 表',
            },
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='学校名字')),
                ('address', models.CharField(max_length=100, verbose_name='学校地址')),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name='添加时间')),
                ('num', models.IntegerField(blank=True, null=True, verbose_name='建校时间')),
                ('per', models.IntegerField(blank=True, null=True, verbose_name='高考升学率')),
            ],
            options={
                'verbose_name': '学校',
                'verbose_name_plural': '学校',
            },
        ),
        migrations.CreateModel(
            name='Threshold',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('per', models.IntegerField(default=50, verbose_name='阀值')),
            ],
            options={
                'verbose_name': '阀值',
                'verbose_name_plural': '阀值',
            },
        ),
        migrations.CreateModel(
            name='MaintainLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maintain_type', models.CharField(max_length=32, verbose_name='维护类型')),
                ('hard_type', models.CharField(max_length=16, verbose_name='难度类型')),
                ('time', models.DateTimeField(default=datetime.datetime.now)),
                ('operator', models.CharField(max_length=16, verbose_name='操作人员')),
                ('note', models.TextField(default='备注:说点什么', verbose_name='备注')),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Host')),
            ],
            options={
                'verbose_name': '维护日志 列表',
                'verbose_name_plural': '维护日志 列表',
            },
        ),
        migrations.CreateModel(
            name='IDC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='IDC名称')),
                ('description', models.TextField(verbose_name='描述')),
                ('contact', models.CharField(max_length=32, verbose_name='联系人')),
                ('telphone', models.CharField(max_length=32, verbose_name='电话')),
                ('address', models.CharField(max_length=128, verbose_name='地址')),
                ('customer_id', models.CharField(max_length=128, verbose_name='客户')),
                ('create_time', models.DateField(auto_now=True, verbose_name='创建日期')),
                ('groups', models.ManyToManyField(to='auth.Group')),
            ],
            options={
                'verbose_name': 'IDC 列表',
                'verbose_name_plural': 'IDC 列表',
            },
        ),
        migrations.CreateModel(
            name='HostGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='名称')),
                ('description', models.TextField(verbose_name='描述')),
                ('hosts', models.ManyToManyField(blank=True, related_name='groups', to='app.Host', verbose_name='Hosts')),
            ],
            options={
                'verbose_name': 'Host Group 列表',
                'verbose_name_plural': 'Host Group 列表',
            },
        ),
        migrations.AddField(
            model_name='host',
            name='idc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.IDC', verbose_name='IDC'),
        ),
    ]
