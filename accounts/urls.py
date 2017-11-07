from django.conf.urls import url
from django.contrib.auth import views as auth_views
from .views import AccountList, account_detail


urlpatterns = [
    url(r'list/$', AccountList.as_view(), name='account_list'),
    url(r'p/(?P<uuid>[\w-]+)/$', account_detail, name='account_detail'),
]
