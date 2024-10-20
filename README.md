### Motivation
After learning online, I added API and decided to share.

chat features:
* create and join chatroom by specifying room_name 
* all chat_messages are broadcast to everyone else in room
* query all rooms created by call to /room [added]

### Install Guide
copy and run (assume linux with python3):
```
python3 -m venv test
cd test
source bin/activate
git clone https://github.com/wendy-py/django_todo.git
cd django_todo
pip install Django django-crispy-forms
pip install --upgrade attrs
python manage.py migrate
python manage.py runserver
```
