from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('exercise/', views.ExerciseList.as_view(), name='exercise_list'),
    path('exercise/<int:pk>', views.ExerciseDetail.as_view(), name='exercise_detail'),
    path('user/', views.UserList.as_view(), name='user_list'),
    path('user/<int:pk>', views.UserDetail.as_view(),
         name='user_detail'),
]
