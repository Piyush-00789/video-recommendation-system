#from django.contrib import admin
from . import views
from django.conf.urls import url

app_name = "video"

urlpatterns = [

    #video
    url(r'^$', views.Indexview.as_view(), name='index'),
    #video/signin
    url(r'signin/$',views.signin,name='sign-in'),

    url(r'usertaste/$',views.CreateUserTaste.as_view(),name='user-taste'),


    url(r'userlogincheck/$',views.logincheck,name="login-check"),

    url(r'signup/add',views.UserFormView.as_view(),name='register'),
]
