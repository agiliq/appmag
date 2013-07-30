from django.db import models

PLATFORMS = (
    (('AN'), ('Android')),
    (('AP'), ('iPhone')),
    (('BB'), ('Blackberry')),
    (('WM'), ('Windows_Mobile')),
)


class Developer(models.Model):
    name = models.CharField("Developer", max_length=200)
    slug = models.CharField("Slug", max_length=50)

    def __unicode__(self):
        return self.name


class Thumbnail(models.Model):
    image = models.URLField("Thumbnail")

    def __unicode__(self):
        return self.image


class Device(models.Model):
    name = models.CharField("Device Name", max_length=50)
    slug = models.CharField("Slug", max_length=50)

    def __unicode__(self):
        return self.name


class Category(models.Model):
    name = models.CharField("Catagory", max_length=100)
    slug = models.CharField("Slug", max_length=50)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __unicode__(self):
        return self.slug


class App(models.Model):
    title = models.CharField("Title", max_length=250)
    slug = models.CharField("Slug", max_length=250)
    description = models.TextField("Description", max_length=10000)
    developer = models.ForeignKey(Developer, verbose_name="Developer", null=True, blank=True)
    url = models.URLField("Link")
    logo = models.URLField("Logo")
    thumbnails = models.ManyToManyField(Thumbnail, null=True, blank=True)
    price = models.CharField("Price", max_length=10, default="FREE", null=True, blank=True)
    device = models.ManyToManyField(Device, related_name="device")
    category = models.ForeignKey(Category, related_name="category")
    platform = models.CharField("Platform", choices=PLATFORMS, max_length=2)

    def __unicode__(self):
        return self.title


class morelinks(models.Model):
    link = models.CharField("Link", max_length=500)
    app = models.ForeignKey(App, related_name="morelinks")
