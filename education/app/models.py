from django.db import models
# Create your models here.

class student(models.Model):
    user_name=models.CharField(max_length=20)
    password1=models.CharField(max_length=25)
    email=models.EmailField()

class courses(models.Model):
    course_name=models.CharField(max_length=25)
    course_image=models.ImageField(upload_to='course/cover/',null=True,blank=True)
    course_description=models.TextField()


class courseregistration(models.Model):
    phoneno=models.IntegerField()
    email=models.EmailField()
    coursename=models.CharField(max_length=20)
    user_id=models.IntegerField()


    