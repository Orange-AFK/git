"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include  # 引用include包含子路由
from . import views  # 引用同一个文件夹下的views文件（内部写了path第二参数的处理方法）
from article.views import article_detail, article_list  # 引用应用内的方法
urlpatterns = [
    # 规定打开主页加admin，localhost:8000/admin/
    path('admin/', admin.site.urls),  # 已有方法,后台管理
    # 第一个参数规定打开的网址，留空即代表打开默认主页网址,第二参数规定处理方式，引用views文件定义的方法index
    path('', views.index),  # 本章新添方法
    # path('article/<int:article_id>', article_detail, name="article_detail"),  # 引入article_id变量设置为数字参数，使用article_detail方法进行网页处理，定义别名
    # path('article/', article_list, name="article_list"),  # 文章列表网址
    path('article/', include('article.urls'))
]
