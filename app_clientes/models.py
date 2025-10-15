from django.db import models

class Cliente(models.Model):
    id_cliente = models.CharField(max_length=20, unique=True) # Puedes usar UUIDField si prefieres
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo_electronico = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15, blank=True, null=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.nombre} {self.apellido} ({self.id_cliente})'

    class Meta:
        ordering = ['fecha_registro'] # Opcional: ordenar por fecha de registro