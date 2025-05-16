from django.urls import path
from atores import views

urlpatterns = [
   
    path('atores/', views.AtoresCreateListView.as_view(), name='atores'),
    path('atores/<int:pk>/', views.AtoresRetrieveUpdateDestroyView.as_view(), name='atores-detail-view'),

]
