from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
from .models import Topic

# Create your views here.
def index(request):
    template = loader.get_template('myhp/index.html')
    #context = {}
    return HttpResponse(template.render(request))

def news(request):
    queryset = Topic.objects.all()
    context = { "news":queryset }
    return render(request, 'news.html', context)

def hello_template(request):
    return render(request, 'index.html')