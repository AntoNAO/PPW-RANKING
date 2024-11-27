# PPW - Professional Pronostic Wrestling

Site web officiel du classement des pronostiqueurs WWE.

## 📊 Système de Points

### Points de Base (PLE Normal)
- Match normal = 1 point
- Prono bonus = 2 points
- Perfect score = +1 point bonus

### Points pour PLE Majeur
*(Détection automatique si le nom contient : WrestleMania, SummerSlam, Royal Rumble ou Survivor Series)*
- Match normal = 2 points
- Prono bonus = 4 points
- Perfect score = +2 points bonus

### Système de Streaks
- 3 bons pronos d'affilée = x2 sur le prochain (x4 pour PLE majeur)
- 2 mauvais pronos d'affilée = -0.5 sur le prochain (-1 pour PLE majeur)

## 🏆 Badges et Récompenses

### Badges de Performance
- 🔥 HOT_STREAK : 3 bonnes prédictions consécutives
- 🌟 ON_FIRE : 5 bonnes prédictions consécutives
- ❄️ ICE_COLD : 3 mauvaises prédictions consécutives
- 🎯 BONUS_MASTER : 3 pronos bonus corrects
- 🏆 MAJOR_PLAYER : Perfect sur un PLE majeur

### Badges des PLEs Majeurs
- 🎭 WRESTLEMANIA_SPECIALIST : Perfect score à WrestleMania
- 👑 RUMBLE_EXPERT : Prédiction correcte du vainqueur du Royal Rumble
- ☀️ SUMMERSLAM_MASTER : Perfect score à SummerSlam
- 🛡️ SURVIVOR_CHAMPION : Perfect score à Survivor Series

### Badges Spéciaux
- 🔄 COMEBACK_KID : Remontée de 3 places après une série de mauvais pronos
- 🌟 SEASON_CHAMPION : Premier du classement de la saison

## 📝 Guide d'Utilisation

### 1. Récupération des Pronostics
1. Ouvrir Google Forms
2. Aller dans "Réponses"
3. Cliquer sur les 3 points (...)
4. Sélectionner "Télécharger les réponses (.csv)"
5. Placer le fichier dans le dossier du projet
6. Renommer le fichier en `responses.csv`

### 2. Mise à Jour des Scores
1. Ouvrir un terminal
2. Naviguer vers le dossier du projet :
   ```
   cd c:/Users/Anto/CascadeProjects/wwe-betting-cards
   ```
3. Lancer le script :
   ```
   python update_scores.py
   ```

### 3. Saisie des Résultats
1. Entrer le nom exact du PLE (ex: "Royal Rumble 2024" ou "Elimination Chamber 2024")
   - Le système détecte automatiquement si c'est un PLE majeur selon le nom
2. Pour chaque match :
   - Match normal : `Roman Reigns vs Cody Rhodes`
   - Match bonus : `[BONUS] Qui va gagner le Royal Rumble`
3. Entrer le gagnant de chaque match
4. Taper `fin` quand tous les matches sont saisis
5. Confirmer avec 'o' pour mettre à jour

## ⚠️ Points Importants

1. **Noms des Joueurs**
   - Doivent être EXACTEMENT les mêmes dans Google Forms et rankings.json
   - Toujours en MAJUSCULES

2. **PLEs Majeurs**
   - Détection automatique si le nom contient :
     * WRESTLEMANIA
     * SUMMERSLAM
     * ROYAL RUMBLE
     * SURVIVOR SERIES
   - Peu importe les majuscules/minuscules

3. **Matches Bonus**
   - Toujours commencer par [BONUS]
   - Sensible aux espaces et à la casse

## 🗂️ Structure des Fichiers
```
ppw-rankings/
├── index.html          # Page principale du site
├── participate.html    # Page du formulaire de pronostics
├── rankings.json       # Données du classement
├── update_scores.py    # Script de mise à jour des scores
├── update_rankings.py  # Script de mise à jour du classement
└── achievements/       # Badges et récompenses
```

## 🆘 En Cas de Problème
1. Vérifier que responses.csv est bien placé
2. Vérifier les noms des joueurs (majuscules)
3. Vérifier la syntaxe des matches bonus
4. En cas d'erreur, ne pas valider et recommencer

## Comment héberger le site gratuitement

1. Créez un compte GitHub si vous n'en avez pas déjà un : https://github.com/signup

2. Créez un nouveau repository nommé `ppw-rankings`

3. Uploadez les fichiers suivants dans votre repository :
   - `index.html`
   - `rankings.json`
   - Le dossier `cards/` avec vos images
   
4. Allez dans les paramètres du repository :
   - Cliquez sur "Settings"
   - Descendez jusqu'à la section "GitHub Pages"
   - Dans "Source", sélectionnez "main"
   - Cliquez sur "Save"

5. Votre site sera disponible à l'adresse : `https://[votre-nom-utilisateur].github.io/ppw-rankings`

## Mise à jour du classement

1. Mettez à jour votre fichier Excel
2. Exécutez le script Python pour générer le nouveau `rankings.json`
3. Uploadez le nouveau `rankings.json` sur GitHub

## Changer le formulaire Google Forms

1. Créez votre nouveau formulaire Google Forms
2. Cliquez sur le bouton "Envoyer" (en haut à droite)
3. Dans la fenêtre qui s'ouvre, sélectionnez l'onglet "<>" (Intégrer)
4. Copiez l'URL qui se trouve dans le code d'intégration (entre les guillemets de `src="..."`)
5. Ouvrez le fichier `participate.html`
6. Trouvez la ligne qui commence par `<iframe src="`
7. Remplacez l'ancienne URL par la nouvelle
8. Si nécessaire, ajustez la hauteur du formulaire :
   - Trouvez la ligne `min-height: 2300px;` dans le CSS
   - Modifiez la valeur selon la taille de votre nouveau formulaire

Exemple de code à modifier dans participate.html :
```html
<iframe src="VOTRE_NOUVELLE_URL_ICI" frameborder="0" marginheight="0" marginwidth="0">Chargement…</iframe>
```

## Personnalisation

- Les images des cartes doivent être nommées exactement comme les noms des joueurs (espaces remplacés par _)
- L'image default.png sera utilisée si l'image d'un joueur n'est pas trouvée
- Le site se met à jour automatiquement toutes les 5 minutes
