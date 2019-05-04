from django.contrib import admin
from core.models import AboutSection


# Register your models here.

class AboutSectionAdmin(admin.ModelAdmin):
    model = AboutSection
    list_display = ("title", "subheading", "body", "image")



admin.site.register(AboutSection, AboutSectionAdmin)