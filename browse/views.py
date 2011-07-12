from django.http import HttpResponse, Http404, HttpResponseRedirect, HttpResponseNotFound
from django.template import Context, loader, RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from browse.models import *

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
    
def device(request):
    profile = Device.objects.all()
    t = loader.get_template('browse/device.html')
    c =RequestContext(request,{'profile':profile})
    return HttpResponse(t.render(c))
    
def developer(request):
    profile = Developer.objects.all()
    t = loader.get_template('browse/developer.html')
    c =RequestContext(request,{'profile':profile})
    return HttpResponse(t.render(c))
    
def platform(request):
    profile = PLATFORMS
    t = loader.get_template('browse/platform.html')
    c =RequestContext(request,{'profile':profile})
    return HttpResponse(t.render(c))
    
def get_list_category(request,slug):
    profile = App.objects.values_list('title','logo','slug','platform').filter(slug__isnull=False).exclude(slug__exact='').filter(category__slug=slug).distinct()
    pro = App.objects.filter(slug__isnull=False).exclude(slug__exact='').filter(platform=profile[0][3]).distinct()
    platform = pro[0].get_platform_display() #_display()
    dev = Category.objects.filter(slug=slug)[0]
    slug=dev.name
    t = loader.get_template('browse/listcategory.html')
    c = RequestContext(request,{'profile':profile,'slug':slug,'platform':platform})
    return HttpResponse(t.render(c))

def get_list_device(request,slug):
    profile = App.objects.values_list('title','logo','slug','platform').filter(slug__isnull=False).exclude(slug__exact='').filter(device__slug=slug).distinct()
    pro = App.objects.filter(slug__isnull=False).exclude(slug__exact='').filter(platform=profile[0][3]).distinct()
    platform = pro[0].get_platform_display() #_display()
    dev = Device.objects.filter(slug=slug)[0]
    slug=dev.name
    t = loader.get_template('browse/listdevice.html')
    c = RequestContext(request,{'profile':profile,'slug':slug,'platform':platform})
    return HttpResponse(t.render(c))

def get_list_developer(request,slug):
    profile = App.objects.values_list('title','logo','slug','platform').filter(slug__isnull=False).exclude(slug__exact='').filter(developer__slug=slug).distinct()
    pro = App.objects.filter(slug__isnull=False).exclude(slug__exact='').filter(platform=profile[0][3]).distinct()
    platform = pro[0].get_platform_display() #_display()
    dev = Developer.objects.filter(slug=slug)[0]
    slug=dev.name
    t = loader.get_template('browse/listdeveloper.html')
    c = RequestContext(request,{'profile':profile,'slug':slug,'platform':platform})
    return HttpResponse(t.render(c))
    
def get_list_platform(request,slug):
    #print slug
    plat="AP"
    if slug=="Android":
        plat="AN"
    if slug=="iPhone":
        plat="AP"
    if slug=="Blackberry":
        plat="BB"
    if slug=="Windows_Mobile":
        plat="WM"
     
    profile = App.objects.values_list('title','logo','slug').filter(slug__isnull=False).exclude(slug__exact='').filter(platform=plat).distinct()
    pro = App.objects.filter(slug__isnull=False).exclude(slug__exact='').filter(platform=plat).distinct()
    platform = pro[0].get_platform_display() #_display()
    #print platform
    t = loader.get_template('browse/listplatform.html')
    c = RequestContext(request,{'profile':profile,'slug':slug,'platform':platform})
    return HttpResponse(t.render(c))
   #used for old url scheme
def get_app(request,id):
    profile = App.objects.filter(slug=id)[:1]
    developerlist = App.objects.values_list('title','logo','slug').filter(slug__isnull=False).exclude(slug__exact='').exclude(title=profile[0].title).filter(developer = profile[0].developer).order_by('?').distinct()[:10]
    related = App.objects.values_list('title','logo','slug').filter(slug__isnull=False).exclude(slug__exact='').exclude(title=profile[0].title).filter(category = profile[0].category).filter(platform=profile[0].platform).order_by('?').distinct()[:10]
    more = morelinks.objects.filter(app__slug=id)
    t = loader.get_template('browse/appdetails.html')
    c = RequestContext(request,{'profile':profile, 'developerlist':developerlist,'related':related,'morelinks':more})
    return HttpResponse(t.render(c))
    # new url scheme
def get_app1(request,id,platform):
    plat="AP"
    if platform=="Android":
        plat="AN"
    if platform=="iPhone":
        plat="AP"
    if platform=="Blackberry":
        plat="BB"
    if platform=="Windows_Mobile":
        plat="WM"
    profile = App.objects.filter(slug=id).filter(platform=plat)[:1]
    developerlist = App.objects.values_list('title','logo','slug').filter(slug__isnull=False).exclude(slug__exact='').exclude(title=profile[0].title).filter(developer = profile[0].developer).order_by('?').distinct()[:10]
    related = App.objects.values_list('title','logo','slug').filter(slug__isnull=False).exclude(slug__exact='').exclude(title=profile[0].title).filter(category = profile[0].category).filter(platform=profile[0].platform).order_by('?').distinct()[:10]
    also = App.objects.filter(title=profile[0].title).exclude(id=profile[0].id).exclude(platform=profile[0].platform)
    more = morelinks.objects.filter(app__id=profile[0].id)
    t = loader.get_template('browse/appdetails.html')
    c = RequestContext(request,{'profile':profile, 'developerlist':developerlist,'related':related,'morelinks':more,'also':also})
    return HttpResponse(t.render(c))
