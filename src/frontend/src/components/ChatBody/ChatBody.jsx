import './ChatBody.css';
import ChatMessage from '../ChatMessage/ChatMessage';

export default function ChatBody({ messages }) {
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
            </div>
        </div>
    );
}

