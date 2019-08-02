
from django.conf.urls import url,include
from django.contrib import admin
from django.conf.urls import handler404, handler500
from django_views import views
from django.views.static import serve
import re
from . import settings
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'',include('model_define.urls',namespace="django_views")),
    # 自己添加规则来处理静态文件
    # url(r'^%s(?P<path>.*)$' % re.escape(settings.STATIC_URL.lstrip('/')), serve,{"document_root": settings.STATIC_ROOT}),
    url(r'^%s(?P<path>.*)$' % re.escape(settings.MEDIA_URL.lstrip('/')), serve,{"document_root": settings.MEDIA_ROOT}),
]

handler404=views.error_404
