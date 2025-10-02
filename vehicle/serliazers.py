from rest_framework import serializers
from vehicle.models import Car, Moto, Milage
from vehicle.validators import TitleValidator


class MilageSerializers(serializers.ModelSerializer):

    class Meta:
        model = Milage
        fields = "__all__"


class CarSerializer(serializers.ModelSerializer):

    last_milage = serializers.IntegerField(source="milage.all.first.milage") # Выводит последний записанный пробег
    milage = MilageSerializers(many=True)

    class Meta:
        model = Car
        fields = '__all__'

    def create(self, validated_data):
        # Извлекаем данные пробега из validated_data
        milage = validated_data.pop("milage")

        car_item = Car.objects.create(**validated_data)
        # Для каждого элемента пробега создаем отдельную запись
        for m in milage:
            Milage.objects.create(**m, car=car_item)  # Связываем с созданной машиной

        return car_item

    # Второй вариант если не все заполнены таблицы
    # last_milage = serializers.SerializerMethodField()
    # milage = MilageSerializers(many=True)
    #
    # class Meta:
    #     model = Car
    #     fields = '__all__'
    #
    # def get_last_milage(self, instance):
    #     # Проверяем, есть ли пробег, и возвращаем последнее значение
    #     first_milage = instance.milage.all().first()
    #     if first_milage:
    #         return first_milage.milage
    #     return 0  # Возвращаем 0, если пробега нет

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
        validators = [
            TitleValidator(field='title'),
            serializers.UniqueTogetherValidator(fields=['title', "description"], queryset=Moto.objects.all()),
        ]

    def create(self, validated_data):
        # Извлекаем данные пробега из validated_data
        milage = validated_data.pop("milage")

        moto_item = Moto.objects.create(**validated_data)
        # Для каждого элемента пробега создаем отдельную запись
        for m in milage:
            Milage.objects.create(**m, moto=moto_item) # Связываем с созданным мотоциклом

        return moto_item

