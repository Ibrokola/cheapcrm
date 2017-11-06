from django.conf.urls import url
from django.contrib.auth import views as auth_views
from .views import AccountList


urlpatterns = [
    url(r'list/$', AccountList.as_view(), name='account_list')
]
