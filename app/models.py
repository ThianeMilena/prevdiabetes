from django.db import models

# Create your models here.

class Paciente(models.Model):

    age = models.IntegerField()
    bmi = models.FloatField()
    HbA1c_level = models.FloatField()
    blood_glucose_level = models.FloatField()
    diabetes = models.BooleanField(null=True, blank=True)

class Previsao(models.Model):
    resultado = models.BooleanField()