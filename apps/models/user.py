from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from django.db.models import (
    Model,
    DateTimeField,
    CharField,
    TextChoices,
    TextField
)
from django_resized import ResizedImageField


class BaseModel(Model):
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    def created_at_product(self):
        return self.created_at.strftime('%d.%m.%Y')

    class Meta:
        abstract = True


class User(AbstractUser):
    class UserType(TextChoices):
        ADMIN = 'admin', 'Admin'
        CURRIER = 'currier', 'Currier'
        DEFAULT = 'default', 'Default'
        OPERATOR = 'operator', 'OPERATOR'
        MANAGER = 'manager', 'Manager'

    type = CharField(_('user_type'), max_length=20, choices=UserType.choices, default=UserType.DEFAULT)
    phone = CharField(max_length=25, unique=True, validators=[
        RegexValidator(regex=r'^\d{12}$',
                       message="Phone number must be entered in the format: '999999999'. Up to 15 digits allowed.")])
    bio = TextField(max_length=1024, blank=True, null=True)
    avatar = ResizedImageField(_('user_avatar'), size=[168, 168], crop=['middle', 'center'], upload_to='users/images',
                               null=True, blank=True, default='users/default_user.jpg')
    banner = ResizedImageField(_('user_banner'), size=[1198, 124], upload_to='users/images', null=True, blank=True,
                               default='users/default_banner.jpg')

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')
