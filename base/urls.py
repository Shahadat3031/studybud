from django.urls import path
from .import views

# This all are the urls that will be used in the project [1]    


urlpatterns = [
    path('', views.home, name='home'),
    path('room/<str:pk>', views.room, name='room'),
    path('about/', views.about, name='about'), 
]

