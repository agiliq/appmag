import json
from browse.models import *
from django.template.defaultfilters import slugify
import string
image = open("berries.json").read()
data = json.loads(image)

        
for datum in data:
    try:
        tmp = string.lower(datum["category"].pop())    
        slugy =slugify(tmp)
        cat, created = Category.objects.get_or_create(name = tmp,slug=slugy)
    except:
        pass
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
    obj.description = datum["desc"].pop()
    obj.url = datum["url"].pop()
    obj.logo = datum["logo"].pop()
    price = datum["price"].pop()
    if price !="FREE":
        obj.price = price[3:]
    else:
        obj.price = "FREE"
    obj.platform = 	'BB'
    obj.category = cat
    obj.developer = devel
    star = datum["star"][0][54:55]
    if star == 'N':
        obj.rating = 0
    else:
        obj.rating = int(star)/2.0
    obj.save()
    a = []
    for thums in datum["screen"]:
        thumb = Thumbnail()
        thumb.image = thums
        thumb.save()
        a.append(thumb)
    obj.thumbnails = a
    b=[]
    for dev in datum["support"]:
        devi, created = Device.objects.get_or_create(name = dev, slug =slugify(dev))
        devi.name = dev
        devi.slug = slugify(dev)
        devi.save()
        b.append(devi)
    obj.device = b
    obj.save()
    print obj
