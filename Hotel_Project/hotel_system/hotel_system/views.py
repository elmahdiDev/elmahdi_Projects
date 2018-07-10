from django.http import HttpResponse


from django.shortcuts import render

def Welcome(request):
    return render(request, "welcome.html")
    
