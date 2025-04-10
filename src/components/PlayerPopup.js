import React, { useState } from 'react';

function PlayerPopup({ player, onUpdateTitleCount }) {
    const [titleCount, setTitleCount] = useState(player.titleCount);

    const handleChange = (e) => {
        setTitleCount(e.target.value);
    };

    const handleSave = () => {
        onUpdateTitleCount(player.id, parseInt(titleCount, 10));
    };

    return (
        <div className="popup">
            <h2>{player.name}</h2>
            <p>Nombre de titres :</p>
            <input
                type="number"
                value={titleCount}
                onChange={handleChange}
            />
            <button onClick={handleSave}>Enregistrer</button>
        </div>
    );
}

export default PlayerPopup;