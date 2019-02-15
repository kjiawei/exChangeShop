## 项目说明
本项目是python的电商网站,基于python3 django1.11.7,需求在上级目录电商网站里的图片
定位:生鲜品类电子商务网站
username:admin  password:kjw123456  (设置的密码保存到哪)

### 开发进度  11.15看到第3部分新手教程出错了
1.掌握python基础
2.熟悉django使用和pycharm的使用   pycharm如何新建django项目
3.架构参考 https://www.cnblogs.com/luodengxiong/p/5212120.html


常见错误
1.indent 需要将所有空格转tab

### 开发笔记   看到  https://yiyibooks.cn/xx/django_182/intro/tutorial01.html
0.开发环境搭建    视频教程 (vi的设置挺好看 )https://ke.qq.com/user/index/index.html#cid=224798&tid=100265413&fr=2&term_id=100265413
极客学院http://www.jikexueyuan.com/course/1325_1.html?ss=1
其余python项目列表 http://www.ibeifeng.cn/page/job_python.html?hmsr=cn-bdss&hmmd=cpc&hmpl=pb318-python&hmcu=mk001-python&hmkw=53805877704_django%E8%A7%86%E9%A2%91%E6%95%99%E7%A8%8B&hmci=13609129865&matchtype=1&adposition=cl5&pagenum=1&matchtype=1&adposition=cl5&pagenum=1&e_keywordid=53805877704#python-prg

- import django
- print(django.get_version())
查看Django版本号

1.D:\Share\python\helloworld  练习项目 合并
2.如何引导和挖掘客户的需求
3.出错点即刻记录来源位置  
(修改INSTALLED_APPS后更新及修改数据表python manage.py makemigrations polls ; [python manage.py sqlmigrate polls 0001;] py -3 manage.py migrate;) 解决python2共存创建数据表问题
4.编写一个数据库驱动的Web应用时，第一步就是定义该应用的模型 —— 本质上，就是定义该模型所对应的数据库设计及其附带的元数据
5.模型更新 python manage.py makemigrations polls
6.PostgreSQL优势https://www.zhihu.com/question/20010554

7.更改setting时区会出现 if zone.upper()=='UTC'  nonetype object has no attribute 'upper'
8.url视图路径出错  https://www.cnblogs.com/way_testlife/archive/2011/03/22/1991453.html  解决了
### 文件说明
manage.py：一个命令行工具，可以使你用多种方式对Django项目进行交互。 你可以在django-admin和manage.py中读到关于manage.py的所有细节。
内层的mysite/目录是你的项目的真正的Python包。它是你导入任何东西时将需要使用的Python包的名字（例如 mysite.urls）。
mysite/__init__.py：一个空文件，它告诉Python这个目录应该被看做一个Python包。 （如果你是一个Python初学者，关于包的更多内容请阅读Python的官方文档）。
mysite/settings.py：该Django 项目的设置/配置。Django 设置 将告诉你这些设置如何工作。
mysite/urls.py：该Django项目的URL声明；你的Django站点的“目录”。 你可以在URL 转发器 中阅读到更多关于URL的内容。
mysite/wsgi.py：用于你的项目的与WSGI兼容的Web服务器入口;

### 需求模块(下列为补充)
1.打分，评价系统；
2.目前有成熟的进销存系统；需要与网站对接；
3.特惠活动模块(限时抢购 倒计时等);
4.拓展/模块化