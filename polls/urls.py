from django.conf.urls import url

from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    # ex: /polls/prive/
    url(r'^prive/$', views.prive, name='prive'),
    # ex: /polls/upload/
    url(r'^upload/$', views.upload, name='upload'),
]