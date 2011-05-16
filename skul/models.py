from django.db import models
from django.contrib.auth.models import User

class Student(User):
    uovog = models.CharField(max_length = 40)
    regNumber = models.CharField(max_length = 10)
    ynemNumber = models.CharField(max_length = 9)
    address = models.CharField(max_length = 150)
    phone = models.IntegerField()
    
class Teacher(User):
    erdem_zereg = models.CharField(max_length = 20)
        
class NarBichig(User): 
    name = models.CharField(max_length = 20)
    
class NewsType(models.Model):
    typename  = models.CharField(max_length = 20)
    
class News(models.Model):
    code = models.CharField(max_length = 10)
    newstype  = models.ForeignKey(NewsType)
    content = models.TextField()
    NBName = models.CharField(max_length = 20)
    date = models.DateField()
    
class Uzleg(models.Model):
    name = models.CharField(max_length = 50)
    date = models.DateField()
    time = models.TimeField()
    score = models.IntegerField()
    commis = models.CharField(max_length = 50)
    room = models.IntegerField()
    shaardlaga = models.TextField()

class score(models.Model):
    uzleg  = models.ForeignKey(uzleg)
    student = models.ForeignKey(Student)
    score = models.IntegerField()
        
class SedevInfo(models.Model):
    name = models.CharField(max_length = 20)
    english_name = models.CharField(max_length = 30)
    shaardlaga = models.TextField()
    
class songoson_sedev(models.Model):
    sedev = models.ForeignKey(SedevInfo)
    tugsult_code = models.IntegerField()
    date = models.DateField()
    stu_year = models.CharField(max_length = 9)
    teacher = models.ForeignKey(Teacher)
    student = models.ForeignKey(Student)   

class tugsult_ajil(models.Model):
    code = models.IntegerField()
    sedev = models.ForeignKey(SedevInfo)
    student = models.ForeignKey(Student)
    teacher = models.ForeignKey(teacher)
    date = models.DateField()
    score = models.IntegerField()
    
class ansQue(models.Model):
    question = models.TextField()
    answer = models.TextField(null=True)
    date = models.DateField()
    user = models.ForeignKey(Student)

class IP(models.Model):
    ip = models.CharField(max_length = 20)
    port = models.IntegerField()
    key = models.CharField(max_length = 100)
