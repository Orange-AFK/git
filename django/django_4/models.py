from django.db import models
from django.contrib.auth.models import User  # django用户模型
# Create your models here.
class Article(models.Model):  # 继承models的Model类
    title = models.CharField(max_length=30)  # 创建标题，使用字符串类型的字段，括号内设置长度限制
    content = models.TextField()  # 创建内容，使用文本字段
    created_time = models.DateTimeField(auto_now_add=True)  # 自动设置文件发布日期
    last_updated_time = models.DateTimeField(auto_now=True)  # 最后更新的时间
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, default=1)  # 添加外键设置作者,第一参数关联模型，第二参数删除文章是否删除作者，第三参数默认值设置为1
    is_deleted = models.BooleanField(default=False)  # 是否删除了，设置默认值为false不删除，用于标记数据是否删除，views更改方法对应这个类型
    readed_num = models.IntegerField(default=0)  # 阅读数量

    def __str__(self):
        return "<Article: %s>" % self.title  # 返回当前对象的标题
