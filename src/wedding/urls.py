import autocomplete_light
autocomplete_light.autodiscover()

from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
import profiles.urls
import accounts.urls
import rsvp.urls
from . import views


urlpatterns = [
    url(r'^$', views.HomePage.as_view(), name='home'),
    url(r'^about/$', views.AboutPage.as_view(), name='about'),
    url(r'^autocomplete/', include('autocomplete_light.urls')),
    url(r'^users/', include(profiles.urls, namespace='profiles')),
    url(r'^rsvp/', include(rsvp.urls, namespace='rsvp')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(accounts.urls, namespace='accounts')),
    url(r'^static/(?P<path>.*)$',
        'django.views.static.serve',
        {'document_root': settings.STATIC_ROOT}),
    url(r'^media/(?P<path>.*)$',
        'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),
]

# User-uploaded files like profile pics need to be served in development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)