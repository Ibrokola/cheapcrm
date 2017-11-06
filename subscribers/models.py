from django.db import models
from django.contrib import auth
from django.contrib.auth.models import User
from django.conf import settings

from decouple import config

import stripe

# class UserNew(auth.models.User,auth.models.PermissionsMixin):
#     def __str__(self):
#         return self.username



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


    def charge(self, request, email, fee):
        #Set secret key
        stripe.api_key = settings.STRIPE_SECRET_KEY

        #Token transferred to stripe
        token = request.POST['stripeToken']

        #Create a Customer
        stripe_customer = stripe.Customer.create(
            card=token,
            description=email
        )

        # Save Stripe ID to customers profile
        self.stripe_id = stripe_customer.id
        self.save()

        #Charge customer instead of card
        stripe.Charge.create(
            amount=fee,
            currency="cad",
            customer=stripe_customer.id
        )
        return stripe_customer


