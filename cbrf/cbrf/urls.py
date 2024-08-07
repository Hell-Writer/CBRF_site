from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('auth/', include('users.urls')),
    path('auth/', include('django.contrib.auth.urls')),
    path('api/v1/', include('api.urls')),
    path('', include('companies.urls', namespace='companies')),
]
