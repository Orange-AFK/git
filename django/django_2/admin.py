from django.contrib import admin
# 应用创建的Article模型
from .models import  Article

# Register your models here.
admin.site.register(Article)  # 注册模型的后台管理
