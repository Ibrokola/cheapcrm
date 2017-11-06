from django.conf.urls import url
from django.contrib.auth import views as auth_views
from .views import subscriber_new


urlpatterns = [
    # url(r'login/$', auth_views.LoginView.as_view(template_name='accounts/login.html'),name='login'),
    # url(r'logout/$', auth_views.LogoutView.as_view(),name='logout'),
    url(r'signup/$', subscriber_new, name='sub_new')
]
