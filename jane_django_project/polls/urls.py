
from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns(
    'polls.views',
    url(r'^tasks$', views.TaskList.as_view()),
    url(r'^tasks/(?P<question_id>[0-9]+)/$', 'task_detail',name='task_detail'),
    url(r'^$', views.index,name='index'),
    url(r'^(?P<question_id>[0-9]+)/$', views.detail,name='detail'),
    url(r'^(?P<question_id>[0-9]+)/results$', views.results,name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote$', views.vote,name='vote'),
)