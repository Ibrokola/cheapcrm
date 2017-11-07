from django.db import models
from django.contrib.auth.models import User

from shortuuidfield import ShortUUIDField

from django.urls import reverse




class Account(models.Model):
    uuid = ShortUUIDField(unique=True)
    name = models.CharField(max_length=80)
    desc = models.TextField(blank=True)
    address_one = models.CharField(max_length=100)
    address_two = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=50)
    province = models.CharField(max_length=2)
    phone = models.CharField(max_length=20)
    owner = models.ForeignKey(User)
    created_on = models.DateField(auto_now_add=True)


    class Meta:
        verbose_name_plural = 'accounts'


    def __str__(self):
        return u"%s" % self.name


    def get_absolute_url(self):
        return reverse('accounts:account_detail', args=[self.uuid])


    def get_update_url(self):
        return reverse('account_update', args=[self.uuid])

    def get_delete_url(self):
        return reverse('account_delete', args=[self.uuid])