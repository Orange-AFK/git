from django.contrib import admin
from .models import Article  # 引用当前文件夹下的models文件的模型Article

# Register your models here.
@admin.register(Article)  # 修饰admin定制类，注册Article模型对应下面的Article定制类
class ArticleAdmin(admin.ModelAdmin):  # Article模型的定制类
    list_display = ("id", "title", "content", "author", "is_deleted", "created_time", "last_updated_time")  # 定制ddmin后台管理，显示标题和内容,id为自动创建的主键显示序列
    ordering = ("id",)  # 让序列号正序排列
    

# admin.site.register(Article, ArticleAdmin)  # 在后台管理中注册创建的应用
