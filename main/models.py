from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='mediaImg/')
    image = models.ImageField(upload_to='mediaImg/', null=True, blank=True)
    about = models.TextField()
    location = models.URLField()
    phone_num = models.CharField(max_length=13)
    telegram = models.URLField()
    facebook = models.URLField()
    other = models.CharField(max_length=255, null=True, blank=True)


class Person(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='mediaImg/', null=True, blank=True)
    reason = models.TextField()
    phone_num = models.CharField(max_length=13)
    telegram = models.URLField()
    other_contact = models.CharField(max_length=255)
