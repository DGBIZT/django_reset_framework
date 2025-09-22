from rest_framework import serializers
from vehicle.models import Car, Moto, Milage


class CarSerializer(serializers.ModelSerializer):

    last_milage = serializers.IntegerField(source="milage_set.all.first.milage") # Выводит последний записанный пробег

    class Meta:
        model = Car
        fields = '__all__'

class MotoSerializer(serializers.ModelSerializer):

    last_milage = serializers.SerializerMethodField()

    class Meta:
        model = Moto
        fields = '__all__'

    def get_last_milage(self, instance):
        if instance.milage_set.all().first():
            return instance.milage_set.all().first().milage
        return 0


class MilageSerializers(serializers.ModelSerializer):

    class Meta:
        model = Milage
        fields = "__all__"