from django.shortcuts import render, HttpResponse,redirect,reverse
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
from .forms import  RegisterForm, LoginForm
from .models import UserInfo

def register(request):
    # 没有绑定数据的表单
    reg_form = RegisterForm()
    if request.method == 'POST':
        #绑定数据的表单
        reg_form = RegisterForm(request.POST)
        if reg_form.is_valid():
            # is_valid => 用来验证表单中的所有数据中否都合法
            # 验证用户名：检查用户是否已经在数据中存在，可以对某个字段来验证
            # 给某个字段添加验证方法:定义form的时候，clean_字段名
            # 给整个表单添加验证方法：定义form的时候，加一个clean方法
            username = reg_form.cleaned_data["username"]
            password = reg_form.cleaned_data["password"]
            print("合法")
            password=make_password(password)
            UserInfo.objects.create(username=username,password=password)
        else:
            print("不合法")
    return render(request, 'forms_base/register.html', {"form":reg_form})


def login(request):
    login_form = LoginForm()
    msg=''
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        # is_valid提交的数据合法(会检查所有字段及表单整体的合法性)
        if login_form.is_valid():
            password = login_form.cleaned_data["password"]
            user = UserInfo.objects.get(username=login_form.cleaned_data["username"])
            if check_password(password,user.password):
                print('用户名密码验证成功')
                request.session['user']=user.username
                return redirect(reverse('forms_base:index'))
            else:
                messages.add_message(request,messages.INFO,'用户名密码验证失败')
                print('用户名密码验证失败')
    kwgs={
        'form':login_form,
        'msg':msg
    }

    return render(request, 'forms_base/login.html', kwgs)


def logout(request):
    print('退出成功')
    return HttpResponse("退出成功")


def index(req):
    return render(req,'forms_base/index.html')