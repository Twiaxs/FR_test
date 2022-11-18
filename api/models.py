from django.db import models
from django.core.validators import RegexValidator

class Delivery(models.Model):
    start_time_date = models.DateTimeField(verbose_name="Дата и время начала рассылки")
    text = models.TextField(verbose_name="Текст")
    teg = models.CharField(max_length=255)
    end_time_date = models.DateTimeField(verbose_name="Дата и время конца рассылки")
    posted = models.BooleanField(verbose_name='Отработан', default=False, null=True, blank=True)

    def __str__(self) -> str:
        return self.text


class Client(models.Model):
    phone_code = RegexValidator(regex=r'^7\d{10}$', message="The client's phone number in the format 7XXXXXXXXXX (X - number from 0 to 9)")
    number_phone = models.CharField(verbose_name="Номер телефона", validators=[phone_code], max_length=11)
    time_cms = models.CharField(max_length=20)
    teg = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.number_phone

class Message(models.Model):
    time_date = models.DateTimeField(verbose_name="Время начала рассылки", auto_now_add=True)
    status = models.BooleanField(verbose_name='Стутс')
    delivery = models.ForeignKey(Delivery, verbose_name='Ид рассылки', on_delete=models.CASCADE)
    client = models.ForeignKey(Client ,verbose_name='Клиент', on_delete=models.CASCADE)




