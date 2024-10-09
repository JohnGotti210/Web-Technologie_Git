from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('startseite.urls')),  # Hier wird die App `katastrophen` hinzugefügt
]
