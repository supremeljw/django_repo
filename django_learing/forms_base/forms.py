# 通过django.forms定义表单
from django import forms
from . import models


class RegisterForm(forms.ModelForm):
    """注册表单"""
    # 因为Model中的元素默认是会把密码显示出来的，所以在这里重新定义一个password
    password = forms.CharField(label="输入密码", max_length=18, widget=forms.PasswordInput)
    password2 = forms.CharField(label="确认密码", max_length=18, widget=forms.PasswordInput)
    class Meta:
        model = models.UserInfo
        # 将model UserInfo中的字段生成到表单
        # exclude表示排除哪个字段，fields表示包含哪个字段， 两个选项必须选其一
        # exclude = ()
        fields = ('username', 'password')

    def clean_username(self):
        """
        对username字段做检查用户名是否已经被注册
        注意字段一定要有返回值
        """
        # self.cleaned_data["username"] => 获取表单提交的username数据
        users = models.UserInfo.objects.filter(username=self.cleaned_data["username"])
        if not users:
            return self.cleaned_data["username"]
        else:
            raise forms.ValidationError("该用户名已经被使用")

    def clean(self):
        """
        验证两次输入的密码是否一次
        对整个表单验证时，不需要返回值
        """
        if self.cleaned_data["password"] != self.cleaned_data["password2"]:
            raise forms.ValidationError("密码不一致！")


class LoginForm(forms.ModelForm):
    """登录表单"""
    password = forms.CharField(label="密码", max_length=30, widget=forms.PasswordInput(attrs={"size": 20, }))

    def clean_username(self):
        user = models.UserInfo.objects.filter(username__iexact=self.cleaned_data["username"])
        if not user:
            raise forms.ValidationError("用户不存在")
        else:
            return self.cleaned_data["username"]

    class Meta:
        model = models.UserInfo
        exclude = ()