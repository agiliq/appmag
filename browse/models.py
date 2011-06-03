from django.db import models
RATINGS = (
	((0),('Not yet Rated')),
	((1),('Poor')),
	((2),('Average')),
	((3),('Above Average')),
	((4),('Good')),
	((5),('Very Good')),
	    )
     
PLATFORMS = (
	(('AN'),('Android')),
	(('AP'),('iPhone')),
	(('BB'),('Blackberry')),
	(('WM'),('Windows Mobile')),
	    )
class Developer(models.Model):
    name = models.CharField(max_length=200)
    def __unicode__(self):
        return self.name

class Thumbnail(models.Model):
    image = models.ImageField("Thumbnail",upload_to='thumbnails')
    def __unicode__(self):
        return self.image.name
	
class Device(models.Model):
    name = models.CharField("Device Name",max_length=50)
    def __unicode__(self):
        return self.name
class Catagory(models.Model):
    name = models.CharField("Catagory",max_length=100)
    def __unicode__(self):
	return self.name
class App(models.Model):
    title = models.CharField("Title", max_length=150)
    description = models.TextField("Description", max_length=10000)
    rating = models.IntegerField("Rating",max_length=1,choices = RATINGS, default= 0,null=True,blank=True)
    developer = models.ForeignKey(Developer,verbose_name="Developer",null=True,blank=True)
    url = models.URLField("Link")
    logo = models.ImageField("Logo",upload_to='logos',null = True, blank = True)
    thumbnails = models.ManyToManyField(Thumbnail, null = True)
    price = models.CharField("Price",max_length =10,default="FREE",null=True,blank=True)
    device = models.ForeignKey(Device)
    catagory = models.ForeignKey(Catagory)
    platform = models.CharField("Platform",choices=PLATFORMS,max_length=2)
    def __unicode__(self):
        return self.title
 
