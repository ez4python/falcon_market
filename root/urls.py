from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include
from django.utils.translation import gettext_lazy as _
from django.views.i18n import set_language

urlpatterns = i18n_patterns(
    path(_('admin/'), admin.site.urls),
    path('set_language/', set_language, name='set_language'),
    # path('', include('apps.urls')),
)
