from django.test import TestCase
import pytest
import unittest
from .validacao import AceitarIdade
from .validacao import AceitarIndiceMassaCorporal
from .validacao import AceitarValorProteina
from .validacao import AceitarValorGlicose

class TestaAceitarIdade(unittest.TestCase):

# Teste para validar se o sistema recebe número inteiro

    def test_validar_idade_numero_inteiro(self):
        aceitar_idade = AceitarIdade(None) 
        actual_result = aceitar_idade.validar_idade(25)
        self.assertEqual(actual_result, 25)

# Teste para validar se o sistema recebe texto ao invés de número inteiro

    def test_validar_idade_texto(self):
        aceitar_idade = AceitarIdade(None)
        actual_result = aceitar_idade.validar_idade("teste")
        self.assertEqual(actual_result, "teste")

# Teste para validar se o sistema passa nenhuma resposta inserida    

    def test_validar_nenhum_valor_inserido(self):
        aceitar_idade = AceitarIdade(None)
        actual_result = aceitar_idade.validar_idade(None)
        self.assertEqual(actual_result, None)

# Teste para validar se o sistema recebe valor negativo

    def test_validar_idade_negativa(self):
        aceitar_idade = AceitarIdade(None)
        actual_result = aceitar_idade.validar_idade(-5)
        self.assertEqual(actual_result, -5)


class TestaAceitarImc(unittest.TestCase):

# Teste para validar se o sistema aceita um valor de IMC inválido

    def test_validar_imc_com_valor_invalido(self):
        aceitar_bmi = AceitarIndiceMassaCorporal(None)
        actual_result = aceitar_bmi.validar_imc(-5)
        self.assertEqual(actual_result, -5)
        
# Teste para validar se o sitema aceita um valor de IMC válido

    def test_validar_imc_com_valor_valido(self):
        aceitar_bmi = AceitarIndiceMassaCorporal(None)
        actual_result = aceitar_bmi.validar_imc(30)
        self.assertEqual(actual_result, 30)

class TestaAceitarProteina(unittest.TestCase):

# Teste para validar se o sistema aceita um valor de nível de hemoglobina glicada inválido

    def test_validar_proteina_com_valor_invalido(self):
        aceitar_proteina = AceitarValorProteina(None)
        actual_result = aceitar_proteina.validar_valor_proteina(16)
        self.assertEqual(actual_result, 16)

# Teste para validar se o sistema aceita um valor de nível de hemoglobina glicada válido  
      
    def test_validar_proteina_com_valor_valido(self):
        aceitar_proteina = AceitarValorProteina(None)
        actual_result = aceitar_proteina.validar_valor_proteina(30)
        self.assertEqual(actual_result, 30)

class TestaAceitarNivelGlicose(unittest.TestCase):

# Teste para validar se o sistema aceita um valor de nível de glicose inválido negativo:

    def test_validar_nivel_glicose_com_valor_invalido_negativo(self):
        aceitar_nivel_glicose = AceitarValorGlicose(None)
        actual_result = aceitar_nivel_glicose.validar_valor_glicose(-2)
        self.assertEqual(actual_result, -2)

# Teste para validar se o sistema aceita um valor de nível de glicose inválido extremamente alto:

    def test_validar_nivel_glicose_com_valor_invalido_extremo(self):
        aceitar_nivel_glicose = AceitarValorGlicose(None)
        actual_result = aceitar_nivel_glicose.validar_valor_glicose(252)
        self.assertEqual(actual_result, 252)

# Teste para validar se o sistema aceita um valor de nível de glicose válido:
      
    def test_validar_proteina_com_valor_valido(self):
        aceitar_nivel_glicose = AceitarValorGlicose(None)
        actual_result = aceitar_nivel_glicose.validar_valor_glicose(16)
        self.assertEqual(actual_result, 16)
   