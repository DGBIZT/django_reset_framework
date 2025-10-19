from django.conf import settings
from django.db import models




class Car(models.Model):
    title = models.CharField(max_length=150, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'машина'
        verbose_name_plural = 'машины'

class Moto(models.Model):
    title = models.CharField(max_length=150, verbose_name="Название")
    description = models.TextField(verbose_name="Описание")
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'мотоцикл'
        verbose_name_plural = 'мотоциклы'

class Milage(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, null=True, blank=True, related_name="milage")
    moto = models.ForeignKey(Moto, on_delete=models.CASCADE, null=True, blank=True,related_name="milage")

    milage = models.PositiveIntegerField(verbose_name="пробег")
    year = models.PositiveSmallIntegerField(verbose_name="год регистрации")

    def __str__(self):
        return f"{self.moto if self.moto else self.car} - {self.year}"

    class Meta:
        verbose_name = "пробег"
        verbose_name_plural = "пробег"
        ordering = ("-year",)


