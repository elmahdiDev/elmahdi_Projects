from controllers.hotel import *
from controllers.customer import *
from controllers.reservation import *
from controllers.notification import *
from controllers.main import *
from controllers.tester import *
from django.http import HttpResponse

def HelloWorld(request):
    return HttpResponse('hello world')

def Welcome(request):
    return HttpResponse('Welcome to my first django page')