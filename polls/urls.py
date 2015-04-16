from django.conf.urls import patterns, url
from polls import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'), # /polls/
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'), #/polls/5/
    url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'), # /polls/5/vote/
)