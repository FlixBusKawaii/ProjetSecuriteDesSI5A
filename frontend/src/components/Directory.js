import React from 'react';
import "../assets/styles/Directory.css"

function Directory({ contacts }) {
  if (!contacts.length) {
    return <p>Aucun contact trouvé.</p>;
  }

  return (
    <div className="directory-container">
      <ul>
        {contacts.map((contact) => (
          <li key={contact.id}>
            <strong>{contact.name}</strong> - {contact.phone} - {contact.email}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Directory;
