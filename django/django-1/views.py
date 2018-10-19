from django.http import HttpResponse

# 定义一个处理方法，固定参数request
def index(request):

    # 返回字符串helloworld
    return HttpResponse("Hello, world")
