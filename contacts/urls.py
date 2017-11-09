from django.conf.urls import url
from django.contrib.auth import views as auth_views
from .views import contact_detail, contact_cru 


urlpatterns = [
    # url(r'l/$', AccountList.as_view(), name='contact_list'),
    url(r'c/new/$', contact_cru, name='contact_new'),
    url(r'c/(?P<uuid>[\w-]+)/$', contact_detail, name='contact_detail'),
    url(r'c/edit/(?P<uuid>[\w-]+)/$', contact_cru, name='contact_update'),
    # url(r'edit/(?P<uuid>[\w-]+)/$', account_cru, name='account_update'),
]
