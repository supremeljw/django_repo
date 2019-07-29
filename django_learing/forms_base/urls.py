
from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^index/$',views.index,name='index'),
    url('^reg/$', views.register, name='register'),
    url('^login/$', views.login, name='login'),
    url('^logout/$', views.logout, name='logout'),
]
