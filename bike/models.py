from django.db import models
from django.contrib.auth import get_user_model

class Bike(models.Model):
  name = models.CharField(max_length=100)
  color = models.CharField(max_length=100)
  description = models.TextField()
  purchaser = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

def __str__(self):
  return self.name
