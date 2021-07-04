from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Blog

# Apply summernote to all TextField in model.
class BlogAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = ('content',)

admin.site.register(Blog, BlogAdmin)