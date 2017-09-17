from django.conf.urls import patterns, include, url
from book_gallery import settings
from django.contrib import admin
from gallery.views import index, ItemList, ItemDetail, PhotosDetail

urlpatterns = [
    url(r'^admin/', include(admin.site.urls), name='admin'),
   url(r'^$', index, name='index'),
   url(r'items/$', ItemList.as_view(), name='item_list'),
   url(r'items/(?P<object_id>\d+)/$', ItemDetail.as_view(), name='item_detail'),
   url(r'photos/(?P<object_id>\d+)/$', PhotosDetail.as_view(), name='photos_detail'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
]
