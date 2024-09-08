from . import views
from django.urls import path

urlpatterns = [
    path('buy/<int:id>/', views.buy_book, name='buy_book'), 
    path('profile_history/', views.profile_history, name='profile_history'),
]

