from django.contrib import admin

# Register your models here.
from .models import Room, Topic, Message

admin.site.register(Room) # register the model (room) to the admin site
admin.site.register(Topic) # register the model (topic) to the admin site
admin.site.register(Message) # register the model (message) to the admin site