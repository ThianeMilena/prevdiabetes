from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from app.models import Paciente 
from app.previsao import fazer_previsao
from app.previsao import carregar_modelo
import os

schema_view = get_schema_view(
    openapi.Info(
        title="Django Sample Application API",
        default_version='v1',
        description="Welcome to the Django Sample Application API documentation",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

class Personnel(APIView):
    def get(self, request):
       
        return Response(data={}, status=status.HTTP_200_OK)

    def post(self, request):
        
        return Response(data={}, status=status.HTTP_201_CREATED)

class ReceberDadosPaciente(APIView):
    """
    View para receber dados de pacientes.
    """

    def get(self, request):
        """
        Manipula requisições GET.
        Retorna uma resposta vazia com status HTTP 200 OK.
        """
        return Response(data={}, status=status.HTTP_200_OK)

    def post(self, request):
        """
        Manipula requisições POST para receber dados do paciente.
        """
        dados = request.data

        try:
            paciente = Paciente(
                age=int(dados.get('age')),
                bmi=float(dados.get('bmi')),
                HbA1c_level=float(dados.get('HbA1c_level')),
                blood_glucose_level=float(dados.get('blood_glucose_level')),
            )
            paciente.save()

            downloads_path = os.path.join(os.path.expanduser('~'), 'Downloads')

            modelo_caminho = os.path.join(downloads_path, 'modelo_diabetes.pkl')

            modelo = carregar_modelo(modelo_caminho)
         
            resultado_previsao = fazer_previsao(modelo, {
                'age': paciente.age,
                'bmi': paciente.bmi,
                'HbA1c_level': paciente.HbA1c_level,
                'blood_glucose_level': paciente.blood_glucose_level,
            })

            paciente.diabetes = resultado_previsao
            paciente.save()

            return JsonResponse({'resultado_previsao': resultado_previsao})
        except Exception as e:
            return JsonResponse({'error': f'Erro ao processar dados: {str(e)}'}, status=400)



