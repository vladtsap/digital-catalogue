from django.contrib import admin
from lgaapp.models import Subject, Art, Group, Book, Place


class SubjectAdmin(admin.ModelAdmin):
	list_display = ['name', ]


class ArtAdmin(admin.ModelAdmin):
	list_display = ['name', ]


class GroupAdmin(admin.ModelAdmin):
	list_display = ['name', ]


class PlaceAdmin(admin.ModelAdmin):
	list_display = ['name', ]


class BookAdmin(admin.ModelAdmin):
	list_display = ['name', ]


admin.site.register(Subject, SubjectAdmin)
admin.site.register(Art, ArtAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Place, PlaceAdmin)
admin.site.register(Book, BookAdmin)
