from django.contrib import admin
from api.models import Message, Delivery, Client

admin.site.register(Message)
admin.site.register(Delivery)
admin.site.register(Client)