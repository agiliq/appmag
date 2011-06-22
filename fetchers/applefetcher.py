import json
from browse.models import *
from django.template.defaultfilters import slugify
image = open("detail.json").read()
data = json.loads(image)

        
for datum in data:
    try:
        tmp = datum["category"].pop()    
        slugy =slugify(tmp)
        cat, created = Category.objects.get_or_create(name = tmp,slug=slugy)
    except:
        pass
    try:
        tmp =datum["developer"].pop().strip('By ')
    except:
        tmp = "None"
    devel, created = Developer.objects.get_or_create(name = tmp, slug =slugify(tmp))
    obj = App()
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
    obj.category = cat
    obj.developer = devel
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
