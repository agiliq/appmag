import json, os, sys
sys.path.append(os.path.join(os.getcwd()))

from django.template.defaultfilters import slugify

from browse.models import *


image = open("detail.json").read()
data = json.loads(image)

        
for datum in data:
    obj = App()
    try:
        tmp = datum["category"].pop()    
        slugy =slugify(tmp)
        cat, created = Category.objects.get_or_create(name = tmp,slug=slugy)
        obj.category = cat
    except:
        continue
    try:
        tmp =datum["developer"].pop().strip('By ')
    except:
        tmp = "None"
    devel, created = Developer.objects.get_or_create(name = tmp, slug =slugify(tmp))
    obj.developer = devel
    try:
        obj.title = datum["name"].pop()
    except:
        continue
    obj.slug = slugify(obj.title)
    obj.description = datum["desc"].pop()
    obj.url = datum["url"].pop()
    obj.logo = datum["logo"].pop()
    obj.price = datum["price"].pop()
    obj.platform = 	'AP'
    obj.save()
    a = []
    for thums in datum["screen"]:
        thumb = Thumbnail()
        thumb.image = thums
        thumb.save()
        a.append(thumb)
    obj.thumbnails = a
    b=[]
    dev, created = Device.objects.get_or_create(name = "iPhone", slug =slugify("iPhone"))
    print obj
    dev.save()
    b.append(dev)
    obj.device = b
    obj.save()
