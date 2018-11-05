import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):  #这是一个模型
	question_text = models.CharField(max_length=200)  #类变量(字段名字) 每个都代表数据库中一个字段 Python代码中使用到它的值,并且你的数据库将把它用作表的列名
	#每个字段通过Field类的一个实例表示 告诉Django，每个字段中保存着什么类型的数据
	
	#__str__方法使你自己在使用交互式命令行时看得更加方便,而且会在Django自动生成的管理界面中使用对象的这种表示
	
	pub_date = models.DateTimeField('date published')

	def __str__(self):				
		return self.question_text
		
	def was_published_recently(self):
		now = timezone.now()
		return now - datetime.timedelta(days=1) <= self.pub_date <= now
		#return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
	was_published_recently.admin_order_field = 'pub_date'
	was_published_recently.boolean = True
	was_published_recently.short_description = 'Published recently?'
	
class Choice(models.Model):
	question = models.ForeignKey(Question,on_delete=models.CASCADE) #ForeignKey定义了一个关联。它告诉Django每个Choice都只关联一个Question。Django支持所有常见的数据库关联：多对一、多对多和一对一
	#看回源代码 django 1.8.2教程   pip install Django --upgrade可以升级django项目  大版本的升级会有兼容性问题，Django 新版本会弃用掉一个函数，建议先在本地测试，测试 ok 再部署到生产环境
    choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)
	
	def __str__(self):
		return self.choice_text