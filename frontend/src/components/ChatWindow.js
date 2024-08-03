import React, { useState } from 'react';

function ChatWindow({ chat, addMessage }) {
  const [message, setMessage] = useState('');

  const sendMessage = (e) => {
    e.preventDefault();
    if (message.trim()) {
      addMessage(chat.id, message);
      setMessage('');
    }
  };

  return (
    <div className="chat-window">
      <div className="messages">
        {chat.messages.map((msg, index) => (
          <div key={index} className={`message ${msg.sender}`}>
            {msg.text}
          </div>
        ))}
      </div>
      <form onSubmit={sendMessage} className="message-input">
        <input
          type="text"
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          placeholder="Type your message..."
        />
        <button type="submit">Send</button>
      </form>
    </div>
  );
}

export default ChatWindow;