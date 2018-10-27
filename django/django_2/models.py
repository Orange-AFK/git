from django.db import models

# Create your models here.
class Article(models.Model):  # 继承models的Model类
    title = models.CharField(max_length=30)  # 创建标题，使用字符串类型的字段，括号内设置长度限制
    content = models.TextField()  # 创建内容，使用文本字段
