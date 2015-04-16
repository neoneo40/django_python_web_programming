from django.conf.urls import patterns, include, url

from django.contrib import admin
from mysite import views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.HomeView.as_view(), name='home'), # Add
    url(r'^polls/', include('polls.urls', namespace='polls')),
    url(r'^books/', include('books.urls', namespace='books')),
    url(r'^admin/', include(admin.site.urls)),
)