from channels.generic.websocket import AsyncWebsocketConsumer
import json

class CalculatorConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def receive(self, text_data):
        print(text_data)
        text_data_json = json.loads(text_data)
        print(text_data_json)

        operation = text_data_json['operation']

        if operation == "add":
            num1 = text_data_json['num1']
            num2 = text_data_json['num2']
            result = num1 + num2

            await self.send(text_data=json.dumps({
                'result': result
            }))
        elif operation == "subtract":
            num1 = text_data_json['num1']
            num2 = text_data_json['num2']
            result = num1 - num2

            await self.send(text_data=json.dumps({
                'result': result
            }))
        else:
            await self.send(text_data=json.dumps({
                'error': 'Invalid operation'
            }))
