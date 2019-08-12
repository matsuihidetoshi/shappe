from django.db import models

class Question(models.Model):
  title = models.CharField(max_length=512)
  content = models.TextField(max_length=65536)

  def __str__(self):
        return self.title