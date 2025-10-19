# celery.py
import os
import eventlet
from celery import Celery

# Применяем monkey_patch только для необходимых компонентов
eventlet.monkey_patch(
    os=False,
    select=True,
    socket=True,
    thread=False,
    time=False
)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
app = Celery('config')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# Только базовые настройки
app.conf.update(
    worker_concurrency=4,
    broker_url='redis://localhost:6379/0',
    result_backend='redis://localhost:6379/0'
)
