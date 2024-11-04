import React, { useState } from 'react';
import Login from './components/Login';
import Directory from './components/Directory';
import UserSettings from './components/UserSettings';
import AdminPanel from './components/AdminPanel';
import Sidebar from './components/common/Sidebar';
import Header from './components/common/Header'; // Importez le composant Header
import './App.css';

function App() {
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [currentPage, setCurrentPage] = useState('login');
  const [contacts, setContacts] = useState([
    { id: 1, name: 'John Doe', phone: '123-456-7890', email: 'john@example.com' },
    { id: 2, name: 'Jane Smith', phone: '987-654-3210', email: 'jane@example.com' }
  ]);

  const handleLogin = () => {
    setIsLoggedIn(true);
    setCurrentPage('directory');
  };

  const handleAddContact = () => {
    const newContact = { id: contacts.length + 1, name: 'New Contact', phone: '000-000-0000', email: 'new@example.com' };
    setContacts([...contacts, newContact]);
  };

  const handleDeleteContact = (id) => {
    setContacts(contacts.filter(contact => contact.id !== id));
  };

  const handleNavigate = (page) => {
    setCurrentPage(page);
  };

  if (!isLoggedIn) {
    return <Login onLogin={handleLogin} />;
  }

  return (
    <div className="App">
      <Header />
      <Sidebar onNavigate={handleNavigate} />
      <div className="content">
        {currentPage === 'directory' && <Directory contacts={contacts} />}
        {currentPage === 'settings' && <UserSettings />}
        {currentPage === 'admin' && (
          <AdminPanel
            contacts={contacts}
            onAdd={handleAddContact}
            onDelete={handleDeleteContact}
          />
        )}
      </div>
    </div>
  );
}

export default App;
