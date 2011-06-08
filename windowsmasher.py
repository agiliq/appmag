import json
from browse.models import *
from django.template.defaultfilters import slugify
import string
image = open("windows_apps.json").read()
data = json.loads(image)

        
for datum in data:
    try:
        tmp = string.lower(datum["category"][0])    
        slugy =slugify(tmp)
        cat, created = Category.objects.get_or_create(name = tmp,slug=slugy)
    except:
        continue
    try:
        tmp =datum["developer"].pop()
    except:
        tmp = "None"
    devel, created = Developer.objects.get_or_create(name = tmp, slug =slugify(tmp))
    obj = App()
    try:
        obj.title = datum["name"].pop()
    except:
        continue
    obj.slug = slugify(obj.title)
    try:
        obj.url = datum["url"].pop()
        obj.description = datum["desc"].pop()
        obj.logo = datum["logo"].pop()
    except:
        pass
    price = datum["price"].pop()
    if price != "null":
        obj.price = price
    else:
        obj.price = "FREE"
    obj.platform = 	'WM'
    obj.category = cat
    obj.developer = devel
    #print datum["rating"]
    obj.rating = float(datum["rating"].pop())/100
    obj.save()
    a = []
    for thums in datum['screen']:
        thumb = Thumbnail()
       # print thums
        thumb.image = thums
        thumb.save()
        a.append(thumb)
    obj.thumbnails = a
    dev, created = Device.objects.get_or_create(name = "Windows Phone", slug =slugify("winphone"))
    dev.save()
    b=[]
    b.append(dev)
    #~ b=[]
    #~ for dev in datum["support"]:
        #~ devi, created = Device.objects.get_or_create(name = dev, slug =slugify(dev))
        #~ devi.name = dev
        #~ devi.slug = slugify(dev)
        #~ devi.save()
        #~ b.append(devi)
    #~ obj.device = b
    obj.device = b
    obj.save()
    print obj
