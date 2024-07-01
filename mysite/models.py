from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=32)
    descriptionm = models.TextField()


class Professor(models.Model):
    user = models.CharField(max_length=32, unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    bio = models.TextField()


class Student(models.Model):
    user = models.CharField(max_length=32, unique=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    enrollment_date = models.DateTimeField()
    graduation_date = models.DateTimeField()


class Cours(models.Model):
    name = models.CharField(max_length=32)
    code = models.PositiveSmallIntegerField()
    description = models.TextField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    price = models.PositiveSmallIntegerField()
