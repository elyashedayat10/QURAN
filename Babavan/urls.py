from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

if settings.DEBUG:
    urlpatterns = [
        path("admin/", admin.site.urls),
        path("account/", include("account.urls", namespace="account")),
        path("dirges/", include("dirges.urls", namespace="dirges")),
        path("praiseres/", include("praiseres.urls", namespace="praiseres")),
        path("natals/", include("natals.urls", namespace="natals")),
        path("translators/", include("translators.urls", namespace="translators")),
        path("qaris/", include("qari.urls", namespace="qaris")),
        path("", include("userfacilities.urls", namespace="facilities")),

    ]
    # ADD ROOT MEDIA FILES
    urlpatterns = urlpatterns + static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
    urlpatterns = urlpatterns + static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )
