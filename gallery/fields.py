# coding:utf-8
from django.db.models.fields.files import ImageField, ImageFieldFile
from PIL import Image  # PIL: Python Image Library
import os


def _add_thumb(s):
    """
    Modifies a string(filename, URL) containing an image filename to insert
    '.thumb' before the file extension (which is changed to be '.jpg'
    """
    parts = s.split(".")
    parts.insert(-1, "thumb")
    if parts[-1].lower() not in ['jpg', 'jpeg']:
        parts[-1] = 'jpg'
    return ".".join(parts)  # join()用法 'sep'.join(seq)


class ThumbnailImageFieldFile(ImageFieldFile):
    def _get_thumb_path(self):
        return _add_thumb(self.path)
    thumb_path = property(_get_thumb_path)

    def _get_thumb_url(self):
        return _add_thumb(self.url)
    thumb_url = property(_get_thumb_url)

    def save(self, name, content, save=True):
        super(ThumbnailImageFieldFile, self).save(name, content, save)
        img = Image.open(self.path)
        img.thumbnail(
            (self.field.thumb_width, self.field.thumb_height),
            Image.ANTIALIAS
        )
        img.save(self.thumb_path, "JPEG")

    def delete(self, save=True):
        if os.path.exists(self.thumb_path):
            os.remove(self.thumb_path)
        super(ThumbnailImageFieldFile, self).delete(save)  # 删除原图


class ThumbnailImageFiled(ImageField):
    attr_class = ThumbnailImageFieldFile

    def __init__(self, thumb_width=400, thumb_height=320, *args, **kwargs):
        self.thumb_width = thumb_width
        self.thumb_height = thumb_height
        super(ThumbnailImageFiled, self).__init__(*args, **kwargs)
