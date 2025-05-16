from django.db.models import Count, Avg
from rest_framework import generics, views, response, status
from rest_framework.permissions import IsAuthenticated
from filmes.models import Filmes
from filmes.serializers import FilmesSerializer, FilmeDetalheSerializer
from app.permissions import GlobalDefaultPermission
from avaliacoes.models import Avaliacoes

class FilmesCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Filmes.objects.all()

    def get_serializer_class(self):

        if self.request.method == 'GET':
            return FilmeDetalheSerializer
        
        return FilmesSerializer

class FilmesRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Filmes.objects.all()
    def get_serializer_class(self):

        if self.request.method == 'GET':
            return FilmeDetalheSerializer
    
        return FilmesSerializer

class filmeStatsView(views.APIView):
     permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
     queryset = Filmes.objects.all()


     def get(self, request):
         
         total_filmes = self.queryset.count()
         filmes_por_genero = self.queryset.values('genero__nome').annotate(total=Count('id'))
         total_avaliacoes = Avaliacoes.objects.count()
         media_avaliacoes = Avaliacoes.objects.aggregate(avg_nota=Avg('nota'))['avg_nota']

         data = {
                    'total_filmes': total_filmes,
                    'filmes_por_genero': filmes_por_genero,
                    'total_avaliacoes': total_avaliacoes,
                    'media_avaliacoes': round(media_avaliacoes, 1)  if media_avaliacoes else 0,
             },

         return response.Response(
             data=data,
             
             status=status.HTTP_200_OK,
             
         )
