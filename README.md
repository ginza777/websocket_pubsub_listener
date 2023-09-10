# websocket_pubsub_listener# 
# Django WebSocket Ishga Tushirish

Bu proyekt Django ilovasini WebSocket protokolini ishlatish uchun qanday sozlashni ko'rsatadi.

## Ishga Tushirish

Proyektni o'rnating:

```bash
git clone https://github.com/sizning-hisobingiz/lokal-repo.git
cd lokal-repo
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
curl -X POST http://localhost:8000/api/create-message/ -d "channel=my_channel&text=Salom, dunyo!"
ws://localhost:8000/ws/my_channel/
