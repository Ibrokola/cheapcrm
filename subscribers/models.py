from django.db import models
from django.contrib import auth
from django.contrib.auth.models import User


class UserNew(auth.models.User,auth.models.PermissionsMixin):
    def __str__(self):
        return self.username



class Subscriber(models.Model):
    user_sub = models.ForeignKey(User)
    address_one = models.CharField(max_length=100)
    address_two = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=50)
    province = models.CharField(max_length=2)
    stripe_id = models.CharField(max_length=30, blank=True)

    class Meta:
        verbose_name_plural = 'subscribers'

    def __str__(self):
        return u"%s's Subscription Info" % self.user_sub