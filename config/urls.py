from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


admin.site.site_header = "Back admin"
admin.site.site_title = "Muhammadnurning sahifasi"
admin.site.index_title = "Welcome Aziz"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('products.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
