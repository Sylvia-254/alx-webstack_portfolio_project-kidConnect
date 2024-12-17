from django.db import models

# Create your models here.
class Report(models.Model):
    """a table to store details of all reported children"""
    firstName = models.CharField(max_length=256)
    middleName = models.CharField(max_length=256)
    lastName = models.CharField(max_length=256)
    email = models.EmailField()
    gender = models.CharField(max_length=20)
    age = models.IntegerField()
    height = models.IntegerField()
    skinTone = models.CharField(max_length=50)
    location = models.CharField(max_length=256)
    dressing = models.TextField()
    profilePhoto = models.ImageField(upload_to='media/reportedChilderen', default="/media/parent-wife-child.png")
    status = models.CharField(max_length=256, default='pending')

    def __str__(self):
        return f"{self.firstName } {self.lastName}"