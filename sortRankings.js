const fs = require('fs');
const filePath = './rankings.json';

// Charger le fichier JSON
fs.readFile(filePath, 'utf8', (err, data) => {
    if (err) {
        console.error('Erreur lors de la lecture du fichier:', err);
        return;
    }

    // Parse le contenu JSON
    let rankings = JSON.parse(data);

    // Trier les joueurs par points de saison (seasonPoints) décroissants
    rankings.sort((a, b) => b.seasonPoints - a.seasonPoints);

    // Réattribuer les rangs en fonction du nouvel ordre
    rankings.forEach((player, index) => {
        player.rank = index + 1;
    });

    // Sauvegarder le fichier trié
    fs.writeFile(filePath, JSON.stringify(rankings, null, 2), 'utf8', err => {
        if (err) {
            console.error('Erreur lors de l\'écriture du fichier:', err);
            return;
        }
        console.log('Fichier rankings.json trié avec succès par seasonPoints !');
    });
});