from rest_framework.generics import (ListCreateAPIView,UpdateAPIView, CreateAPIView, ListAPIView, DestroyAPIView)
from rest_framework.permissions import IsAuthenticated
from api.models import Client, Message, Delivery
from api.serializers import ClientSerializer, MessageSerializer, DeliverySerializer, StatDeliverySerializer


class UserProfileListCreateView(ListCreateAPIView):
    queryset=Client.objects.all()
    serializer_class=ClientSerializer


class UserProfileListUpdateView(UpdateAPIView):
    queryset=Client.objects.all()
    serializer_class=ClientSerializer


class UserProfileListDestroyView(DestroyAPIView):
    queryset=Client.objects.all()
    serializer_class=ClientSerializer


class MessageCreateView(ListCreateAPIView):
    queryset=Message.objects.all()
    serializer_class=MessageSerializer


class DeliveryCreateView(ListCreateAPIView):
    queryset=Delivery.objects.all()
    serializer_class=DeliverySerializer


class DeliveryDestroyAPIView(DestroyAPIView):
    queryset=Delivery.objects.all()
    serializer_class=DeliverySerializer


class DeliveryUpdateAPIView(UpdateAPIView):
    queryset=Delivery.objects.all()
    serializer_class=DeliverySerializer


class StatDeliveryView(ListAPIView):
    queryset=Delivery.objects.all()
    serializer_class=StatDeliverySerializer


  