from flask import Flask, jsonify, request, session
from flask_cors import CORS
from modules import auth, chat
from modules.database import test_connection

app = Flask(__name__)
CORS(app)
app.secret_key = 'your_secret_key'  # Replace with a real secret key

test_connection()
@app.route('/')
def hello():
    return jsonify({"message": "Welcome to WebCoach AI!"})

@app.route('/register', methods=['POST'])
def register():
    return auth.register()

@app.route('/login', methods=['POST'])
def login():
    return auth.login()

@app.route('/logout', methods=['POST'])
def logout():
    return auth.logout()

@app.route('/chat', methods=['POST'])
def create_chat_route():
    return chat.create_chat()

@app.route('/api/chat/<chat_id>', methods=['POST'])
def send_message_route(chat_id):
    return chat.send_message(chat_id)

@app.route('/api/chat/<chat_id>', methods=['GET'])
def get_chat_history_route(chat_id):
    return chat.get_chat_history(chat_id)
def send_message_route(chat_id):
    return chat.send_message(chat_id)

@app.route('/api/chat/<chat_id>/message', methods=['POST'])
def send_message(chat_id):
    return chat.send_message(chat_id)


@app.route('/api/chat/<chat_id>/history', methods=['GET'])
def get_chat_history(chat_id):
    return chat.get_chat_history(chat_id)


if __name__ == '__main__':
    app.run(debug=True)