from django.db import models

class Recpices(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    slug = models.SlugField()
    preparation_time = models.IntegerField()
    preparation_time_unit = models.CharField(max_length=50)
    servings = models.IntegerField()
    serving_unit = models.CharField(max_length=50)
    preparation_steps = models.TextField()
    preparation_steps_is_html = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='recipes/covers/%Y%m%d/')