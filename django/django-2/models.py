from django.db import models

# Create your models here.
class Article(models.Model):  # 定义模型并继承models的Model类
    title = models.CharField(max_length=30)  # 设置标题(CharField代表文本型字符型字段),定义长度限制为30个字符
    content = models.TextField()  # 设置内容
