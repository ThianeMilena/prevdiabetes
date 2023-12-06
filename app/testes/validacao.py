
class AceitarIdade:
    
    
     def __init__(self, age):
        self.age = age

     def validar_idade(self, age: int):
          if not isinstance(age, int):
               raise ValueError("A idade inserida não é válida")
          elif age is None:
               raise ValueError("A idade inserida não é válida")
          elif age < 0:
               raise ValueError("A idade inserida não pode ser negativa")
          elif age > 120:
               raise ValueError("A idade inserida não é válida")
          return age
     
     
class AceitarIndiceMassaCorporal:

     def __init__(self, bmi):
         self.bmi = bmi

     def validar_imc(self, bmi: float):
          if bmi < 0:
               raise ValueError("O IMC inserido não é válido")
          return bmi
     

class AceitarValorProteina:

     def __init__(self, HbA1c_level):
          self.HbA1c_level = HbA1c_level

     def validar_valor_proteina(self, HbA1c_level: float):
          if HbA1c_level < 20:
               raise ValueError("O nível de hemoglobina glicada inserido é inválido")
          return HbA1c_level


class AceitarValorGlicose:

     def __init__(self,  blood_glucose_level):
          self.blood_glucose_level = blood_glucose_level

     def validar_valor_glicose(self, blood_glucose_level):
          if  blood_glucose_level < 0:
               raise ValueError("O nível de glicose inserido é inválido")
          elif blood_glucose_level > 250:
               raise ValueError("O nível de glicose inserido é inválido")
          return blood_glucose_level