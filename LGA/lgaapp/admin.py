from django.contrib import admin
from .models import Subject
# Register your models here.

class SubjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name', )}


admin.site.register(Subject, SubjectAdmin)
