from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from leads.views import HomePageView
from django.contrib.auth.views import LoginView, LogoutView
from leads.views import SignUpView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", HomePageView.as_view(), name="homepage"),
    path('lead/', include("leads.urls", namespace='leads')),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("login/", LoginView.as_view(), name="login"),  
    path("signup/", SignUpView.as_view(), name="signup")
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)