from django.db import models

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


class Student(models.Model):
    student_id=models.AutoField(primary_key=True,verbose_name='主键')
    name=models.CharField(max_length=10,verbose_name='姓名')
    desc=models.TextField(verbose_name='描述')
    insertDate=models.DateField(auto_now=True,verbose_name='插入时间')
    updateDate=models.DateField(auto_now_add=True,verbose_name='修改时间')
    email=models.EmailField(verbose_name='email')
    avator = models.ImageField(upload_to='avator/', default='imgs/default.png')
    def __str__(self):
        return self.name


