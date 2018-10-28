from django.shortcuts import render_to_response, get_object_or_404  # 引用render_to_response方法简化render代码的写法,引用get_object_or_404方法，简化网页异常抛出错误信息的代码写法
# from django.http import HttpResponse, Http404  # 引用404方法，在网页出错是提示404页面不存在
from .models import Article  # 引用文件夹下models的模型

# Create your views here.
def article_detail(request, article_id):  # 创建处理方法,获取文章标题和内容
    # try:  # 处理网页异常
        # article = Article.objects.get(id=article_id)  # 使用django内置方法objects.get()获取内容，设置获取条件为article_id以获取内容
        article = get_object_or_404(Article, pk=article_id)  # 第一个参数为模型，第二个参数为条件，传入主键，可以直接使用主键的简写pk
        context = {}  # 创建一个字典作为render的第三个参数
        context['article_obj'] = article  # 传递已经取到的文章对象article到字典内
        return render_to_response("article_detail.html", context)  # 下一段代码的简化方法,功能相同,仅需要两个参数，一个模板的地址，一个字典
        # return render(request, "article_detail.html", context)  # 第一个参数request，第二个参数需要模板页面的地址，第三个参数为字典
    # except Article.DoesNotExist:  # 捕获页面不存在异常
        # return HttpResponse("不存在")
        # raise Http404("not exist")  # 当网页不存在抛出预定的错误信息
    # return HttpResponse("文章id: %s" % article_id)  # 返回文章id
    # return HttpResponse("<h2>文章标题: %s</h2><br>文章内容: %s" % (article.title, article.content))  # 使用article这个对象，输出它的标题，title，以及内容content,其中<br>是HTML换行标记<h2>设置标题

def article_list(request):  # 创建处理方法，获取文章列表
    # articles = Article.objects.all()  # 通过objects获取全部对象获取文章列表存储于变量中
    articles = Article.objects.filter(is_deleted=False)  # 对应models的是否删除字段，若标记为删除则不显示
    context = {}
    context['articles'] = articles
    return render_to_response("article_list.html", context)
