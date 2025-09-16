from django.db import models
from django.utils.text import slugify 

class Blog(models.Model):
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(unique=True)
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        # Custom save logic to auto-generate slug from title
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
