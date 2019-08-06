from django.db import models
from django.contrib.auth.models import User
class Category(models.Model):
    """快速上手示例"""
    # 定义字段
    name = models.CharField(max_length=30, verbose_name='分类名称')
    desc = models.CharField(max_length=255, default=None, verbose_name='分类描述')
    index = models.IntegerField(default=999, verbose_name='分类的排序')

    # 设置元数据（设置查询和展示的输出）
    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name
        ordering = ['index', 'id']
        db_table = "category"

    # 类的魔术方法，返回一个友好的显示
    def __str__(self):
        return self.name
import random
def func01():
    return random.randint(6000,7000)

from django.core.exceptions import ValidationError
def check_score(value):
    if value < 0:
        raise ValidationError(f"{value} 必须大于等于0")


class Course(models.Model):
    """课程表-处理模型关系"""
    # name = models.CharField('课程名', max_length=10)
    course_name = models.CharField(verbose_name='课程名', max_length=10)
    # 多对一：一门课只能一个老师上，一个老师可以上多门课
    teacher = models.ForeignKey(User, verbose_name="任课老师", related_name='course_teacher_user')
    # 一对一关系：一门课程只能有一个课代表，一个课代表只能当一个课代表
    monitor = models.OneToOneField(User, verbose_name="课代表", related_name="course_monitor_user")
    # ForeignKey 与 OneToOneField
    # 如果被选模型可以选多次，则可定义为ForeignKey
    # 如果被选模型只能选一次，则可定义为OneToOneField
    #  多对多关系: ManyToManyField
    def __str__(self):
        return self.course_name

    class Meta:
        verbose_name = "课程列表"
        verbose_name_plural = verbose_name


class Student(models.Model):
    """
    primary_key : 设置主键
    如果表中定义了主键，就不会再创建名为id的主键字段了
    verbose_Name: 设置名称(或第一个位置参数（在Fk，M2M和O2O不行）)
    """
    SEX_CHOICES2 = (
        (None, '请选择'),  # 把------去掉
        (0, '男'),
        (1, '女'),
    )
    # AutoField: 自增型字段（值自增） => int
    student_id = models.AutoField(primary_key=True)
    # max_length将在数据库层和Django表单验证中起作用, 用来限定字段的长度。
    username = models.CharField("用户名", max_length=10, db_index=True) # varchar(10)
    # 用于大文本数据
    desc = models.TextField(max_length=100, verbose_name="个人简介", help_text="这里来一些介绍吧，不要超过100个字")
    sex = models.IntegerField(verbose_name="性别", choices=SEX_CHOICES2)  # 0 => 男生， 1 => 女生
    # 录入时间
    insert_time = models.DateTimeField(auto_now_add=True, verbose_name="录入时间")
    # 更新时间
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    # 成绩
    english_score = models.FloatField(verbose_name="英语成绩", validators=[check_score])
    # 学费（跟钱相关的，一定要用这个字段类型）
    schooling = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="学费", default=func01)
    # 整数位：5位，小数位：2位
    # 只要表单层面验证，不在DB层面验证
    email = models.EmailField(verbose_name="邮箱")
    # 最后登录IP
    last_login_ip = models.GenericIPAddressField(verbose_name="最后登录IP")
    # 当前登录状态
    is_login = models.BooleanField()
    # NullBooleanField默认值是Null
    is_login2 = models.NullBooleanField()
    avator = models.ImageField(upload_to='avator/', default='avator/default.png', verbose_name="用户头像")
    # settings.py: MEDIA_ROOT, MEDIA_URL
    # urls.py    : 添加路由
    # null=False => 数据库 => 这是一个必填项
    allow_null = models.CharField(max_length=10, verbose_name="null=True", null=True)
    # blank=False => 表单 => 这是一个必填项
    allow_blank = models.CharField(max_length=10, verbose_name="blank=True", blank=True)
    # 注意事项：给一个字段设置值的时候，同时设置为True或同时设置为False
    select = models.CharField(max_length=10, db_column="choices")
    # student_number = models.CharField(max_length=10, unique=True)
    #
    courses = models.ManyToManyField(Course, verbose_name="选修课")

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "学生表"
        verbose_name_plural = verbose_name
        get_latest_by = 'update_time'
        # 设置这个字段作用：当使用latest和earliest查询时的排序字段
        # ordering = ['desc', '-student_id']
        # 查询
        ordering = ['-student_id']


    # save() => 保存信息
    # 重写save的目的
    def save(self, *args, **kwargs):
        # # 不保存数据则直接return
        # return
        print("student保存前")
        if self.sex == 0:
            self.username = self.username + "帅哥"
        elif self.sex == 1:
            self.username = self.username + "美女"
        super().save(*args, **kwargs)
        print("student保存后")


class Article(models.Model):
    title = models.CharField(max_length=64, verbose_name="文章标题")
    content = models.TextField(verbose_name="文章正文")
    author = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.title}-{self.author}"

    class Meta:
        unique_together = ["title", "author"]
        index_together = ["title", "author"]