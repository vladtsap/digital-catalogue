from django.contrib import admin
from .models import Subject, Art, Group, Book, Place


class SubjectAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug']
	prepopulated_fields = {'slug': ('name',)}


class ArtAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug']
	prepopulated_fields = {'slug': ('name',)}


class GroupAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug']
	prepopulated_fields = {'slug': ('name',)}


class PlaceAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug']
	prepopulated_fields = {'slug': ('name',)}


class BookAdmin(admin.ModelAdmin):
	list_display = ['name', 'slug']
	prepopulated_fields = {'slug': ('name', ('isbn'),)}


admin.site.register(Subject, SubjectAdmin)
admin.site.register(Art, ArtAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Place, PlaceAdmin)
admin.site.register(Book, BookAdmin)
