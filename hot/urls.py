from django.urls import path
from . import views

urlpatterns = [
    path('hot/', views.about, name='about'),  # المسار يشير إلى دالة العرض 'about'
]
