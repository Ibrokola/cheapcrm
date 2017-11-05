from django.conf.urls import url
from django.contrib.auth import views as auth_views
from .views import SubscriberNew


urlpatterns = [
    # url(r'login/$', auth_views.LoginView.as_view(template_name='accounts/login.html'),name='login'),
    # url(r'logout/$', auth_views.LogoutView.as_view(),name='logout'),
    url(r'signup/$', SubscriberNew.as_view(template_name='subscribers/subscriber_new.html'),name='sub_new')
]
