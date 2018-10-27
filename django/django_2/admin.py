from django.contrib import admin
from .models import Article  # 引用当前文件夹下的models文件的模型Article

# Register your models here.
admin.site.register(Article)  # 在后台管理中注册创建的应用
