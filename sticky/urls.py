from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from django.views.generic import ListView

from app.models import *

urlpatterns = patterns('',
    url(r'^$', ListView.as_view(model=Note), name='list_note'),
    url(r'^admin/', include(admin.site.urls)),
)
