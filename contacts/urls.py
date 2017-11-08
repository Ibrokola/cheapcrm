from django.conf.urls import url
from django.contrib.auth import views as auth_views
from .views import contact_detail 


urlpatterns = [
    # url(r'l/$', AccountList.as_view(), name='contact_list'),
    url(r'c/(?P<uuid>[\w-]+)/$', contact_detail, name='contact_detail'),
    # url(r'new/$', account_cru, name='account_new'),
    # url(r'edit/(?P<uuid>[\w-]+)/$', account_cru, name='account_update'),
]
