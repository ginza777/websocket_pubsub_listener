# websocket_pubsub_listener# 
# Django WebSocket Integration

This project demonstrates how to set up a Django application to work with WebSocket protocol.

## Getting Started

Clone the project:

```bash
git clone https://github.com/Sherzamon/websocket_pubsub_listener.git
```

```bash
cd websocket_pubsub_listener
```

Set up a virtual environment and install Django:
```bash
python -m venv venv
```
```bash
source venv/bin/activate
```
```bash
pip install -r requirements.txt
```

Apply migrations and set up the database:
```bash
python manage.py makemigrations
```
```bash
python manage.py migrate
```

Start the server:
```bash
python manage.py runserver
```

Creating a Channel and Text on localhost

```bash
curl -X POST http://localhost:8000/ -d "channel=my_channel&text=Salom, dunyo!"
```
WebSocket Communication
Open a WebSocket connection:


```bash
ws://localhost:8000/ws/my_channel/
```
