from django.contrib import admin
from core.models import AboutSection, Post, Projects
from . import models


# Register your models here.

class AboutSectionAdmin(admin.ModelAdmin):
    model = AboutSection
    list_display = ("title", "subheading", "body", "image")

class PostSectionAdmin(admin.ModelAdmin):
    model = Post
    

class ProjectsAdmin(admin.ModelAdmin):
    model: Projects
    

admin.site.register(AboutSection, AboutSectionAdmin)

admin.site.register(models.Post)
admin.site.register(models.Projects)

