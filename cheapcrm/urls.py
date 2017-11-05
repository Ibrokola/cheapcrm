from django.conf.urls import url, include
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static
from marketing.views import HomePage

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^subscribe/', include('subscribers.urls',namespace='subscribers')),
    url(r'^accounts/',include('django.contrib.auth.urls')),
    url(r'^$', HomePage.as_view(), name='home')
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)