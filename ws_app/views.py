import json
import datetime
from datetime import datetime, timedelta
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
        fields = ['text','channel']


class MessageCreateView(generics.CreateAPIView):
    serializer_class = MessageCreateSerializer
    queryset = Message.objects.all()

    def post(self, request, *args, **kwargs):
        message_text = request.data['text']
        channel = request.data['channel']


        # Create the message in the database
        message = Message.objects.create(text=message_text)
        # Publish the message to the 'events' Redis channel
        r = redis.Redis(host='localhost', port=6379, db=0)
        payload = json.dumps({'message': message.text})
        r.publish(channel, payload)


        # Send the message to connected WebSocket clients

        response = super().post(request, *args, **kwargs)
        return response