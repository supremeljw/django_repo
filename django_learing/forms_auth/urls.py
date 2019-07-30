
from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^$', views.index, {"template_name": "forms_auth/index.html"}, name='index'),
]

