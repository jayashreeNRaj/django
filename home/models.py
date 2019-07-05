from django.db import models

# Create your models here.
class Student(models.Model):
    student_name=models.CharField('Student Names',max_length=30,null=True)
    dept=(
        ('CSE','Computer Science'),
        ('MH','Mech'),
        ('CV','Civil')
    )
    department=models.CharField('Department',choices=dept,blank=True,null=True,max_length=30)
    timestamp=models.DateTimeField(auto_now_add=True)
    usn=models.CharField("USN",max_length=12,null=True)
    def __str__(self):

        return self.student_name
 


class book(models.Model):
    book=models.CharField("Book",max_length=20,null=False)
    def __str__(self):
        return self.book
 

class Section(models.Model):
    advisor=models.OneToOneField('Teacher',on_delete=models.SET_NULL,null=True)
    students=models.ManyToManyField('Student',null=False)
    section=models.CharField('Section',max_length=30,null=False)
    def __str__(self):
        return self.section
 
class Teacher(models.Model):
    teacher=models.CharField("Teacher_name",max_length=40,null=False)
    timestamp=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.teacher

class library(models.Model):
    library_name=models.CharField("Library_name",max_length=100,null=False)
    books=models.ManyToManyField('book',null=True)
    def __str__(self):
        return self.library_name
 
 


