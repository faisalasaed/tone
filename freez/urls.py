
from django.urls import path
from django.urls import path
from . import views

urlpatterns = [
    path('hot/', views.about, name='about'),  # ربط دالة العرض 'about' مع المسار '/hot/'
    path('', views.home, name='home'),  # ربط دالة العرض 'home' مع المسار '/'
]
