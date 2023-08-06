from django.db import models


# Create your models here.

class Requests(models.Model):
    """
        Modelo para almacenar solicitudes de consultas.

        Atributos:
            id (AutoField): Campo de clave primaria autoincremental que identifica de manera única cada solicitud.
            date (DateField): Campo que almacena la fecha de la solicitud.
            method (CharField): Campo que indica el método utilizado para realizar la consulta (por ejemplo, GET, POST, PUT, DELETE, etc.).
            consult (CharField): Campo que almacena la consulta realizada (por ejemplo, la URL o el contenido enviado).
            dataReturn (CharField): Campo que almacena los datos de retorno o respuesta recibidos tras la consulta.

    """
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    method = models.CharField(max_length=100, null=False)
    consult = models.CharField(max_length=1000, null=False)
    dataReturn = models.CharField(max_length=10000, null=False)
