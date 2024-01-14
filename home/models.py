
from __future__ import unicode_literals
from django.db import models
from login.models import User
from login.models import Shop, Client
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.conf import settings
from django.utils.text import slugify
from django.urls import reverse

    
class Post(models.Model):
    post = models.CharField(max_length=500)
    image = models.ImageField(upload_to='homepage/%Y/%m/%d',null=True, blank=True)#models.URLField(max_length=350, blank=True)
    imagedescription = models.CharField(max_length=500, blank=True)

    image1 = models.ImageField(upload_to='homepage/%Y/%m/%d',null=True, blank=True)
    imagedescription1 = models.CharField(max_length=500, blank=True)
    post1 = models.CharField(max_length=500, blank=True)

    image2 = models.ImageField(upload_to='homepage/%Y/%m/%d',null=True, blank=True)
    imagedescription2 = models.CharField(max_length=500, blank=True)
    post2 = models.CharField(max_length=500,blank=True)

    def __str__(self):
        return self.post


class Homepage(models.Model):
    title = models.CharField(max_length=120, default='')
    content = models.TextField(max_length=800,blank=True, default='')
    image = models.ImageField(upload_to='homepage/%Y/%m/%d',null=True, blank=True)

    title1 = models.CharField(max_length=500, default='')
    content1 = models.TextField(max_length=700, blank=True, default='')
    image1 = models.ImageField(upload_to='homepage/%Y/%m/%d',null=True, blank=True)

    title2 = models.CharField(max_length=500, default='')
    content2 = models.TextField(max_length=700, blank=True, default='')
    image2 = models.ImageField(upload_to='homepage/%Y/%m/%d',null=True, blank=True)
 
    def __str__(self):
        return self.title

class Newsletter(models.Model):
    email = models.EmailField(max_length=200)

    def __str__(self):
        return self.email



#contact mmodel helps clients and shops to contact Favourite
class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=200)
    content = models.TextField(max_length=300)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

#privacy model
class Privacy(models.Model):
    title = models.CharField(max_length=55, default='')
    text = models.TextField(max_length=7000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Terms(models.Model):
    title = models.CharField(max_length=55, default='')
    text = models.TextField(max_length=100000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

#about

class Aboutpage(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(max_length=700,blank=True)
    image = models.ImageField(upload_to='aboutpage/%Y/%m/%d', blank=True)
    image1 = models.ImageField(upload_to='aboutpage/%Y/%m/%d', blank=True)

    ourvision = models.TextField(max_length=500, blank=True)

    ourmission = models.TextField(max_length=500, blank=True)

    expertteam = models.TextField(max_length=500, blank=True)
    teammember1 = models.ImageField(upload_to='aboutpage/%Y/%m/%d', blank=True)
    teammember2 = models.ImageField(upload_to='aboutpage/%Y/%m/%d', blank=True)
    teammember3 = models.ImageField(upload_to='aboutpage/%Y/%m/%d', blank=True)

    communityengagement = models.TextField(max_length=500, blank=True)
    communityimage = models.ImageField(upload_to='aboutpage/%Y/%m/%d', blank=True)

    qualityandsafety = models.TextField(max_length=500, blank=True)

    yourtrusted = models.TextField(max_length=500, blank=True)


   

    def __str__(self):
        return self.title

        

class Aboutpagee(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(max_length=700,blank=True)
    image = models.ImageField(upload_to='aboutpage/%Y/%m/%d', blank=True)
    image1 = models.ImageField(upload_to='aboutpage/%Y/%m/%d', blank=True)

    ourvision = models.TextField(max_length=500, blank=True)

    ourmission = models.TextField(max_length=500, blank=True)

    expertteam = models.TextField(max_length=500, blank=True)
    teammember1 = models.ImageField(upload_to='aboutpage/%Y/%m/%d', blank=True)
    teammember2 = models.ImageField(upload_to='aboutpage/%Y/%m/%d', blank=True)
    teammember3 = models.ImageField(upload_to='aboutpage/%Y/%m/%d', blank=True)

    communityengagement = models.TextField(max_length=500, blank=True)
    communityimage = models.ImageField(upload_to='aboutpage/%Y/%m/%d', blank=True)

    qualityandsafety = models.TextField(max_length=500, blank=True)

    yourtrusted = models.TextField(max_length=500, blank=True)

   

    def __str__(self):
        return self.title
