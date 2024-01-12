from django.urls import path
from . import views

urlpatterns = [
    path('/', views.getUsers) ,
    path('/<int:id>', views.updateUser) ,
    path('/<int:id>', views.deleteUser) ,
]