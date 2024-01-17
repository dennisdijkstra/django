from django.urls import path
from . import views

urlpatterns = [
  path('', views.UserList.as_view()),
  path('<int:id>/', views.UserDetail.as_view()),
]