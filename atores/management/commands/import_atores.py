# import csv
# from datetime import datetime
# from atores.models import Atores
# from django.core.management.base import BaseCommand


# class Command(BaseCommand):

#     def add_arguments(self, parser):
#         parser.add_argument(
#             'file_name', 
#             type=str, 
#             help='Nome do arquivo CSV a ser importado',
#     )

#     def handle(self, *args, **options):
#         file_name = options['file_name']

#         with open(file_name, 'r', encoding='utf-8') as file:
#             reader = csv.DictReader(file)
#             for row in reader:
#                 nome = row['nome']
#                 aniversario = datetime.strptime(row['aniversario'], '%Y-%m-%d').date()
#                 nacionalidade = row['nacionalidade']

#                 self.stdout.write(self.style.NOTICE(nome))

#                 Atores.objects.create(
#                     nome=nome,
#                     aniversario=aniversario,
#                     nacionalidade=nacionalidade,
#                 )

#         self.stdout.write(self.style.SUCCESS('Arquivo importado com sucesso!'))

import pandas as pd
from datetime import datetime
from atores.models import Atores
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument(
            'file_name', 
            type=str, 
            help='Nome do arquivo CSV a ser importado',
    )

    def handle(self, *args, **options):
        caminho = r"G:\\workspace\\django master\\flix-api\\atores.csv"
        df = pd.read_csv(caminho, sep=',', encoding='utf-8')
        print(df)
        
        for row in df:
            nome = row['nome']
            aniversario = datetime.strptime(row['aniversario'], '%Y-%m-%d').date()
            nacionalidade = row['nacionalidade']

            self.stdout.write(self.style.NOTICE(nome))

            Atores.objects.create(
                nome=nome,
                aniversario=aniversario,
                nacionalidade=nacionalidade,
            )

        self.stdout.write(self.style.SUCCESS('Arquivo importado com sucesso!'))



