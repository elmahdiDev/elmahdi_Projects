from django.http import HttpResponse

def HelloWorld(request):
    return HttpResponse('hello world')

def Welcome(request):
    return HttpResponse('Welcome to my first django page')

