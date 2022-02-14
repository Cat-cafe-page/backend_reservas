from AppReservas.models.reserva_usuario       import Reserva
from AppReservas.models.reserva_usuario       import Reserva
from AppReservas.models.plan_usuario          import Plan_usuario
from AppReservas.serializers.plan_serializer  import PlanSerializer
from rest_framework                           import serializers

class CreateReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = ['id_reserva', 'tipo_documento','numero_documento','nombre_completo','telefono','correo_electronico','fecha','id_plan']

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = ['id_reserva', 'tipo_documento','numero_documento','nombre_completo','telefono','correo_electronico','fecha','id_plan']
   
