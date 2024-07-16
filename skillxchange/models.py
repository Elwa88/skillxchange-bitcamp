from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=150,unique=True)
    is_admin = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False) 
    is_basic = models.BooleanField(default=True)
    def __str__(self):
        return f'{self.name} {self.last_name}'

class Skills(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    limit = models.IntegerField(default=10)
    tutor = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    current_students = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.title}'

class Enrollment(models.Model):
    skill = models.ForeignKey(Skills,on_delete=models.CASCADE)
    student = models.ForeignKey(CustomUser,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.student} {self.enrolled} {self.skill}'

class Review(models.Model):
    grades = [
        (1,1),
        (2,2),
        (3,3),
        (4,4),
        (5,5),
    ]
    skill = models.ForeignKey(Skills,on_delete=models.CASCADE)
    grade = models.IntegerField(choices=grades)
    
    def __str__(self):
        return f'{self.skill} - {self.grade}'