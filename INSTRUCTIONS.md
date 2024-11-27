# Guide d'utilisation - Système de Points PPW

## 🎯 Règles de Points

### Points de Base (PLE Normal)
- Match normal = 1 point
- Prono bonus = 2 points
- Perfect score = +1 point bonus

### Points pour PLE Majeur
*(WrestleMania, SummerSlam, Royal Rumble, Survivor Series)*
- Match normal = 2 points
- Prono bonus = 4 points
- Perfect score = +2 points bonus

### Système de Streaks
- 3 bons pronos d'affilée = x2 sur le prochain (x4 pour PLE majeur)
- 2 mauvais pronos d'affilée = -0.5 sur le prochain (-1 pour PLE majeur)

## 📝 Étapes d'Utilisation

### 1. Préparation
1. Ouvrir Google Forms
2. Aller dans "Réponses"
3. Cliquer sur les 3 points (...)
4. Sélectionner "Télécharger les réponses (.csv)"
5. Placer le fichier dans le dossier du projet
6. Renommer le fichier en `responses.csv`

### 2. Lancement du Script
1. Ouvrir un terminal (PowerShell ou CMD)
2. Naviguer vers le dossier du projet :
   ```
   cd c:/Users/Anto/CascadeProjects/wwe-betting-cards
   ```
3. Lancer le script :
   ```
   python update_scores.py
   ```

### 3. Utilisation du Script

#### A. Nom du PLE
- Entrer le nom exact du PLE
- Le script détecte automatiquement s'il s'agit d'un PLE majeur

#### B. Saisie des Matches
Pour chaque match :
1. Entrer le nom du match
   - Match normal : `Roman Reigns vs Cody Rhodes`
   - Match bonus : `[BONUS] Qui va gagner le Royal Rumble`
2. Entrer le gagnant
3. Répéter pour tous les matches
4. Taper `fin` quand terminé

#### C. Vérification
1. Le script affiche un récapitulatif
2. Confirmer avec 'o' pour mettre à jour
3. Ou 'n' pour annuler

### 4. Résultats
Le script affichera :
- Les points gagnés par chaque joueur
- Les perfect scores
- Le nouveau top 3
- Les streaks mises à jour

## ⚠️ Points Importants

1. **Noms des Joueurs**
   - Doivent être EXACTEMENT les mêmes dans Google Forms et rankings.json
   - Toujours en MAJUSCULES

2. **PLEs Majeurs**
   - Doivent contenir un de ces mots dans leur nom :
     * WRESTLEMANIA
     * SUMMERSLAM
     * ROYAL RUMBLE
     * SURVIVOR SERIES

3. **Matches Bonus**
   - Toujours commencer par [BONUS]
   - Sensible aux espaces et à la casse

4. **Sauvegarde**
   - Le script met à jour automatiquement rankings.json
   - Les changements sont visibles immédiatement sur le site

## 🆘 En Cas de Problème

1. Vérifier que responses.csv est bien placé
2. Vérifier les noms des joueurs (majuscules)
3. Vérifier la syntaxe des matches bonus
4. En cas d'erreur, ne pas valider et recommencer
