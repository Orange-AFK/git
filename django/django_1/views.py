from django.http import HttpResponse

def index(request):  # request为固定参数
    return HttpResponse("Hello world")  # 处理方法，返回helloworld
