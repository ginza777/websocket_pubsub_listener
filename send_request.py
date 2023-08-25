import asyncio
import websockets
import json

async def send_calculation():
    async with websockets.connect('ws://localhost:8000/ws/calculator/') as websocket:
        calculation_data = {
            "operation": "subtract",
            "num1": 15,
            "num2": 9
        }
        await websocket.send(json.dumps(calculation_data))

        response = await websocket.recv()
        print("Response:", response)

asyncio.get_event_loop().run_until_complete(send_calculation())
