from django.db import models

# Create your models here.

class Empresa(models.Model):
    nome = models.CharField(max_length = 255)
    CNPJ = models.DecimalField(max_digits=11, decimal_places=4)

class Funcionario(models.Model):
    nome = models.CharField(max_length = 255)
    rua = models.CharField(max_length = 255)
    area = models.CharField(max_length = 255)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)

class Disciplinas(models.Model):
    descricao= models.CharField(max_length = 255)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)

class Professor(models.Model):
    nome = models.CharField(max_length = 255)
    disciplinas = models.ForeignKey(Disciplinas, on_delete=models.CASCADE)

