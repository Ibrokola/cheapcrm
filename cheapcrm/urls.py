from django.conf.urls import url, include
from django.contrib import admin

from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static
from marketing.views import HomePage

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'login/$',auth_views.login, {'template_name':'login.html'}, name='login'),
    url(r'login/$', auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    # url(r'logout/$', auth_views.logout, {'next_page':'/'}),
    url(r'logout/$', auth_views.LogoutView.as_view(template_name='logout.html'),name='logout'),
    url(r'^subscribe/', include('subscribers.urls',namespace='subscribers')),
    url(r'^accounts/',include('django.contrib.auth.urls')),
    url(r'^$', HomePage.as_view(), name='home')
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)