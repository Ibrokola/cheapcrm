from django.conf.urls import url
from django.contrib.auth import views as auth_views
from .views import comm_cru 


urlpatterns = [
    url(r'new/$', comm_cru, name='comm_new'),
    # url(r'c/(?P<uuid>[\w-]+)/$', contact_detail, name='contact_detail'),
    # url(r'c/edit/(?P<uuid>[\w-]+)/$', contact_cru, name='contact_update'),
    # url(r'c/delete/(?P<pk>[\w-]+)/$', ContactDelete.as_view(), name='contact_delete'),
]
