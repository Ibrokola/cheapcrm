from django.conf.urls import url
from django.contrib.auth import views as auth_views
from .views import subscriber_new


urlpatterns = [
    url(r'signup/$', subscriber_new, name='sub_new')
]
