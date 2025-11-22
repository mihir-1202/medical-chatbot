import './Footer.css';

export default function Footer({ onSendMessage }) {
    const handleSubmit = () => {
        const textarea = document.querySelector('.input-section textarea');
        const message = textarea.value.trim();
        
        if (message && onSendMessage) {
            onSendMessage(message);
            textarea.value = '';
        }
    };

    const handleKeyDown = (e) => {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            handleSubmit();
        }
    };

    return (
        <div className="chat-footer">
            <div className="footer-section">
                <div className="input-section">
                    <textarea 
                        placeholder="Type your medical question here..." 
                        rows="1"
                        onKeyDown={handleKeyDown}
                    />
                    <button type="submit" onClick={handleSubmit}>Send</button>
                </div>
                <div className="disclaimer-section">
                    ⚠️ Disclaimer: This is for informational purposes only. Always consult healthcare professionals for medical advice.
                </div>
            </div>
        </div>
    );
}

