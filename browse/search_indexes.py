from browse.models import *
from haystack import indexes
from browse.models import App


class AppIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr="title")

    def get_model(self):
        return App

    def index_queryset(self, using=None):
        return self.get_model.objects.all()


# class DeveloperIndex(indexes.SearchIndex, indexes.Indexable):
#     text = indexes.CharField(document=True, use_template=True)
#     name = indexes.CharField(model_attr="name")

    # def get_model(slef):
    #   return Developer
