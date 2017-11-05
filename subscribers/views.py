from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView

from .forms import SubscriberForm



class SubscriberNew(CreateView):
    form_class = SubscriberForm
    success_url = reverse_lazy('login')
    template_name = 'subscribers/subscriber_new.html'



