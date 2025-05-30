"""LearningDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Add Django site authentication urls (for login, logout, password management)
    path('', views.index, name="index"),
    path('service-worker.js', views.service_worker_js),
    path('firebase-messaging-sw.js', views.firebase_messaging_sw_js),
    path('accounts/', include('django_registration.backends.activation.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls'), name='accounts'),
    path('digitaldairy/', include('digitaldairy.urls'), name="digitaldairy"),
    path('digitaldairyApi/', include('digitalDairyApi.urls'), name="digitaldairyApi"),
    path('admin/', admin.site.urls),
    path('fodder-calculator/', views.fodder_calculator, name='fodder-calculator'),
    path('test/', views.test, name='test'),
    path('dashboard/', views.dashboard, name='back_to_dashboard'),
    path('', include('fodder_marketplace.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)