import React from 'react';
import "../assets/styles/AdminPanel.css"

function AdminPanel({ contacts, onAdd, onDelete }) {
  const handleDelete = (id) => {
    onDelete(id);
  };

  return (
    <div className="admin-container">
      <h2>Panneau d'administration</h2>
      <button onClick={onAdd}>Ajouter un contact</button>
      <ul>
        {contacts.map((contact) => (
          <li key={contact.id}>
            <strong>{contact.name}</strong> - {contact.phone} - {contact.email}
            <button onClick={() => handleDelete(contact.id)}>Supprimer</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default AdminPanel;
