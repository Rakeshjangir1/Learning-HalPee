from django.db import models
from tinymce.models import HTMLField
from autoslug import AutoSlugField


class chapter(models.Model):
    chapter_name = models.CharField(max_length=100)


status = ((0,"Draft"),(1,"Publish"))
class html_post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = AutoSlugField(populate_from='title', unique=True, null=True, default=None)
    updated_on = models.DateTimeField(auto_now=True)
    content = HTMLField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=status, default=0)

    def __str__(self):
        return self.title

class css_post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = AutoSlugField(populate_from='title', unique=True, null=True, default=None)
    updated_on = models.DateTimeField(auto_now=True)
    content = HTMLField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=status, default=0)

    def __str__(self):
        return self.title

