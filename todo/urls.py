from django.urls import path
from . import views

urlpatterns = [
    path('',views.list),
    path('create/', views.create),
    path('<int:todo_id>/', views.detail_read),
    path('delete/<int:todo_id>/', views.delete),
    path('edit/<int:todo_id>/',views.edit),
    path('myposts/',views.myposts),
    path('myprofile/',views.myprofile),
]