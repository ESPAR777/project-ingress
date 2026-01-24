from django.contrib import admin
from django.urls import path
from Myapp.view import get_data  # Ensure 'Myapp' has a capital M

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/data/', get_data),
]