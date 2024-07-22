from flask import jsonify, request
from modules.database import chat_sessions
from config import OPENAI_API_KEY
import openai

openai.api_key = OPENAI_API_KEY

def create_chat():
   if 'user_id' not in session:
        return jsonify({'message': 'Unauthorized'}), 401
   
   chat = {
       'user_id': session['user_id'],
       'messages': [],
       'created_at': datetime.utcnow()
    }
   result = chat_sessions.insert_one(chat)
   return jsonify({'id': str(result.inserted_id)}), 201

def send_message(chat_id):
    if 'user_id' not in session:
        return jsonify({'message': 'Unauthorized'}), 401

    user_message = request.json.get('message')
    if not user_message: 
        return jsonify({'message': 'Missing required fields'}), 400

    chat = chat_sessions.find_one({'_id': ObjectId(chat_id), 'user_id': session['user_id']})
    if not chat:
        return jsonify({'message': 'Chat not found'}), 404
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages= [
            {'role': 'system', 'content': ' You are an AI Coach describing the potential and the functionality of webcoach AI. You are trying to help the user and convince them about the project.'},
            {'role': 'user', 'content': user_message}
        ]
    )
    ai_message = response.choices[0].message['content']

    chat_sessions.update_one(
        {'_id': ObjectId(chat_id)},
        {'$push': {'messages': {'user': user_message, 'ai': ai_message, 'timestamp': datetime.utcnow()}}}
    )

    return jsonify({'message': ai_message}), 200
def get_chat_history():
    if 'user_id' not in session:
        return jsonify({'error': 'PLease log in'}), 401
    
    chat = chat_sessions.find_one({'user_id': session['user_id']})
    if not chat:
        return jsonify({'error': 'Chat not found'}), 404
    
    return jsonify({'messages': chat['messages']}), 200