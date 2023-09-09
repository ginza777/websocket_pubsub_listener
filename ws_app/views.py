import json

from django.core.cache.backends import redis
from django.shortcuts import render
from rest_framework import generics
from rest_framework import serializers
from channels.layers import get_channel_layer
from ws_app.models import Message
from asgiref.sync import async_to_sync
import redis

# Create your views here.


class MessageCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['text']


class MessageCreateView(generics.CreateAPIView):
    serializer_class = MessageCreateSerializer
    queryset = Message.objects.all()

    def post(self, request, *args, **kwargs):
        message_text = request.data['text']
        print(message_text)

        # Create the message in the database
        message = Message.objects.create(text=message_text)

        # Publish the message to the 'events' Redis channel
        r = redis.Redis(host='localhost', port=6379, db=0)
        payload = json.dumps({'message': message.text})
        r.publish('events', payload)

        # Send the message to connected WebSocket clients

        response = super().post(request, *args, **kwargs)
        return response