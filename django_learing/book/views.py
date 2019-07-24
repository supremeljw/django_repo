from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    if request.method == "post":
        email = request.GET.get("email")
        pwd = request.GET.get('pwd')
        return HttpResponse("<h1>欢迎你，登录成功</h1>")
    return render(request, "book/index_form.html")


def index_form(request):
    return render(request, "book/index.html")
