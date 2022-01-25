from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),    # url to admin dashboard
    path('api/', include('api.urls')),  # including api(app) urls
]
