from django.db.models import (
    Model,
    CharField, SlugField, ForeignKey, CASCADE,

)
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from django_resized import ResizedImageField

from apps.models.user import BaseModel


class Category(Model):
    name = CharField(_('category_name'), max_length=255)
    slug = SlugField(_('category_slug'), max_length=255, unique=True)
    image = ResizedImageField(_('category_image'), size=[168, 168], upload_to='category/images',
                              crop=['middle, center'])

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.name


class ProductImage(BaseModel):
    image = ResizedImageField(size=[1098, 717], null=True, blank=True)
    product = ForeignKey('apps.Product', CASCADE, 'categories')

    class Meta:
        verbose_name = 'Product_image'
        verbose_name_plural = 'Product_images'

    def __repr__(self):
        return self.product.name


class Product(BaseModel):
    name = CharField(_('product_name'), max_length=255)
    slug = SlugField(_('product_slug'), max_length=255, unique=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if force_update is True:
            self.slug = slugify(self.name)
        super().save(force_insert, force_update, using, update_fields)


class Order(BaseModel):
    pass
