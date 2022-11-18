from __future__ import absolute_import, unicode_literals
from core.celery import app as celery_app
from api.models import Message, Delivery, Client
from django.utils import timezone
import requests
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

@celery_app.on_after_finalize.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(60.0, auto_message.s())
    

@celery_app.task
def auto_message():
    delivery = Delivery.objects.filter(start_time_date__lte = timezone.now(), end_time_date__gte = timezone.now(), posted = False).values('id', 'teg', 'text')
    header = {
                'Authorization': f'Bearer {"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MDAxMzg4MDksImlzcyI6ImZhYnJpcXVlIiwibmFtZSI6IkBpaWlpZW1wdHloaWlpaSJ9.QiIl6FbxlfEgXP6YLxb6-5hY_5uWczl5ppEXx2nQQfY"}',
                'Content-Type': 'application/json'
                }

    for deliver in delivery:
        clients = Client.objects.filter(teg = deliver['teg']).values('number_phone', 'id')
        for client in clients:
            data = {
                "id":deliver['id'],
                "phone":client['number_phone'],
                "text":deliver['text']
            }
            try:
                resp = requests.post(url=f'https://probe.fbrq.cloud/v1/send/{deliver["id"]}', json=data, headers=header)
                if resp.status_code == 200:
                    Delivery.objects.filter(id=deliver['id']).update(posted=True)
                    Message.objects.create(status=True, delivery_id=deliver["id"], client_id=client['id'])
                    logger.info(f"Сообщение с id {data['id']} было отправлено")
                else:
                    message = Message.objects.create(status=False, delivery_id=deliver["id"], client_id=client['id'])
                    logger.error(f"Пользователю с id {client['id']} не была доставлена расслка с id {deliver['id']}, id сообщения {message.id}")
            except:
                logger.info(f"Рассылка {data['id']} не была доставлена пользователю с id {client['id']}")
    

