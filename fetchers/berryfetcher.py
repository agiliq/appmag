import json
from browse.models import *
from django.template.defaultfilters import slugify
import string
import time
image = open("berries.json").read()
data = json.loads(image)

        
for datum in data:
#    time.sleep(1)
    obj = App()
    try:
        tmp = string.lower(datum["category"].pop())    
        slugy =slugify(tmp)
        cat, created = Category.objects.get_or_create(name = tmp,slug=slugy)
        #print cat
        #if cat == 'NULL'
        #cat 
        #obj.category = cat
    except:
        cat, created = Category.objects.get_or_create(name = "Miscellaneous",slug="misc")
    obj.category = cat
    try:
        tmp =datum["developer"].pop()
    except:
        tmp = "None"
    devel, created = Developer.objects.get_or_create(name = tmp, slug =slugify(tmp))
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
        try:
            devi, created = Device.objects.get_or_create(name = dev, slug =slugify(dev))
            devi.name = dev
            devi.slug = slugify(dev)
            devi.save()
            b.append(devi)
        except:
            continue
    obj.device = b
    obj.save()
    print obj.id
