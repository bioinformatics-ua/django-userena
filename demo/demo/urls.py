from django.conf.urls import url, include
from django.conf import settings

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

from django.contrib import admin
from django.core.exceptions import ImproperlyConfigured

from profiles.views import promo

admin.autodiscover()

try:
    # django.VERSION < 2.0
    admin_urls = include(admin.site.urls)
except ImproperlyConfigured:
    admin_urls = admin.site.urls

urlpatterns = [
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', admin_urls),

    # Demo Override the signup form with our own, which includes a
    # first and last name.
    # (r'^accounts/signup/$',
    #  'userena.views.signup',
    #  {'signup_form': SignupFormExtra}),

    url(r'^accounts/', include('userena.urls')),
    url(r'^messages/', include('userena.contrib.umessages.urls')),
    url(r'^$', promo, name='promo'),
    url(r'^i18n/', include('django.conf.urls.i18n')),
]

# Add media and static files
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


