import React, { useState } from 'react';
import "../assets/styles/UserSettings.css"


function UserSettings() {
  const [username, setUsername] = useState('JohnDoe');
  const [email, setEmail] = useState('john@example.com');

  const handleSave = (e) => {
    e.preventDefault();
    // Sauvegarder les données de l'utilisateur (à implémenter)
    alert('Paramètres sauvegardés');
  };

  return (
    <div className="settings-container">
      <h2>Paramètres utilisateur</h2>
      <form onSubmit={handleSave}>
        <div>
          <label>Nom d'utilisateur</label>
          <input 
            type="text" 
            value={username} 
            onChange={(e) => setUsername(e.target.value)} 
          />
        </div>
        <div>
          <label>Email</label>
          <input 
            type="email" 
            value={email} 
            onChange={(e) => setEmail(e.target.value)} 
          />
        </div>
        <button type="submit">Sauvegarder</button>
      </form>
    </div>
  );
}

export default UserSettings;
