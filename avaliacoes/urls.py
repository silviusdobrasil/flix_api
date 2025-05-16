from django.urls import path
from avaliacoes import views

urlpatterns = [
   
    path('avaliacoes/', views.AvaliacaoCreateListView.as_view(), name='filmes'),
    path('avaliacoes/<int:pk>/', views.AvaliacaoRetrieveUpdateDestroyView.as_view(), name='avaliacoes-detail-view'),

]
