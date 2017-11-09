from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from django.utils.decorators import method_decorator

from django.views.generic import DeleteView

from .models import Contact
from .forms import ContactForm

from accounts.models import Account






class ContactMixin(object):
    model = Contact

    def get_context_data(self, **kwargs):
        kwargs.update({'object_name':'Contact'})
        return kwargs

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ContactMixin, self).dispatch(*args, **kwargs)


@login_required()
def contact_cru(request, uuid=None, account=None):
    
    #if the contact object already exists
    if uuid:
        contact = get_object_or_404(Contact, uuid=uuid)
        # Contacts can only be accessed by account owner
        if contact.owner != request.user:
            return HttpResponseForbidden()
    else:
        contact = Contact(owner=request.user)


    if request.POST:
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            # make sure the user owns the account
            account = form.cleaned_data['account']
            if account.owner != request.user:
                return HttpResponseForbidden()
            # save the data
            contact = form.save(commit=False)
            contact.owner = request.user
            contact.save()
            # form.save()
            # return the user to the account detail view
            if request.is_ajax():
                return render(request, 'contacts/contact_item_view.html', {'account':account, 'contact':contact})
            else:
                reverse_url = reverse(
                    'accounts:account_detail', args=(account.uuid,)
                )
                return HttpResponseRedirect(reverse_url)
        else:
            # If the form isn't valid, still fetch the account so it can be passed into the template
            account = form.cleaned_data['account']
    else:
        form = ContactForm(instance=contact)

    # this fetches the account if it exists as a URL parameter
    if request.GET.get('account', ''):
        account = Account.objects.get(id=request.GET.get('account', ''))

    context ={
        'form': form,
        'contact': contact,
        'account': account
    }

    if request.is_ajax():
        template = 'contacts/contact_item_form.html'
    else:
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


class ContactDelete(ContactMixin, DeleteView):
    template_name = 'object_confirm_delete.html'

    def get_object(self, queryset=None):
        obj = super(ContactDelete, self).get_object()
        if not obj.owner == self.request.user:
            raise Http404
        # Specifies which account the contact being deleted is related to
        account = Account.objects.get(id=obj.account.id,)
        self.account = account
        return obj

    def get_success_url(self):
        return reverse(
            'accounts:account_detail', args=(self.account.uuid,)
        )