import pandas as pd
import joblib
import os

def carregar_modelo(modelo_caminho):
   try:
        if os.path.exists(modelo_caminho):
            modelo = joblib.load(modelo_caminho)
            print("Modelo carregado com sucesso!")
            return modelo
        else:
            print("Caminho do modelo não encontrado.")
            return None
   except Exception as e:
        print(f"Erro ao carregar o modelo: {str(e)}")
        return None

def fazer_previsao(modelo, dados):
    try:
        print("Valores recebidos:", dados)

        dados_formatados = pd.DataFrame.from_dict(dados, orient='index').transpose()

        dados_formatados = dados_formatados.apply(lambda x: pd.to_numeric(x, errors='ignore'))

        print("Valores formatados:", dados_formatados)

        resultado_da_previsao = modelo.predict(dados_formatados)

        resultado_serializavel = bool(resultado_da_previsao[0])

        return resultado_serializavel
    except Exception as e:
        print(f'Erro na previsão: {str(e)}')
        return None













