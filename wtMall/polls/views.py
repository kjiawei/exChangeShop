from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import Question
#视图可以从数据库中读取记录，或者不读取数据库。 你还可以动态地生成一个PDF文件、输出XML文件、创建一个ZIP文件或者使用你想用的Python 库生成任何想要的形式

def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	template = loader.get_template('polls/index.html')
	context = RequestContext(request, {
		'latest_question_list': latest_question_list,
	})
	return HttpResponse(template.render(context))

def detail(request, question_id):
	return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
	response = "You're looking at the results of question %s."
	return HttpResponse(response % question_id)

def vote(request, question_id):
	return HttpResponse("You're voting on question %s." % question_id)