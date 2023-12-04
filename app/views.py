from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Paciente
from .previsao import carregar_modelo, fazer_previsao
from django.views.decorators.debug import sensitive_post_parameters
import os

# Obtendo o caminho do diretório "Downloads"
downloads_path = os.path.join(os.path.expanduser('~'), 'Downloads')

# Construindo o caminho completo para o modelo
modelo_caminho = os.path.join(downloads_path, 'modelo_diabetes.pkl')

# Carregando modelo
modelo = carregar_modelo(modelo_caminho)

def minha_pagina_inicial(request):
    return JsonResponse({'message': 'Bem-vindo à minha página inicial!'})

@sensitive_post_parameters()
@csrf_exempt
def receber_dados_paciente(request):

    if request.method == 'GET':
        return render(request, 'app/receber_dados_paciente.html')

    if request.method == 'POST':
        dados = request.POST.copy() 
        dados.pop('csrfmiddlewaretoken', None) 

        try:
            paciente = Paciente(
                age=int(dados['age']),
                bmi=float(dados['bmi']),
                HbA1c_level=float(dados['HbA1c_level']),
                blood_glucose_level=float(dados['blood_glucose_level']),
            )
            paciente.save()

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
    else:
        return JsonResponse({'error': 'Método não permitido'}, status=405)