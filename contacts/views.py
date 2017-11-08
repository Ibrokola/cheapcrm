from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Contact



@login_required()
def contact_detail(request, uuid):

    contact = Contact.objects.get(uuid=uuid)

    template = 'contacts/contact_detail.html'
    context = {
        'contact': contact
    }

    return render(request, template, context)