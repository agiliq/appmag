from browse.models import *
from haystack import site
from haystack.indexes import *
class AppIndex(SearchIndex):
   text = CharField(document = True, use_template = True)
   title = CharField(model_attr = "title")
#   description = CharField(model_attr = "description")
#   developer = MultiValueField()
#   developer = CharField(model_attr = "developer")
#   device = MultiValueField()

#   def prepare_developer(self, obj): 
#       return [a for a in Developer.objects.all()]
   def index_queryset(self):
       return App.objects.all()
class DeveloperIndex(SearchIndex):
   text = CharField(document = True, use_template = True)
   name = CharField(model_attr = "name")

site.register(App, AppIndex)   
site.register(Developer, DeveloperIndex)
