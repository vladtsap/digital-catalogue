from django.contrib import admin
from .models import Subject, Art, Group, Book
# Register your models here.


class SubjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name', )}


class ArtAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name', )}


class GroupAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name', )}


class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name', )}


admin.site.register(Subject, SubjectAdmin)
admin.site.register(Art, ArtAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Book, BookAdmin)