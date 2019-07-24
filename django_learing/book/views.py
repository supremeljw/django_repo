from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    userlist = {'ljw@qq.com':"123456","liu@qq.com":'1122'}
    email = request.POST.get("email")
    pwd = request.POST.get('pwd')
    if email in userlist.keys() and userlist.get(email)==pwd:
        return HttpResponse(f"<h1>欢迎你{email}登录成功</h1>")
    else:
        return render(request, "book/index_form.html")


def index_form(request):
    return render(request, "book/index.html")
