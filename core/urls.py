from django.contrib import admin
from django.urls import path,include
from rest_framework_swagger.views import get_swagger_view
from core.yasg import urlpatterns as doc_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/",include("api.urls")),
]

urlpatterns += doc_urls