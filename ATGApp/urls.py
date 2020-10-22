# This is the urls module for the ATGApp Application
from django.conf.urls import url
from ATGApp import views

urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^stadiums/$', views.stadiums, name='stadiums'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^account/$', views.account, name='account'),
    url(r'^like/$', views.like_category, name='like_category'),
    url(r'^add_stadium/$', views.add_stadium,name='add_stadium'),
    url(r'^chosenStadium/(?P<stadium_name_slug>[\w\-]+)/$',views.chosenStadium, name='chosenStadium'),
    url(r'^writeReview/(?P<stadium_name_slug>[\w\-]+)/$',views.writeReview, name='writeReview'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^del_acc/$', views.del_acc, name='del_acc'),
]
