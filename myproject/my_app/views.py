from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from my_app.models import SmallDogs
from my_app.models import LargeDogs

# Create your views here.
# def hello(request):
#     return render(request, "ashle/CSE 310/Web App/myproject/my_app/template/hello.html", {})

def index(request):
    template = loader.get_template('my_app/index2.html')
    context = {}
    return HttpResponse(template.render(context, request))

def smallDogs(request):
    smalldogList = SmallDogs.objects.all()
    template = loader.get_template('my_app/index.html')
    context = {
        'smalldogList': smalldogList,
    }
    return HttpResponse(template.render(context, request))

def largeDogs(request):
    largedogList = LargeDogs.objects.all()
    template = loader.get_template('my_app/index1.html')
    context = {
        'largedogList': largedogList,
    }
    return HttpResponse(template.render(context, request))