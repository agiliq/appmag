import json,os,sys
from os import path
sys.path.append(os .path.join(os.getcwd()))
from browse.models import *
from django.template.defaultfilters import slugify
image = open("android_apps.json").read()
data = json.loads(image)

        
for datum in data:
    obj = App()
    try:
        tmp =datum["developer"].pop()
        devel, created = Developer.objects.get_or_create(name = tmp, slug =slugify(tmp))
        obj.developer = devel
    except:
        devel, created = Developer.objects.get_or_create(name = "Some Developer", slug =slugify("somedev"))
        obj.developer = devel
        print "Caught developer"
    try:
        tmp = datum["category"].pop()    
        slugy =slugify(tmp)
        obj.title = datum["name"].pop()
        cat, created = Category.objects.get_or_create(name = tmp,slug=slugy)
        obj.category = cat
    except:
        print "Caught You category"
        continue
    obj.slug = slugify(obj.title)
    obj.description = datum["desc"].pop()
    obj.url = datum["url"].pop()
    obj.logo = datum["logo"].pop()
    obj.price = datum["price"].pop()
    obj.platform = 	'AN'
    obj.rating = datum["rating"].pop()[8:11]
    obj.save()
    
    #~ crosscheck,status = App.objects.get_to_create(obj)
    #~ if status == True:
        #~ obj.title = obj.title + " andorid"
        #~ obj.save()
    a = []
    for thums in datum["screen"]:
        thumb = Thumbnail()
        thumb.image = thums
        thumb.save()
        a.append(thumb)
    obj.thumbnails = a
    b=[]
    dev, created = Device.objects.get_or_create(name = "Android", slug =slugify("android"))
    print obj
    dev.save()
    b.append(dev)
    obj.device = b
    obj.save()
