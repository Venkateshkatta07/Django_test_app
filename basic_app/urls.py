
from django.urls import path
from django.conf.urls import url
from basic_app import views

app_name='basic_app'

urlpatterns = [
    url(r'^register/$',views.register, name='register'),
    url(r'^login/$',views.user_login,name='login'),
    url(r'^logout/$',views.user_logout,name='logout'),
    url(r'^special/',views.special,name='special')
]