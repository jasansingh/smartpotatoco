from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.


class Health(models.Model):
    male = 'male'
    female = 'female'
    sex_choices = ((male, 'male'), (female, 'female'))
    user = models.ForeignKey(User)
    sex = models.CharField(max_length=2, choices=sex_choices)
    weight = models.IntegerField(max_length=3)
    height = models.IntegerField(max_length=5)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.user


class UserPicture(models.Model):
    user = models.ForeignKey(User)
    image = models.ImageField(upload_to='profiles/')
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    active = models.BooleanField(default=True)

    def __unicode__(self, ):
        return str(self.image)


class ReceiptImage(models.Model):
    user = models.ForeignKey(User)
    image = models.ImageField(upload_to='images/receipts')
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    active = models.BooleanField(default=True)

    def __unicode__(self, ):
        return str(self.image)






