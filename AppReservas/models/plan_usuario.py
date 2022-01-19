from django.db    import models

JORNADAS = (("Diurna","diurna"),("Nocturna","nocturna"))
class Plan_usuario(models.Model): 
    id_plan            = models.BigAutoField(primary_key=True)
    jornada            = models.CharField('Jornada',choices=JORNADAS, max_length=10, default="Diurno")
    nombre_plan        = models.CharField('Nombre del plan', max_length=50)
    duracion           = models.FloatField('Duración en minutos', default="45.00")
    descripcion        = models.CharField('Descripcion', max_length=100)
    precio             = models.FloatField('Precio', default= 0.00)
    url                = models.CharField('Url del plan', max_length=2083, default="https://images.squarespace-cdn.com/content/v1/59014ed8db29d637250fa476/1506798703877-DZ64MSMJEPT91MKR124C/IMG_7487.JPG?format=1500w")
    
