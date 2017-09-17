from django.conf.urls import patterns, include, url
from django.contrib import admin
from book_gallery.settings import ROOT_URL


def root_url_processor(request):
    return {'ROOT_URL': ROOT_URL}

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls), name=admin),
                       url(r'^', include('gallery.urls')),
                       )
