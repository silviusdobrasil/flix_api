from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/', include('genero.urls')),
    path('api/v1/', include('filmes.urls')),
    path('api/v1/', include('atores.urls')),
    path('api/v1/', include('avaliacoes.urls')),

]
