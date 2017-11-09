from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.http import HttpResponseForbidden

from .models import Communication
from .forms import CommunicationForm





@login_required()
def comm_cru(request):
    
    if request.POST:
        form = CommunicationForm(request.POST)
        if form.is_valid():
            #make sure the user owns the account
            account = form.cleaned_data['account']
            if account.owner != request.user:
                return HttpResponseForbidden()

            # save the data
            comm = form.save(commit=False)
            comm.owner = request.user
            comm.save()
            # return the user to the account detail view
            reverse_url = reverse('accounts:account_detail.html', args=(account.uuid,))
            return HttpResponseRedirect(reverse_url)
    else:
        form = CommunicationForm()

    context = {
        'form': form,
    }
    template = 'communications/comm_cru.html'

    return render(request, template, context)




@login_required()
def comm_detail(request, uuid):
    
    comm = Communication.objects.get(uuid=uuid)
    if comm.owner != request.user:
        return HttpResponseForbidden()
    template = 'communications/comm_detail.html'
    context = {'comm':comm}
    return render(request, template, context)