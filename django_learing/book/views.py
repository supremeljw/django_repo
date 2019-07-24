from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
from book.models import UserInfo


def index(request):
    email = request.GET.get("email")
    pwd = request.GET.get('pwd')
    msg=''
    try:
        userInfo=UserInfo.objects.get(email=email)
        if userInfo and userInfo.password==pwd:
            return HttpResponse(f"<h1>欢迎您，{email}</h1>")
        else:
            msg="用户名或密码错误"
    except:
        msg="用户名不存在"
    kwgs={
        "msg":msg,
    }
    return render(request, "book/index_form.html",kwgs)


def index_form(request):
    return render(request, "book/index.html")
