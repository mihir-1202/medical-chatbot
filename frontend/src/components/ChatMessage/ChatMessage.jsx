import './ChatMessage.css';

export default function ChatMessage({ from, content }) {
    const isUser = from === 'user';

    return (
        <div className={isUser ? 'chat-body-message-user' : 'chat-body-message-ai'}>
            {!isUser && <div className="message-avatar-ai">🏥</div>}
            <p className="chat-message">{content}</p>
            {isUser && <div className="message-avatar-user">👤</div>}
        </div>
    );
}

