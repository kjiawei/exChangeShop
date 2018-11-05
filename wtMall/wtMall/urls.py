from django.conf.urls import include,url
from django.contrib import admin 
from wtMall.views import hello
#from . import view
#from views import polls
 
urlpatterns = [
	url(r'^polls/', include('polls.urls')),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^hello/',hello),
]
