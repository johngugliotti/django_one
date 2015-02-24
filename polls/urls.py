from django.conf.urls import patterns, url

from polls import views

"""
urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)
"""

urlpatterns = patterns('',
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<question_id>\d+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    # strips off the /polls/ part, sets question_id = 5 calls views.results  
    url(r'^(?P<question_id>\d+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),
)


