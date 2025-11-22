import './Navbar.css';

export default function Navbar() {
    return (
        <nav className="nav-container">
            <div className="logo-section"> 
                <div className="logo-icon">🏥</div>

                <div className="chatbot-text">
                    <h1>Medical Assistant</h1>
                    <h2>AI Powered Medical Information</h2>
                </div>  
            </div>

            <div className="status-section">
                <div className="status-section-left">
                    <div className="status-dot"></div>
                    <span className="status-text">Online</span>
                </div>
            </div>
        </nav>
    );
}

