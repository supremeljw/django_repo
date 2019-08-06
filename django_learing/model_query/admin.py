from django.contrib import admin
from .models import Blog,Entry,Author,Publisher,Store,Book


# 定制类
class EntryAdmin(admin.ModelAdmin):
    # 列表页显示的字段
    list_display = ('blog', 'n_comments', 'n_pingbacks', 'rating')
    # 可直接点击进入修改页面
    list_display_links = ('n_pingbacks',)
    # 可在列表页直接修改（链接和编辑不能同时用）
    list_editable = ('rating',)
    # 右侧过滤器
    list_filter = ('authors',)
    search_fields = ('authors', 'headline')
    # 编辑页显示/不显示哪些字段
    fields = ( 'date_count', 'unique_vistor')

# 定制关联类（Blog是外键）
class EntryInLine(admin.StackedInline):
    model = Entry
    extra = 0

# Blog是外键，希望编辑Blog是可以看到关联的类信息
class BlogAdmin(admin.ModelAdmin):
    # inlines: 关联数据,如外键/m2m/o2o, Blog是Entry的外键
    inlines = [EntryInLine,]


admin.site.register(Entry, EntryAdmin)
admin.site.register(Author)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Publisher)
admin.site.register(Store)
admin.site.register(Book)
