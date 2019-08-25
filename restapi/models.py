from django.db import models
import numpy as np

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

  def calculate_ratio(
    self, result1, result2,
    result3, result4, result5
    ):
        results = np.array([result1, result2, result3, result4, result5])
        sum = results.sum()
        sum = 1 if sum == 0 else sum

        self.ratio_1 = (result1 / sum) * 100
        self.ratio_2 = (result2 / sum) * 100
        self.ratio_3 = (result3 / sum) * 100
        self.ratio_4 = (result4 / sum) * 100
        self.ratio_5 = (result5 / sum) * 100

        self.save()
        return
