from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(TextPage)

class FileInLine(admin.TabularInline):
    model = File

class EventAdmin(admin.ModelAdmin):
    inlines = [
        FileInLine,
    ]
admin.site.register(Event,EventAdmin)

admin.site.register(File)
