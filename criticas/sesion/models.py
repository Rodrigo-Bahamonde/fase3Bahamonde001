from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.

class Perfil(models.Model):
    id = models.AutoField(primary_key=True,unique=True)
    usuario= models.OneToOneField(User, on_delete=models.CASCADE, related_name = 'usuario')
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    edad = models.DecimalField(max_digits=2, decimal_places=0)
    
    genero_status = (
        ('Masculino', 'Masculino'),
        ('Femenino', 'Femenino'),
    )

    nacionalidad_status = (
        ('--Seleccione una opción--', 'Seleccione una opcion'),
        ('Argentina', 'Argentina'),
        ('Bolivia', 'Bolivia'),
        ('Chile', 'Chile'),
        ('Colombia', 'Colombia'),
        ('Costa Rica', 'Costa Rica'),
        ('Cuba', 'Cuba'),
        ('Ecuador', 'Ecuador'),
        ('El Salvador', 'El Salvador'),
        ('Guatemala', 'Guatemala'),
        ('Honduras', 'Honduras'),
        ('México', 'México'),
        ('Nicaragua', 'Nicaragua'),
        ('Panamá', 'Panamá'),
        ('Paraguay', 'Paraguay'),
        ('Perú', 'Perú'),
        ('Puerto Rico', 'Puerto Rico'),
        ('República Dominicana', 'República Dominicana'),
        ('Uruguay', 'Uruguay'),
        ('Venezuela', 'Venezuela'),
        ('España', 'España'),
        ('Guinea Ecuatorial', 'Guinea Ecuatorial'),
        ('Otro', 'Otro'),
    )

    tipo_status = (
        ('Admin', 'Admin'),
        ('User', 'User'),
    )

    genero = models.CharField(
        max_length = 50,
        choices = genero_status,
    )
    nacionalidad = models.CharField(
        max_length = 50,
        choices = nacionalidad_status,
    )
    correo = models.EmailField()

    tipo = models.CharField(
        max_length = 6,
        choices = tipo_status,
        default = 'User',
    )

    def __str__(self):
        return f'{self.usuario}'
    
    def get_absolute_url(self):
        return reverse('perfil-detail', args=[str(self.usuario)])

    

    