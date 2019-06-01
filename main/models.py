from django.db import models

class User(models.Model):
  firstName = models.CharField(max_length=255, null=True, blank=True)
  lastName = models.CharField(max_length=255, null=True, blank=True)
  email = models.CharField(max_length=255, null=True, blank=True)
  password = models.CharField(max_length=255, null=True, blank=True)
  createdAt = models.DateTimeField(auto_now_add=True, null=True, blank=True)
  updatedAt = models.DateTimeField(auto_now=True, null=True, blank=True)

class Note(models.Model):
  name = models.CharField(max_length=255, null=True, blank=True)
  email = models.CharField(max_length=255, null=True, blank=True)
  message = models.TextField(null=True, blank=True) 
  createdAt = models.DateTimeField(auto_now_add=True, null=True, blank=True)
  updatedAt = models.DateTimeField(auto_now=True, null=True, blank=True)