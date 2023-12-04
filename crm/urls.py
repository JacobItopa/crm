from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lead/', include("leads.urls", namespace='lead')),
]