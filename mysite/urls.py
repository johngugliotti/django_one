from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    #   Pattern.......INCLUDE.............NAMESPACE (namespace allows us to avoid hard-coding urls and polls:details and reports:details can easily point to different detail views in different apps
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^$', include("polls.urls",namespace="polls")),
    #set the defaul resolution to polls.urls -- > which then points to url(r'^$', views.index, name='index') the index
    url(r'^$', include('polls.urls', namespace="polls")), 

)
