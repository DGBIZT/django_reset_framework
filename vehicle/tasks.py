from celery import shared_task

from celery import shared_task
from vehicle.models import Car, Moto

@shared_task
def check_milage(pk, model):
    if model == 'car':
        instance = Car.objects.filter(pk=pk).first()
    else:
        instance = Moto.objects.filter(pk=pk).first()

    if instance:
        prev_milage = -1
        for m in instance.milage.all():
            if prev_milage == -1:
                prev_milage = m.milage

            else:
                if prev_milage <= m.milage:
                    print("Не верный пробег")
                    break

