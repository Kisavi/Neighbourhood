from django.contrib import admin
from .models import Profile, Post, Business, Alert

# Register your models here.
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Business)
admin.site.register(Alert)
