# Create your views here
from django.http import HttpResponse, Http404,HttpResponseRedirect,HttpResponseNotFound
from django.template import Context,loader,RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from appster.browse.models import *

def index(request):
    profile = Category.objects.all()
    t = loader.get_template('browse/index.html')
    c =RequestContext(request,{'profile':profile})
    return HttpResponse(t.render(c))

def home(request):
    profile = Category.objects.all()
    t = loader.get_template('browse/home.html')
    c =RequestContext(request,{'profile':profile})
    return HttpResponse(t.render(c))
    
def get_list_category(request,slug):
    print slug
    profile = App.objects.filter(category__slug=slug)
    t = loader.get_template('browse/category.html')
    c = RequestContext(request,{'profile':profile})
    return HttpResponse(t.render(c))
