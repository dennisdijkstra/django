from django.urls import path
from . import views

urlpatterns = [
    path('', views.userViews),
    path('<int:id>/', views.updateUser),
    path('<int:id>/', views.deleteUser),
]