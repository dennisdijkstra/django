from django.urls import path
from . import views

urlpatterns = [
    path('', views.createUser),
    path('<int:id>/', views.getUser),
    path('<int:id>/', views.updateUser),
    path('<int:id>/', views.deleteUser),
]