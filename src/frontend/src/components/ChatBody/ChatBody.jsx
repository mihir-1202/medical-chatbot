import './ChatBody.css';
import ChatMessage from '../ChatMessage/ChatMessage';
import { useRef, useEffect } from 'react';


export default function ChatBody({ messages }) {
    const messagesEndRef = useRef(null);
    
    //created an empty div after all the chat messages
    //when the messages change, scroll to that empty div, which consequently scrolls to the bottom of the chatbox
    //useEffect will only run after a render, so messagesEndRef will never be null
    useEffect(() => {
        messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
    }, [messages]);
    
    return (
        <div className="chat-body">
            <div className = "chat-body-messages">
                {messages.map((message, index) => (
                    <ChatMessage 
                        key={index}
                        from={message.from}
                        content={message.content}
                    />
                ))}
                <div ref={messagesEndRef} />
            </div>
        </div>
    );
}

