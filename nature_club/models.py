from os import times
from django.db import models
from django.db.models.manager import ManagerDescriptor

# Create your models here.


class Articles(models.Model):
    Articla_name = models.CharField(max_length=100)


class Gallery(models.Model):
    Images = models.FileField(upload_to= 'gallery')

class Events(models.Model):
    Title = models.CharField(max_length=100)
    description = models.TextField()
    Images = models.FileField(upload_to= 'events')

    def __str__(self):
        return self.Title


class LeaderShip(models.Model):
    Name = models.CharField(max_length=100)
    Position = models.CharField(max_length=100)
    Images = models.FileField(upload_to= 'events')

    def __str__(self):
        return self.Name


class Contact(models.Model):
    Email = models.EmailField()
    Phone = models.CharField(max_length=100)
    Name = models.CharField(max_length=100)
    Message = models.TextField()

    def __str__(self):
        return self.Email
    
class Team(models.Model):
    Images = models.FileField(upload_to= 'Team')
    Position = models.CharField(max_length=100)
    Name = models.CharField(max_length=100)
    Description = models.TextField()

    def __str__(self):
        return self.Name

class Slider(models.Model):
    Full_image = models.FileField(upload_to= 'Slider')
    Small_image = models.FileField(upload_to= 'Slider')
    title = models.CharField(max_length=100)
    Description = models.TextField()

    def __str__(self):
        return self.title

class Activities(models.Model):
    Images = models.FileField(upload_to= 'Slider')
    title = models.CharField(max_length=100)
    Description = models.TextField()

    def __str__(self):
        return self.title
