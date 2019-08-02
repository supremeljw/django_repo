from django.conf.urls import url
from . import views
urlpatterns=[
    url(r'^$',views.IndexView.as_view(),name='index'),
    url(r'^test/$',views.test,name='test'),
    url(r'^dv/(?P<user_id>\d+)/$',views.myDetailView.as_view(),name='myDetailView')
]