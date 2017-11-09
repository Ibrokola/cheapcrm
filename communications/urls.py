from django.conf.urls import url
from django.contrib.auth import views as auth_views
from .views import comm_cru, comm_detail 


urlpatterns = [
    url(r'new/$', comm_cru, name='comm_new'),
    url(r'd/(?P<uuid>[\w-]+)/$', comm_detail, name='comm_detail'),
    # url(r'c/(?P<uuid>[\w-]+)/$', contact_detail, name='contact_detail'),
    url(r'edit/(?P<uuid>[\w-]+)/$', comm_cru, name='comm_update'),
    # url(r'c/delete/(?P<pk>[\w-]+)/$', ContactDelete.as_view(), name='contact_delete'),
]
