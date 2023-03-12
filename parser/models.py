from django.db import models


# Create your models here.

class Resource(models.Model):
    resource_name = models.CharField(max_length=255)
    resource_url = models.URLField()
    top_tag = models.CharField(max_length=255)
    bottom_tag = models.CharField(max_length=255)
    title_cut = models.CharField(max_length=255)
    date_cut = models.CharField(max_length=255)


class Item(models.Model):
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    link = models.URLField()
    title = models.CharField(max_length=255)
    content = models.TextField()
    nd_date = models.DateTimeField()
    s_date = models.DateTimeField(auto_now_add=True)
    not_date = models.DateField()
