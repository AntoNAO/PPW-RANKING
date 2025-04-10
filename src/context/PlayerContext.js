import React, { createContext, useState } from 'react';

export const PlayerContext = createContext();

export const PlayerProvider = ({ children }) => {
    const [players, setPlayers] = useState([]);

    const updateTitleCount = (playerId, newCount) => {
        setPlayers((prevPlayers) =>
            prevPlayers.map((player) =>
                player.id === playerId ? { ...player, titleCount: newCount } : player
            )
        );
    };

    return (
        <PlayerContext.Provider value={{ players, updateTitleCount }}>
            {children}
        </PlayerContext.Provider>
    );
};