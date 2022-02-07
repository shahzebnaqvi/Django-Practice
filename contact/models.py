from asyncio.windows_events import NULL
from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length = 100)
    body = models.CharField(max_length = 100)
    is_completed = models.BooleanField(default=False)
    date_created = models.DateField(auto_created=True)
    last_modified = models.DateField(auto_now=True)

    def __str___(self):
        return self.title
        # signup table
class Signup(models.Model):
    number = models.CharField(max_length = 100, default="False")
    name = models.CharField(max_length = 100, default="False")
    email = models.CharField(max_length = 100, default="False")
  
    def __str___(self):
        return self.number