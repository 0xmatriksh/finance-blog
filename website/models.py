from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from .utils import generate_slug

# Create your models here.


class Blog(models.Model):
    author = models.ForeignKey(User,blank=True,null=True,on_delete=models.CASCADE)
    title = models.CharField(max_length=1000)
    content = models.TextField()
    slug = models.SlugField(max_length=1000,null=True,blank=True)
    image = models.ImageField(upload_to='image/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = generate_slug(self.title)
        super(Blog, self).save(*args, **kwargs)

    @property
    def author_name(self):
        try :
            name = self.author.get_full_name()
        except : 
            name = self.author
        return name

