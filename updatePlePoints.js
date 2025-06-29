const fs = require('fs');
const filePath = './rankings.json';

// Liste des mises à jour pour chaque joueur
const updates = [
    { name: 'JASON', plePoints: 0, seasonPoints: 9, totalPoints: 112 },
    { name: 'SHOOOTIX', plePoints: 0, seasonPoints: 0, totalPoints: 0 },
    { name: 'BLEMZER', plePoints: 0, seasonPoints: 0, totalPoints: 0 },
    { name: 'NEOZY', plePoints: 0, seasonPoints: 0, totalPoints: 0 },
    { name: 'ANTO', plePoints: 0, seasonPoints: 13, totalPoints: 116 },
    { name: 'QUENTIN', plePoints: 0, seasonPoints: 9, totalPoints: 108 },
    { name: 'BRANDON', plePoints: 0, seasonPoints: 6, totalPoints: 96 },
    { name: 'AURELIEN', plePoints: 0, seasonPoints: 17, totalPoints: 0 },
    { name: 'MATHIS', plePoints: 1, seasonPoints: 9, totalPoints: 110 },
    { name: 'NEK', plePoints: 0, seasonPoints: 8, totalPoints: 107 },
    { name: 'NATHAN', plePoints: 0, seasonPoints: 4, totalPoints: 71 },
    { name: 'ONI', plePoints: 0, seasonPoints: 0, totalPoints: 54 },
    { name: 'MIZOU', plePoints: 0, seasonPoints: 7, totalPoints: 0 },
    { name: 'BEN', plePoints: 0, seasonPoints: 0, totalPoints: 38 },
    { name: 'LUDOPOUL', plePoints: 0, seasonPoints: 0, totalPoints: 56 },
    { name: 'RYOLAIT12', plePoints: 0, seasonPoints: 0, totalPoints: 29 },
    { name: 'ELCHAPO', plePoints: 0, seasonPoints: 3, totalPoints: 10 },
    { name: 'PETRELOU', plePoints: 0, seasonPoints: 4, totalPoints: 21 },
    { name: 'ANGELITO', plePoints: 0, seasonPoints: 8, totalPoints: 8 },
    { name: 'FLO', plePoints: 0, seasonPoints: 9, totalPoints: 8 },
];

// Charger le fichier JSON
fs.readFile(filePath, 'utf8', (err, data) => {
    if (err) {
        console.error('Erreur lors de la lecture du fichier:', err);
        return;
    }

    // Parse le contenu JSON
    let rankings = JSON.parse(data);

    // Appliquer les mises à jour
    updates.forEach(update => {
        let player = rankings.find(p => p.name === update.name);
        if (player) {
            if (update.plePoints !== undefined) player.plePoints = update.plePoints;
            if (update.seasonPoints !== undefined) player.seasonPoints = update.seasonPoints;
            if (update.totalPoints !== undefined) player.totalPoints = update.totalPoints;
            console.log(`Mise à jour pour ${update.name} : PLE=${update.plePoints}, Saison=${update.seasonPoints}, Total=${update.totalPoints}`);
        } else {
            console.error(`Joueur "${update.name}" introuvable dans le fichier.`);
        }
    });

    // Trier et réattribuer les rangs
    rankings.sort((a, b) => b.seasonPoints - a.seasonPoints);
    rankings.forEach((player, index) => {
        player.rank = index + 1;
    });

    // Sauvegarder les modifications dans le fichier JSON
    fs.writeFile(filePath, JSON.stringify(rankings, null, 2), 'utf8', err => {
        if (err) {
            console.error('Erreur lors de l\'écriture du fichier:', err);
            return;
        }
        console.log('Fichier rankings.json mis à jour avec succès !');
    });
});