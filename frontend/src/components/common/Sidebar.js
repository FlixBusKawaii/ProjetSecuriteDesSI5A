import React, { useState, useEffect } from 'react';
import '../../assets/styles/Sidebar.css';


const Sidebar = ({ onNavigate }) => {
  const [isVisible, setIsVisible] = useState(false);

  useEffect(() => {
    const handleMouseMove = (event) => {
      if (event.clientX <= 10) {
        setIsVisible(true);
      }
    };

    document.addEventListener('mousemove', handleMouseMove);
    return () => {
      document.removeEventListener('mousemove', handleMouseMove);
    };
  }, []);

  const handleMouseLeave = () => {
    setIsVisible(false);
  };

  return (
    <div 
      className={`sidebar ${isVisible ? 'visible' : ''}`}
      onMouseLeave={handleMouseLeave}
    >
      <h2>Sidebar</h2>
      <ul>
        <li>
          <button onClick={() => onNavigate('directory')}>Annuaire</button>
        </li>
        <li>
          <button onClick={() => onNavigate('settings')}>Paramètres</button>
        </li>
        <li>
          <button onClick={() => onNavigate('admin')}>Administration</button>
        </li>
      </ul>
    </div>
  );
};

export default Sidebar;