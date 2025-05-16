from django.urls import path
from filmes import views

urlpatterns = [
   
    path('filmes/', views.FilmesCreateListView.as_view(), name='filmes'),
    path('filmes/<int:pk>/', views.FilmesRetrieveUpdateDestroyView.as_view(), name='filmes-detail-view'),
    path('filmes/stats/', views.filmeStatsView.as_view(), name='filmes-stats-view'),

]
