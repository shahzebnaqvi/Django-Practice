from django.contrib import admin

from contact.models import Signup, Todo

# Register your models here.
admin.site.register(Todo)
admin.site.register(Signup)