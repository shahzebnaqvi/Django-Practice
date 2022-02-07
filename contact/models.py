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
    number = models.CharField(max_length = 100)
    name = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 100)
  
    def __str___(self):
        return self.title