from django.db import models
from django.contrib.auth.models import User

from accounts.models import Account

from shortuuidfield import ShortUUIDField

from django.urls import reverse


class Contact(models.Model):
    uuid = ShortUUIDField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField()
    account = models.ForeignKey(Account)
    owner = models.ForeignKey(User)
    created_on = models.DateField(auto_now_add=True)


    class Meta:
        verbose_name_plural = 'contacts'

    @property
    def full_name(self):
        return u'%s %s' % (self.first_name, self.last_name)

    def __str__(self):
        return u'%s' % self.full_Name
    
    def get_absolute_url(self):
        return reverse('contact:contact_detail', args=[self.uuid])


    def get_update_url(self):
        return reverse('contact:contact_update', args=[self.uuid])


    def get_delete_url(self):
        return reverse('contact:contact_delete', args=[self.uuid])

