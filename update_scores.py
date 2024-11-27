import pandas as pd
import json
from datetime import datetime

# Liste des PLEs majeurs
MAJOR_PLES = ['WRESTLEMANIA', 'SUMMERSLAM', 'ROYAL RUMBLE', 'SURVIVOR SERIES']

# Configuration des badges
BADGES = {
    'PERFECT_SCORE': {
        'title': 'Perfect Score',
        'imageUrl': 'achievements/perfect.svg',
        'description': 'Prédictions parfaites sur un PLE'
    },
    'HOT_STREAK': {
        'title': 'Hot Streak',
        'imageUrl': 'achievements/hot_streak.svg',
        'description': '3 bonnes prédictions consécutives'
    },
    'ON_FIRE': {
        'title': 'On Fire',
        'imageUrl': 'achievements/on_fire.svg',
        'description': '5 bonnes prédictions consécutives'
    },
    'ICE_COLD': {
        'title': 'Ice Cold',
        'imageUrl': 'achievements/ice_cold.svg',
        'description': '3 mauvaises prédictions consécutives'
    },
    'WRESTLEMANIA_SPECIALIST': {
        'title': 'WrestleMania Specialist',
        'imageUrl': 'achievements/wrestlemania_specialist.svg',
        'description': 'Perfect score à WrestleMania'
    },
    'RUMBLE_EXPERT': {
        'title': 'Royal Rumble Expert',
        'imageUrl': 'achievements/rumble_expert.svg',
        'description': 'Prédiction correcte du vainqueur du Royal Rumble'
    },
    'SUMMERSLAM_MASTER': {
        'title': 'SummerSlam Master',
        'imageUrl': 'achievements/summerslam_master.svg',
        'description': 'Perfect score à SummerSlam'
    },
    'SURVIVOR_CHAMPION': {
        'title': 'Survivor Champion',
        'imageUrl': 'achievements/survivor_champion.svg',
        'description': 'Perfect score à Survivor Series'
    },
    'MONEY_IN_THE_BANK_MASTER': {
        'title': 'Mr. Money in the Bank',
        'imageUrl': 'achievements/money_in_the_bank.svg',
        'description': 'Plus grand nombre de points sur les PLEs Money in the Bank',
        'emoji': '💼',
        'aura': {
            'color': '#00A36C'
        }
    },
    'BONUS_MASTER': {
        'title': 'Bonus Master',
        'imageUrl': 'achievements/bonus_master.svg',
        'description': '3 prédictions bonus correctes'
    },
    'MAJOR_PLAYER': {
        'title': 'Major Player',
        'imageUrl': 'achievements/major_player.svg',
        'description': 'Perfect score sur un PLE majeur'
    },
    'COMEBACK_KID': {
        'title': 'Comeback Kid',
        'imageUrl': 'achievements/comeback_kid.svg',
        'description': 'Remontée de 3 places après une série de mauvais pronos'
    },
    'SEASON_CHAMPION': {
        'title': 'Season Champion',
        'imageUrl': 'achievements/season_champion.svg',
        'description': 'Premier du classement de la saison'
    }
}

def add_achievement(player, badge_key, date=None):
    """Ajoute un achievement au joueur s'il ne l'a pas déjà"""
    if date is None:
        date = datetime.now().strftime("%Y-%m-%d")
    
    badge = BADGES[badge_key].copy()
    badge['days'] = date
    
    # Vérifie si le joueur a déjà ce badge
    if not any(a['title'] == badge['title'] for a in player['achievements']):
        player['achievements'].append(badge)
        print(f"🏆 Nouveau badge pour {player['name']}: {badge['title']}")
        return True
    return False

def is_major_ple(ple_name):
    """Vérifie si c'est un PLE majeur"""
    return any(major.lower() in ple_name.lower() for major in MAJOR_PLES)

def calculate_match_points(is_correct, is_bonus, streak_multiplier, is_major_ple):
    """Calcule les points pour un match"""
    base_points = 2 if is_bonus else 1
    
    if is_major_ple:
        base_points *= 2
    
    if streak_multiplier > 1:
        return base_points * streak_multiplier
    elif streak_multiplier < 1:
        penalty = -1 if is_major_ple else -0.5
        return max(base_points + penalty, 0)
    
    return base_points

def check_achievements(player, response, results, is_major, ple_name, bonus_matches):
    """Vérifie et attribue les achievements"""
    # Vérification des streaks
    if player['streak_history'].get('good_streak', 0) >= 3:
        add_achievement(player, 'HOT_STREAK')
    if player['streak_history'].get('good_streak', 0) >= 5:
        add_achievement(player, 'ON_FIRE')
    if player['streak_history'].get('bad_streak', 0) >= 3:
        add_achievement(player, 'ICE_COLD')
    
    # Vérification des bonus
    bonus_correct = 0
    for match in bonus_matches:
        if str(response[match]).strip().lower() == str(results[match]).strip().lower():
            bonus_correct += 1
    if bonus_correct >= 3:
        add_achievement(player, 'BONUS_MASTER')
    
    # Vérification des achievements spéciaux
    if is_major:
        # Perfect sur PLE majeur
        all_correct = all(str(response[match]).strip().lower() == str(results[match]).strip().lower() 
                         for match in results.keys())
        if all_correct:
            add_achievement(player, 'MAJOR_PLAYER')
            
            # Achievements spécifiques aux PLEs
            if 'WRESTLEMANIA' in ple_name.upper():
                add_achievement(player, 'WRESTLEMANIA_SPECIALIST')
            elif 'ROYAL RUMBLE' in ple_name.upper():
                for match in results.keys():
                    if 'RUMBLE' in match.upper() and str(response[match]).strip().lower() == str(results[match]).strip().lower():
                        add_achievement(player, 'RUMBLE_EXPERT')
            elif 'SUMMERSLAM' in ple_name.upper():
                add_achievement(player, 'SUMMERSLAM_MASTER')
            elif 'SURVIVOR SERIES' in ple_name.upper():
                add_achievement(player, 'SURVIVOR_CHAMPION')
    
    # Vérification du Comeback Kid
    if ('previous_rank' in player and 
        player['previous_rank'] - player['rank'] >= 3 and 
        player['streak_history'].get('bad_streak', 0) > 0):
        add_achievement(player, 'COMEBACK_KID')
    
    # Attribution du badge Mr. Money in the Bank à Jason
    if player['name'].upper() == 'JASON':
        add_achievement(player, 'MONEY_IN_THE_BANK_MASTER')

def calculate_points(row, results, bonus_matches, player_history, is_major):
    """Calcule les points pour une ligne de réponses"""
    points = 0
    correct_count = 0
    total_matches = len(results)
    
    good_streak = player_history.get('good_streak', 0)
    bad_streak = player_history.get('bad_streak', 0)
    
    multiplier = 1
    if good_streak >= 3:
        multiplier = 4 if is_major else 2
    elif bad_streak >= 2:
        multiplier = 0.5
    
    for match, result in results.items():
        is_bonus = match in bonus_matches
        is_correct = str(row[match]).strip().lower() == str(result).strip().lower()
        
        if is_correct:
            match_points = calculate_match_points(True, is_bonus, multiplier, is_major)
            points += match_points
            correct_count += 1
            good_streak += 1
            bad_streak = 0
        else:
            good_streak = 0
            bad_streak += 1
    
    if correct_count == total_matches:
        perfect_bonus = 2 if is_major else 1
        points += perfect_bonus
    
    player_history['good_streak'] = good_streak
    player_history['bad_streak'] = bad_streak
    
    return points, correct_count == total_matches

def load_responses(csv_path):
    """Charge les réponses depuis le fichier CSV"""
    try:
        print(f"Chargement du fichier {csv_path}...")
        df = pd.read_csv(csv_path)
        print(f"Fichier chargé avec succès! ({len(df)} réponses trouvées)")
        return df
    except FileNotFoundError:
        print(f"Le fichier {csv_path} n'a pas été trouvé!")
        return None
    except Exception as e:
        print(f"Erreur lors de la lecture du CSV : {str(e)}")
        return None

def update_rankings(responses, results, ple_name, bonus_matches):
    """Met à jour le fichier rankings.json avec les nouveaux scores"""
    try:
        is_major = is_major_ple(ple_name)
        print(f"Type de PLE: {'Majeur' if is_major else 'Normal'}")
        
        with open('rankings.json', 'r', encoding='utf-8') as f:
            rankings = json.load(f)
        print("Fichier rankings.json chargé avec succès!")
        
        rankings_dict = {player['name']: player for player in rankings}
        
        # Sauvegarder les rangs précédents
        for player in rankings:
            player['previous_rank'] = player['rank']
            if 'streak_history' not in player:
                player['streak_history'] = {'good_streak': 0, 'bad_streak': 0}
        
        perfect_scores = []
        print("\nTraitement des réponses...")
        
        for _, response in responses.iterrows():
            player_name = response['Nom']
            
            if player_name in rankings_dict:
                player = rankings_dict[player_name]
                
                points, is_perfect = calculate_points(
                    response, 
                    results, 
                    bonus_matches,
                    player['streak_history'],
                    is_major
                )
                
                player['seasonPoints'] += points
                player['totalPoints'] += points
                player['plePoints'] = points
                
                ple_entry = {
                    "name": ple_name,
                    "points": points
                }
                player['pleHistory'].append(ple_entry)
                
                print(f"{player_name}: {points} points")
                
                if is_perfect:
                    perfect_scores.append(player_name)
                    add_achievement(player, 'PERFECT_SCORE')
                
                # Vérifier les autres achievements
                check_achievements(player, response, results, is_major, ple_name, bonus_matches)
        
        # Recalculer les rangs
        print("\nMise à jour des classements...")
        sorted_players = sorted(rankings, key=lambda x: x['seasonPoints'], reverse=True)
        for i, player in enumerate(sorted_players, 1):
            player['rank'] = i
        
        # Vérifier le Season Champion
        if sorted_players:
            add_achievement(sorted_players[0], 'SEASON_CHAMPION')
        
        # Sauvegarder
        print("Sauvegarde des modifications...")
        with open('rankings.json', 'w', encoding='utf-8') as f:
            json.dump(rankings, f, ensure_ascii=False, indent=2)
        
        # Afficher le résumé
        print("\nRésumé des mises à jour")
        print(f"PLE: {ple_name} ({'Majeur' if is_major else 'Normal'})")
        
        if perfect_scores:
            print("\nPerfect Scores:")
            for player in perfect_scores:
                print(f"⭐ {player}")
        
        print("\nTop 3 actuel:")
        for i, player in enumerate(sorted_players[:3], 1):
            print(f"{i}. {player['name']} - {player['seasonPoints']} points")
            
        print("\nMise à jour terminée avec succès!")
        
    except Exception as e:
        print(f"Erreur lors de la mise à jour : {str(e)}")

def main():
    print("WWE BETTING RANKING SYSTEM")
    print("=========================\n")
    
    csv_path = 'responses.csv'
    ple_name = input("Nom du PLE (ex: Royal Rumble 2024): ")
    
    print("\nSaisie des résultats")
    print("Entrez les résultats des matches (tapez 'fin' pour terminer)")
    print("Pour un prono bonus, ajoutez '[BONUS]' au début du nom du match")
    
    results = {}
    bonus_matches = set()
    match_num = 1
    
    while True:
        match_name = input(f"\nMatch #{match_num} (ou 'fin' pour terminer): ")
        if match_name.lower() == 'fin':
            break
            
        if match_name.upper().startswith('[BONUS]'):
            bonus_matches.add(match_name)
            print("(Match Bonus)")
            
        winner = input(f"Gagnant de {match_name}: ")
        results[match_name] = winner
        match_num += 1
    
    if not results:
        print("Aucun résultat saisi!")
        return
    
    print("\nRécapitulatif des matches:")
    for match, winner in results.items():
        match_type = "(BONUS)" if match in bonus_matches else "(Normal)"
        print(f"{match} {match_type}: {winner}")
    
    confirm = input("\nConfirmer la mise à jour ? (o/n): ").lower()
    if confirm != 'o':
        print("Mise à jour annulée!")
        return
    
    responses = load_responses(csv_path)
    if responses is not None:
        update_rankings(responses, results, ple_name, bonus_matches)

if __name__ == '__main__':
    main()
