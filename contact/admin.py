from django.contrib import admin

from contact.models import  Todo, customerUsers

# Register your models here.
admin.site.register(Todo)
admin.site.register(customerUsers)