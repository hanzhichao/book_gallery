from django.conf.urls import include, url, patterns
# from django.contrib import admin
from book_gallery.settings import ROOT_URL


# urlpatterns = [
#     url(r'^admin/', include(admin.site.urls)),
#     url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
# ]

urlpatterns = [
    url(r'^%s' % ROOT_URL[1:], include('book_gallery.real_urls')),
]
