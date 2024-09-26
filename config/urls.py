from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from debug_toolbar.toolbar import debug_toolbar_urls



admin.site.site_header = "Back admin"
admin.site.site_title = "Muhammadnurning sahifasi"
admin.site.index_title = "Welcome Aziz"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('', include('products.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += debug_toolbar_urls()
