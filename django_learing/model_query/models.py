from django.db import models
from django.db import models

class BlogManager(models.Manager):
    def all_log(self):
        print("This is all blog info")
    pass

class Blog(models.Model):
    objects = BlogManager()
    name = models.CharField(max_length=100, verbose_name="标题")
    tagline = models.TextField(verbose_name="摘要")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return "http"+self.name

    # 还要记住传递参数给这个模型方法 —— 即*args, **kwargs。 Django 未来将一直会扩展内建模型方法的功能并添加新的参数。
    # 如果在你的方法定义中使用*args, **kwargs，将保证你的代码自动支持这些新的参数。
    def save(self, *args, **kwargs):
        print(self.name, "保存前")
        # Call the "real" save() method.
        # 必须要记住调用超类的方法—— `super(Blog, self).save(*args, **kwargs)`—— 来确保对象被保存到数据库中。
        # 如果你忘记调用超类的这个方法，默认的行为将不会发生且数据库不会有任何改变。
        super().save(*args, **kwargs)
        print(self.name, "保存后")

class Author(models.Model):
    name = models.CharField(max_length=50, verbose_name="姓名")
    email = models.EmailField(verbose_name="邮箱")
    age = models.IntegerField()
    def __str__(self):
        return self.name

class Entry(models.Model):
    """入口"""
    blog = models.OneToOneField(Blog, on_delete=models.PROTECT, null=True, blank=True, related_name = 'entry_set') # 默认related_name = entry
    # blog = models.ForeignKey(Blog, on_delete=models.PROTECT, null=True, blank=True) #　默认related_name = entry_set
    # blog = models.ForeignKey(Blog)
    headline = models.CharField(max_length=255, verbose_name="大标题")
    body_text = models.TextField(verbose_name="文章正文")
    pub_date = models.DateField(verbose_name="发布日期")
    mod_date = models.DateField(auto_now=True, verbose_name="修改日期")
    # 一篇论文可以有多个作者
    authors = models.ManyToManyField(Author, verbose_name="作者")
    n_comments = models.IntegerField(verbose_name="评论数")
    n_pingbacks = models.IntegerField(verbose_name="点击数")
    rating = models.IntegerField(verbose_name="论文定级")

    def __str__(self):
        return self.headline

class Publisher(models.Model):
    name = models.CharField(max_length=300)
    num_awards = models.IntegerField()
    def __str__(self):
        return self.name
class Book(models.Model):
    name = models.CharField(max_length=300)
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.FloatField()
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    pubdate = models.DateField()
    def __str__(self):
        return self.name
class Store(models.Model):
    name = models.CharField(max_length=300)
    books = models.ManyToManyField(Book)
    registered_users = models.PositiveIntegerField()
    def __str__(self):
        return self.name