from django.contrib import admin
from .models import Post

# Register your models here.

# This will make Posts appear on the browser GUI
# Comment this in or out and refresh local server to see the difference
admin.site.register(Post)