from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.base import View

from .models import *


class BaseView(TemplateView):

    def get_context_data(self, **kwargs):
        context = super(BaseView, self).get_context_data(**kwargs)
        profile = Category.objects.all()
        context['profile'] = profile
        return context


class IndexView(BaseView):
    template_name = 'browse/index.html'

index = IndexView.as_view()


class HomeView(BaseView):
    template_name = 'browse/home.html'

home = HomeView.as_view()


class DeviceView(TemplateView):
    template_name = 'browse/device.html'

    def get_context_data(self, **kwargs):
        context = super(DeviceView, self).get_context_data(**kwargs)
        profile = Device.objects.all()
        context['profile'] = profile
        return context

device = DeviceView.as_view()


class DeveloperView(TemplateView):
    template_name = 'browse/developer.html'

    def get_context_data(self, **kwargs):
        context = super(DeveloperView, self).get_context_data(**kwargs)
        profile = Developer.objects.all()
        context['profile'] = profile
        return context

developer = DeveloperView.as_view()


class PlatformView(TemplateView):
    template_name = 'browse/platform.html'

    def get_context_data(self, **kwargs):
        context = super(PlatformView, self).get_context_data(**kwargs)
        profile = PLATFORMS
        context['profile'] = profile
        return context

platform = PlatformView.as_view()


class CategoryView(View):
    template_name = 'browse/listcategory.html'

    def get(self, request, slug, **kwargs):
        profile = App.objects.values_list('title',
                                          'logo', 'slug',
                                          'platform').filter(slug__isnull=False).exclude(slug__exact='').filter(category__slug=slug).distinct()
        pro = App.objects.filter(slug__isnull=False).exclude(slug__exact='').filter(platform=profile[0][3]).distinct()
        platform = pro[0].get_platform_display()
        dev = Category.objects.filter(slug=slug)[0]
        slug = dev.name
        context = {'profile': profile, 'slug': slug, 'platform': platform}
        return render(request, self.template_name, context)


get_list_category = CategoryView.as_view()


class ListdeviceView(View):
    template_name = 'browse/listdevice.html'

    def get(self, request, slug, **kwargs):
        profile = App.objects.values_list('title',
                                          'logo',
                                          'slug',
                                          'platform').filter(slug__isnull=False).exclude(slug__exact='').filter(device__slug=slug).distinct()
        pro = App.objects.filter(slug__isnull=False).exclude(slug__exact='').filter(platform=profile[0][3]).distinct()
        platform = pro[0].get_platform_display()
        dev = Device.objects.filter(slug=slug)[0]
        slug = dev.name
        context = {'profile': profile, 'slug': slug, 'platform': platform}
        return render(request, self.template_name, context)

get_list_device = ListdeviceView.as_view()


class ListdeveloperView(View):
    template_name = 'browse/listdeveloper.html'

    def get(self, request, slug, **kwargs):
        profile = App.objects.values_list('title',
                                          'logo',
                                          'slug',
                                          'platform').filter(slug__isnull=False).exclude(slug__exact='').filter(developer__slug=slug).distinct()
        pro = App.objects.filter(slug__isnull=False).exclude(slug__exact='').filter(platform=profile[0][3]).distinct()
        platform = pro[0].get_platform_display()
        dev = Developer.objects.filter(slug=slug)[0]
        slug = dev.name
        context = {'profile': profile, 'slug': slug, 'platform': platform}
        return render(request, self.template_name, context)

get_list_developer = ListdeveloperView.as_view()


class ListplatformView(View):
    template_name = 'browse/listplatform.html'

    def get(self, request, slug, **kwargs):
        plat = "AP"
        if slug == "Android":
            plat = "AN"
        if slug == "iPhone":
            plat = "AP"
        if slug == "Blackberry":
            plat = "BB"
        if slug == "Windows_Mobile":
            plat = "WM"

        profile = App.objects.values_list('title',
                                          'logo',
                                          'slug').filter(slug__isnull=False).exclude(slug__exact='').filter(platform=plat).distinct()
        pro = App.objects.filter(slug__isnull=False).exclude(slug__exact='').filter(platform=plat).distinct()
        platform = pro[0].get_platform_display()
        context = {'profile': profile, 'slug': slug, 'platform': platform}
        return render(request, self.template_name, context)

get_list_platform = ListplatformView.as_view()


class GetappView(View):
    template_name = 'browse/appdetails.html'

    def get(self, request, id):
        profile = App.objects.filter(slug=id)[:1]
        developerlist = App.objects.values_list('title',
                                                'logo',
                                                'slug').filter(slug__isnull=False).exclude(slug__exact='').exclude(title=profile[0].title).filter(developer=profile[0].developer).order_by('?').distinct()[:10]
        related = App.objects.values_list('title',
                                          'logo',
                                          'slug').filter(slug__isnull=False).exclude(slug__exact='').exclude(title=profile[0].title).filter(category=profile[0].category).filter(platform=profile[0].platform).order_by('?').distinct()[:10]
        more = morelinks.objects.filter(app__slug=id)
        context = {'profile': profile,
                   'developerlist': developerlist,
                   'related': related,
                   'morelinks': more}
        return render(request, self.template_name, context)

get_app = GetappView.as_view()


class Getapp1View(View):
    template_name = 'browse/appdetails.html'

    def get(self, request, id, platform, **kwargs):
        plat = "AP"
        if platform == "Android":
            plat = "AN"
        if platform == "iPhone":
            plat = "AP"
        if platform == "Blackberry":
            plat = "BB"
        if platform == "Windows_Mobile":
            plat = "WM"
        profile = App.objects.filter(slug=id).filter(platform=plat)[:1]
        developerlist = App.objects.values_list('title',
                                                'logo',
                                                'slug').filter(slug__isnull=False).exclude(slug__exact='').exclude(title=profile[0].title).filter(developer=profile[0].developer).order_by('?').distinct()[:10]
        related = App.objects.values_list('title',
                                          'logo',
                                          'slug').filter(slug__isnull=False).exclude(slug__exact='').exclude(title=profile[0].title).filter(category=profile[0].category).filter(platform=profile[0].platform).order_by('?').distinct()[:10]
        also = App.objects.filter(title=profile[0].title).exclude(id=profile[0].id).exclude(platform=profile[0].platform)
        more = morelinks.objects.filter(app__id=profile[0].id)
        context = {'profile': profile,
                   'developerlist': developerlist,
                   'related': related,
                   'morelinks': more,
                   'also': also}
        return render(request, self.template_name, context)

get_app1 = Getapp1View.as_view()
