from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    category = models.CharField(max_length=200)

    def __str__(self):
        return self.category
    

class Question(models.Model):
    choice = models.ForeignKey(Category, on_delete=models.CASCADE)
    question = models.CharField(max_length=250)
    answer = models.CharField(max_length=100)
    option_one = models.CharField(max_length=100)
    option_two = models.CharField(max_length=100)
    option_three = models.CharField(max_length=100, blank=True)
    option_four = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question

class Course(models.Model):
    titile = models.CharField(max_length=50)
    details = models.TextField(max_length=500)
    cost = models.IntegerField(max_length=5)
    offered_by = models.CharField(max_length=200)
    course_pic = models.ImageField(upload_to='course_image')
    def __str__(self) -> str:
        return self.titile



