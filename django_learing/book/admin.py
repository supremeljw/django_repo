from django.contrib import admin

# Register your models here.
from book.models import UserInfo

admin.site.register(UserInfo)