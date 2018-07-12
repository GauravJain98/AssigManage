from django.db import models
from django.contrib.auth.models import User

##
class Custom_User(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.OneToOneField(
        User,
        on_delete = models.CASCADE
    )

class Branch(models.Model):
    #DO NOT CONNECT SYLLABUS TO BRANCH BUT TO C_CLASS
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    branch = models.CharField(max_length=20,null=False,blank=False)
    

class c_class(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    branch = models.ForeignKey(
        Branch,
        null=False,
        blank = False,
        on_delete = models.CASCADE
    )
    year = models.CharField(max_length=4,null=False,blank=False)

class Teacher(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.OneToOneField (
        Custom_User,
        on_delete=models.CASCADE,
    )

class Subject(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=30)
    code =  models.CharField(max_length=6)

class Teaches(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    teacher =  models.ForeignKey(
        Teacher,
        null=False,
        blank=False,
        on_delete = models.CASCADE
    )
    subject = models.ForeignKey(
        Subject,
        null=False,
        blank=False,
        on_delete = models.CASCADE
    )
    c_class = models.ForeignKey(
        c_class,
        null=False,
        blank=False,
        on_delete = models.CASCADE
    )

class Student(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.OneToOneField(
        User,
        on_delete = models.CASCADE
    )
    rollno = models.CharField(max_length=11,null=False,blank=False)
    c_class = models.ForeignKey(
        c_class,
        null=False,
        blank=False,
        on_delete = models.CASCADE
    )

class Assignment(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deadline = models.DateTimeField(auto_now=True)
    c_class = models.ForeignKey(
        c_class,
        null=False,
        blank=False,
        on_delete = models.CASCADE
    )
    teaches = models.ForeignKey(
        Teaches,
        null=False,
        blank=False,
        on_delete = models.CASCADE
    )

class Submission(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    student = models.ForeignKey(
        Student,
        null=False,
        blank=False,
        on_delete = models.CASCADE
    )
    assignment = models.ForeignKey(
        Assignment,
        null=False,
        blank=False,
        on_delete = models.CASCADE
    )
