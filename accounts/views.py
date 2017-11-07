from django.shortcuts import render
from django.http import HttpResponseForbidden,Http404,HttpResponseRedirect 

from django.core.urlresolvers import reverse
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .forms import AccountForm
from .models import Account



class AccountList(ListView):
    model = Account
    paginate_by = 12
    template_name = 'accounts/account_list.html'
    context_object_name = 'accounts'

    def get_queryset(self):
        try:
            a = self.request.GET.get('account',)
        except KeyError:
            a = None
        if a:
            account_list = Account.objects.filter(
                name__icontains=a, 
                owner=self.request.user
        )
        else:
            account_list = Account.objects.filter(owner=self.request.user)
        return account_list

    @method_decorator(login_required)
    def dispatch(self,*args,**kwargs):
        return super(AccountList, self).dispatch(*args, **kwargs)


@login_required()
def account_detail(request, uuid):

    account = Account.objects.get(uuid=uuid)
    if account.owner != request.user:
        return HttpResponseForbidden()
    
    template = 'accounts/account_detail.html'
    context ={
        'account': account,
    }
    return render(request, template, context)

@login_required()
def account_cru(request):
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            account = form.save(commit=False)
            account.owner = request.user
            account.save()
            redirect_url = reverse(
                'accounts:account_detail', args=(account.uuid)
            )
            return HttpResponseRedirect(redirect_url)
    else:
        form = AccountForm()

    context = {
        'form': form,
    }
    template = 'accounts/account_cru.html'

    return render(request, template, context)