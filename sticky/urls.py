from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from app.models import *
from app.views import *

urlpatterns = patterns('',
    url(r'^$', NoteListView.as_view(), name='list_note'),
    url(r'^admin/', include(admin.site.urls)),
)
