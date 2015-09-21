from django.conf.urls import patterns, include, url
from django.contrib import admin
from mysite.views import mainpage, bob, register, profpage, edit_profile, find_match
import mysite.views as views

urlpatterns = patterns('',
	url(r'^main/$', mainpage),
	url(r'^login/$', 'django.contrib.auth.views.login'),
	url(r'^logout/$', 'django.contrib.auth.views.logout'),
    url(r'^profile/bob/$', bob),
    url(r'^profile/$', profpage, name = 'profilepage'),
    #url(r'^profile/(?P<username>\w{0,50})/$', profpage),
    url(r'^register/$', views.register, name = 'register'),
    url(r'^profile/edit/$', edit_profile),
    url(r'^findmatch/$', find_match,)

)
#views.CreateRegistration