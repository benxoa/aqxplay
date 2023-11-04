from django.contrib import admin

# Register your models here.

from .models import Publish, Category

admin.site.register(Category)
@admin.register(Publish)
class AdminPublish(admin.ModelAdmin):
    list_display = ['date','title']