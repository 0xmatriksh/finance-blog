from django.contrib import admin
# from django_summernote.admin import SummernoteModelAdmin
from .models import Blog
from tinymce.widgets import TinyMCE
from django.db import models
from django.forms import TextInput

class BlogAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField : { 'widget':TinyMCE()},
        models.CharField: {'widget':TextInput(attrs={'size':'150'})}
    }

admin.site.register(Blog,BlogAdmin)