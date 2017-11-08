from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from .models import Contact
from .forms import ContactForm


@login_required()
def contact_cru(request):
    
    if request.POST:
        form = ContactForm(request.POST)
        if form.is_valid():
            # make sure the user owns the account
            account = form.cleaned_data['account']
            if account.owner != request.user:
                return HttpResponseForbidden()

            contact = form.save(commit=False)
            contact.owner = request.user
            contact.save()
            # return the user to the account detail view
            reverse_url = reverse(
                'accounts:account_detail', args=(account.uuid,)
            )
            return HttpResponseRedirect(reverse_url)
    else:
        form = ContactForm()

    context ={
        'form': form,
    }
    template = 'contacts/contact_cru.html'

    return render(request, template, context)















@login_required()
def contact_detail(request, uuid):

    contact = Contact.objects.get(uuid=uuid)

    template = 'contacts/contact_detail.html'
    context = {
        'contact': contact
    }

    return render(request, template, context)