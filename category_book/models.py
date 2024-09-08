from django.db import models

class CategoryModel(models.Model):
    category_name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100,unique=True, null=True, blank=True)
    def __str__(self):
        return self.category_name