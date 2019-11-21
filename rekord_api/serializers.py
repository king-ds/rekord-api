from rekord_api.models import Transportation
from rest_framework import serializers

class TransportationSerializer(serializers.ModelSerializer):

    description = serializers.CharField(required=False)
    location = serializers.CharField(required=True)
    cost = serializers.IntegerField(required=True)
    departure_date = serializers.DateTimeField(required=True)
    eta = serializers.IntegerField(required=True)
    vehicle_type = serializers.CharField(required=True)

    class Meta:
        model = Transportation
        fields = ('id', 'description', 'location', 'cost', 'departure_date', 'eta', 'vehicle_type')

class TransportationUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transportation
        fields = ('id', 'arrived', 'arrival_date')

        def update(self, instance, validated_data):
            instance.arrived = validated_data.get('arrived', instance.arrived)
            instance.arrival_date = validated_data.get('arrival_date', instance.arrival_date)
            instance = super().update(instance, validated_data)

            return instance