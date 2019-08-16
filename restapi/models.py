from django.db import models

class Question(models.Model):
  title = models.CharField(max_length=512)
  content = models.TextField(max_length=65536)
  option_1 = models.CharField(max_length=512)
  result_1 = models.IntegerField(default=0)
  ratio_1 = models.IntegerField(default=20)
  option_2 = models.CharField(max_length=512)
  result_2 = models.IntegerField(default=0)
  ratio_2 = models.IntegerField(default=20)
  option_3 = models.CharField(max_length=512)
  result_3 = models.IntegerField(default=0)
  ratio_3 = models.IntegerField(default=20)
  option_4 = models.CharField(max_length=512)
  result_4 = models.IntegerField(default=0)
  ratio_4 = models.IntegerField(default=20)
  option_5 = models.CharField(max_length=512)
  result_5 = models.IntegerField(default=0)
  ratio_5 = models.IntegerField(default=20)

  def __str__(self):
        return self.title