from rest_framework import serializers
from api.models import Delivery, Message, Client

class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = ('start_time_date', 'text', 'teg', 'end_time_date')

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model=Message
        fields = ('status', 'delivery', 'client')

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('number_phone','time_cms', 'teg')

class StatDeliverySerializer(serializers.ModelSerializer):
    message = serializers.SerializerMethodField()

    class Meta:
        model=Delivery
        fields = ('start_time_date', 'text', 'teg', 'end_time_date', 'message')

    def get_message(self, obj):
        # customer_account_query = Client.objects.filter(
        #     user=obj.id)
        customer_account_query = Message.objects.filter().order_by('status')
        serializer = MessageSerializer(customer_account_query, many=True)
        return serializer.data