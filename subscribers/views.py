from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.forms.forms import NON_FIELD_ERRORS
from django.conf import settings
from django.core.urlresolvers import reverse

from django.http import HttpResponseRedirect

import stripe


from django.views.generic import CreateView
from django.views.generic.edit import FormView
from django.views import View

from .forms import SubscriberForm
from .models import Subscriber



# class SubscriberNew(CreateView):
#     form_class = SubscriberForm
#     success_url = reverse_lazy('login')
#     template_name = 'subscribers/subscriber_new.html'


# class SubscriberNew(View):
#     form_class = SubscriberForm
#     success_url = reverse_lazy('login')
#     template_name = 'subscribers/subscriber_new.html'

#     def get(self, request, *args, **kwargs):
#         form = self.form_class()
#         return render(request, self.template_name, {'form':form})


def subscriber_new(request):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            #Unpacking form values
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            # Create the User record
            user = User(busername=username, email=email, first_name=first_name, last_name=last_name)
            user.set_password(password)
            user.save()

            # Create Subscriber Record
            address_one = form.cleaned_data['address_one']
            address_two = form.cleaned_data['address_two']
            city = form.cleaned_data['city']
            province = form.cleaned_data['province']
            sub = Subscriber(address_one=address_one, address_two=address_two, province=province, user_sub=user)
            sub.save()

            fee = settings.SUBSCRIPTION_PRICE
            try:
                stripe_customer = sub.charge(request, email, fee)
            except stripe.StripeError as e:
                form._errors[NON_FIELD_ERRORS] = form.error_class([e.args[0]])
                
                template='subscribers/subscriber_new.html'
                context = {
                    'form':form,
                    'STRIPE_PUBLISHABLE_KEY':settings.STRIPE_PUBLISHABLE_KEY}
                return render(request, template, context)
            a_u = authenticate(username=username, password=password)
            if a_u is not None:
                if a_u.is_active:
                    login(request, a_u)
                    return reverse_lazy('account_list')
                else:
                    return HttpResponseRedirect(reverse('subscribers:sub_new'))
            return reverse_lazy('login')
    else: form = SubscriberForm()
    

    template='subscribers/subscriber_new.html'
    context = {'form':form,'STRIPE_PUBLISHABLE_KEY':settings.STRIPE_PUBLISHABLE_KEY}

    return render(request,template,context)
