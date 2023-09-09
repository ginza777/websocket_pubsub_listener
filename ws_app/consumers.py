# consumers.py
import time

from channels.generic.websocket import AsyncWebsocketConsumer
import json
import aioredis


# def message():
#     redis = aioredis.from_url("redis://127.0.0.1:6379/0")
#     pubsub = redis.pubsub()
#     await pubsub.subscribe("events")
#     async for message in pubsub.listen():
#         print('socket: ', message)
#         if message['type'] != 'message':
#             print('socket: ', message)

import redis
import aioredis
from channels.generic.websocket import AsyncWebsocketConsumer

class WsPubsubConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        channel=self.scope['url_route']['kwargs']['channel']
        await self.accept()
        print('WebSocket connected')
        self.redis = await aioredis.from_url("redis://127.0.0.1:6379/0")
        self.pubsub = self.redis.pubsub()
        await self.pubsub.subscribe(channel)

        while True:
            message = await self.pubsub.get_message()
            if message is not None:
                message=str(message['data'])
                await self.send(message)














