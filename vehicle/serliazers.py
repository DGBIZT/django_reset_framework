from rest_framework import serializers
from vehicle.models import Car, Moto, Milage



class MilageSerializers(serializers.ModelSerializer):

    class Meta:
        model = Milage
        fields = "__all__"


class CarSerializer(serializers.ModelSerializer):

    last_milage = serializers.IntegerField(source="milage_set.all.first.milage") # Выводит последний записанный пробег
    milage = MilageSerializers(many=True)

    class Meta:
        model = Car
        fields = '__all__'

class MotoSerializer(serializers.ModelSerializer):

    last_milage = serializers.SerializerMethodField()

    class Meta:
        model = Moto
        fields = '__all__'

    def get_last_milage(self, instance):
        if instance.milage.all().first():
            return instance.milage.all().first().milage
        return 0


class MotoMilageSerializers(serializers.ModelSerializer):

    moto = MotoSerializer()

    class Meta:
        model = Milage
        fields = ("milage", "year", "moto",)


class MotoCreateSerializer(serializers.ModelSerializer):

    milage = MilageSerializers(many=True)

    class Meta:
        model = Moto
        fields = "__all__"

    def create(self, validated_data):
        # Извлекаем данные пробега из validated_data
        milage = validated_data.pop("milage")

        moto_item = Moto.objects.create(**validated_data)
        # Для каждого элемента пробега создаем отдельную запись
        for m in milage:
            Milage.objects.create(**m, moto=moto_item) # Связываем с созданным мотоциклом

        return moto_item

