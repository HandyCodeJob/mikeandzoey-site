from django.conf.urls import patterns, url

from .views import rsvp, person

urlpatterns = [
    url(r'^$', rsvp, name='rsvp'),
    url(r'^person/(?P<name>.*)$', person, name='person'),
    #url(r'^group$', group, name='group'),
]
