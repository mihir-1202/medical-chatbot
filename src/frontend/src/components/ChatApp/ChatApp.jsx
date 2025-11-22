import { useState } from 'react';
import './ChatApp.css';
import Navbar from '../Navbar/Navbar';
import ChatBody from '../ChatBody/ChatBody';
import Footer from '../Footer/Footer';

export default function ChatApp() {
    const [messages, setMessages] = useState([
        {
            from: 'ai',
            content: "Hello! I'm your medical assistant. How can I help you today?"
        }
    ]);

    const handleSendMessage = (content) => {
        // Add user message
        setMessages(prev => [...prev, { from: 'user', content }]);
        
        fetch ('http://localhost:8000/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ prompt: content })
        })
        .then(response => response.json())
        .then(data => {
            setMessages(prev => [...prev, { from: 'ai', content: data }]);
        })
        .catch(error => {
            console.error('Error:', error);
            setMessages(prev => [...prev, { 
                from: 'ai', 
                content: '❌ Sorry, I encountered an error. Please try again.' 
            }]);
        });
    };

    return (
        <div className="chat-container">
            <Navbar />
            <ChatBody messages={messages} />
            <Footer onSendMessage={handleSendMessage} />
        </div>
    );
}

