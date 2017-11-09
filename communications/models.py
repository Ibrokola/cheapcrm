from django.db import models
from django.contrib.auth.models import User

from accounts.models import Account
from shortuuidfield import ShortUUIDField

from django.urls import reverse


TYPE_LIST = (
        (1, 'Meeting'),
        (2, 'Phone'),
        (3, 'Email'),
    )

class Communication(models.Model):
    uuid = ShortUUIDField(unique=True)
    subject = models.CharField(max_length=50)
    notes = models.TextField()
    kind = models.PositiveSmallIntegerField(choices=TYPE_LIST)
    date = models.DateField()
    owner = models.ForeignKey(User)
    account = models.ForeignKey(Account)
    created_on = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'communications'


    def __str__(self):
        return u"%s" % self.subject
    
    def get_absolute_url(self):
        return reverse('comm:comm_detail', args=[self.uuid])


    def get_update_url(self):
        return reverse('comm:comm_update', args=[self.uuid])


    def get_delete_url(self):
        return reverse('comm:comm_delete', args=[self.id])

