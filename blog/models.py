from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=225)
    description = models.CharField(max_length=225)
    content = models.TextField()
    author = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"