from django.conf.urls import patterns, url

from .views import rsvp, person, song

urlpatterns = [
    url(r'^$', rsvp, name='rsvp'),
    url(r'^song/$', song, name='song'),
    url(r'^person/(?P<name>.*)$', person, name='person'),
    #url(r'^group$', group, name='group'),
]
