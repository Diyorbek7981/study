from django.contrib import admin
from .models import *

# Admin panelidagi korinadigan narsalar uchun
class RoomAdmin(admin.ModelAdmin):
    list_display = ("title","content","created","category")
    list_display_links = ("title","content")
    search_fields = ("title","content")

#Admin panelidagi obektlar

admin.site.register(Category)
admin.site.register(RommModel,RoomAdmin)
admin.site.register(Messages)
admin.site.register(User)
