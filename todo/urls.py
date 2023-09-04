from django.urls import path
from . import views

urlpatterns = [
    path('', views.list),
    path('got_data/', views.got_data),
]