from django.conf.urls import url
from django.contrib.auth import views as auth_views
from .views import AccountList, account_detail, account_cru


urlpatterns = [
    url(r'l/$', AccountList.as_view(), name='account_list'),
    url(r'p/(?P<uuid>[\w-]+)/$', account_detail, name='account_detail'),
    url(r'new/$', account_cru, name='account_new'),
    url(r'edit/(?P<uuid>[\w-]+)/$', account_cru, name='account_update'),
]
