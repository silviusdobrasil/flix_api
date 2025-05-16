from django.urls import path
from genero import views

urlpatterns = [
   
    path('genero/', views.GenereCreateListView.as_view(), name='genero'),
    path('genero/<int:pk>/', views.GeneroRetrieveUpdateDestroyView.as_view(), name='genero-detail-view'),

]
