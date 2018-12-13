from django.contrib import admin
from .models import Subject, Art
# Register your models here.

class SubjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name', )}


class ArtAdmin(admin.ModelAdmin):
    list_display = ['name', 'country']


admin.site.register(Subject, SubjectAdmin)
admin.site.register(Art, ArtAdmin)