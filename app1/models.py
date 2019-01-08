from django.db import models

class StudentModel(models.Model):
    eid=models.IntegerField()
    ename=models.CharField(max_length=45)
    esal=models.IntegerField()

