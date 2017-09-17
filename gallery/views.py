# coding:utf-8
from django.shortcuts import render, render_to_response
from django.views.generic import ListView, DetailView
from .models import Item, Photo


def index(request):
    return render_to_response("gallery/index.html")


class ItemList(ListView):
    model = Item  # 默认取Item中全部数据
    context_object_name = 'item_list'  # 模板中使用的变量
    template_name = 'gallery/items_list.html'

    def get_context_data(self, **kwargs):  # 必须要有，不然无返回数据，可以在模型基础上新增返回数据
        item_list = super(ItemList, self).get_context_data(**kwargs)
        return item_list


class ItemDetail(DetailView):
    model = Item
    context_object_name = 'item'
    template_name = 'gallery/items_detail.html'
    pk_url_kwarg = 'object_id'  # 必须添加

    def get_context_data(self, **kwargs):  # 必须要有，不然无返回数据，可以在模型基础上新增返回数据
        item_detail = super(ItemDetail, self).get_context_data(**kwargs)
        return item_detail


class PhotosDetail(DetailView):
    model = Photo
    context_object_name = 'photo'
    template_name = 'gallery/photos_detail.html'
    pk_url_kwarg = 'object_id'

    def get_context_data(self, **kwargs):  # 必须要有，不然无返回数据，可以在模型基础上新增返回数据
        photos_detail = super(PhotosDetail, self).get_context_data(**kwargs)
        return photos_detail

