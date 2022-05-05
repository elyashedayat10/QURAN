from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("account/", include("account.urls", namespace="account")),
    path("dirges/", include("dirges.urls", namespace="dirges")),
    path("praiseres/", include("praiseres.urls", namespace="praiseres")),
    path("natals/", include("natals.urls", namespace="natals")),
    path("translators/", include("translators.urls", namespace="translators")),
    path("qaris/", include("qari.urls", namespace="qaris")),
    path("quran/", include("quran.urls", namespace="quran")),
    path("", include("userfacilities.urls", namespace="facilities")),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', include('config.urls', namespace='config')),

]
if settings.DEBUG:
    # ADD ROOT MEDIA FILES
    urlpatterns = urlpatterns + static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
    urlpatterns = urlpatterns + static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )
