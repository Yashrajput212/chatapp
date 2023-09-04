from django.contrib import admin

from .models import *

# Register your models here.

class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'modified')
    ordering = ['-modified']

class MessageAdmin(admin.ModelAdmin):
    list_display = ('user', 'room', 'time')
    ordering = ['-time']

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'user')
    ordering = ['name']



admin.site.register(User),
admin.site.register(Room, RoomAdmin),
admin.site.register(Message, MessageAdmin),
admin.site.register(Contacts, ContactAdmin)
