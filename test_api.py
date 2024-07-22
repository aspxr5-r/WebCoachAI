import requests

BASE_URL = 'http://localhost:5000/api'

def register(username, password):
    response = requests.post(f'{BASE_URL}/register', json={'username': username, 'password': password})
    print('Register:', response.json())

def login(username, password):
    response = requests.post(f'{BASE_URL}/login', json={'username': username, 'password': password})
    print('Login:', response.json())
    return response.cookies.get('session')

def create_chat():
    response = requests.post(f'{BASE_URL}/chat')
    print('Create Chat:', response.json())
    return response.json().get('chat_id')

def send_message(session_cookie, chat_id, message):
    response = requests.post(f'{BASE_URL}/chat/{chat_id}/message', cookies={'session': session_cookie})
    print('AI Response:', response.json())

def get_chat_history(session_cookie, chat_id):
    response = requests.get(f'{BASE_URL}/chat/{chat_id}/history', cookies={'session': session_cookie})
    print('Chat History:', response.json())


username = 'testuser'
password = 'testpassword'

register(username, password)
session_cookie = login(username, password)
chat_id = create_chat(session_cookie)
send_message(session, chat_id, 'How do I create my own AI Coach?')
get_chat_history(session_cookie, chat_id)
