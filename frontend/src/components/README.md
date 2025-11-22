# Medical Chatbot Components

This directory contains modular React components for the medical chatbot interface.

## Component Structure

```
components/
├── ChatApp/          # Main app container
│   ├── ChatApp.jsx
│   └── ChatApp.css
├── Navbar/           # Top navigation bar with logo and status
│   ├── Navbar.jsx
│   └── Navbar.css
├── ChatBody/         # Message container
│   ├── ChatBody.jsx
│   └── ChatBody.css
├── ChatMessage/      # Individual message component
│   ├── ChatMessage.jsx
│   └── ChatMessage.css
└── Footer/           # Input area and disclaimer
    ├── Footer.jsx
    └── Footer.css
```

## Usage

### Basic Usage

Import and use the `ChatApp` component in your main `App.jsx`:

```jsx
import ChatApp from './components/ChatApp/ChatApp';

function App() {
  return <ChatApp />;
}

export default App;
```

### Individual Components

You can also use components individually:

```jsx
import Navbar from './components/Navbar/Navbar';
import ChatBody from './components/ChatBody/ChatBody';
import ChatMessage from './components/ChatMessage/ChatMessage';
import Footer from './components/Footer/Footer';

function CustomChat() {
  const [messages, setMessages] = useState([
    { type: 'ai', content: 'Hello!' },
    { type: 'user', content: 'Hi there!' }
  ]);

  const handleSendMessage = (content) => {
    setMessages([...messages, { type: 'user', content }]);
  };

  return (
    <div className="chat-container">
      <Navbar />
      <ChatBody messages={messages} />
      <Footer onSendMessage={handleSendMessage} />
    </div>
  );
}
```

## Component Props

### ChatApp
- No props required (self-contained)

### Navbar
- No props required

### ChatBody
- `messages` (array): Array of message objects with `type` ('ai' | 'user') and `content` (string)

### ChatMessage
- `type` (string): Either 'ai' or 'user'
- `content` (string): The message text

### Footer
- `onSendMessage` (function): Callback when user sends a message, receives message content as parameter

## CSS Architecture

Each component has its own CSS file that matches the corresponding styles from `testing.css`. The CSS is scoped to each component for better maintainability.

## HTML-to-JSX Mapping

The JSX structure maps 1:1 to the HTML structure in `testing.html`:
- `class` → `className`
- Self-closing tags in JSX
- Camelcase event handlers (e.g., `onClick`, `onKeyDown`)

## Features

- ✅ Responsive design
- ✅ Gradient backgrounds
- ✅ Auto-expanding textarea
- ✅ Enter to send (Shift+Enter for new line)
- ✅ Message avatars with emojis
- ✅ Smooth animations
- ✅ Focus states for inputs

