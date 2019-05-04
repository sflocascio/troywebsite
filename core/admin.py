from django.contrib import admin
from core.models import AboutSection


# Register your models here.

class AboutSectionAdmin(admin.ModelAdmin):
    model = AboutSection
    list_display = ("title", "subtitle", "subheading", "body")



admin.site.register(AboutSection, AboutSectionAdmin)