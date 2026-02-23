"""Module pour la gestion des tâches liées aux missions."""

import json

# 1. Chargeons le fichier missions.json.
f = open('mission_data/missions.json', 'r', encoding="utf-8")
missions = json.loads(f.read())
print("✅ missions.json chargé avec succès")


# 2. Affichons un résumé de chaque mission sous cette forme :
for mission in missions["missions"]:
    print(f"[{mission['id']}] {mission['nom']} —→ {mission['destination']} | {mission['duree_jours']} jours | Equipage: {len(mission['equipage'])} | Budget: {mission['budget_millions_usd']} M$")

# 3. Affichons un résumé de chaque mission sous cette forme :
total_budget = sum(mission['budget_millions_usd'] for mission in missions["missions"])
print(f"\nBudget total de toutes les missions: {total_budget} M$")

# 4. Indiquons la mission la plus longue et la plus courte.
if missions["missions"]:
    LONGEST_MISSION = missions["missions"][0]
    SHORTEST_MISSION = missions["missions"][0]

    for mission in missions["missions"]:
        if mission['duree_jours'] > LONGEST_MISSION['duree_jours']:
            LONGEST_MISSION = mission
        if mission['duree_jours'] < SHORTEST_MISSION['duree_jours']:
            SHORTEST_MISSION = mission

    print(f"\nMission la plus longue : {LONGEST_MISSION['nom']} avec {LONGEST_MISSION['duree_jours']} jours")
    print(f"Mission la plus courte : {SHORTEST_MISSION['nom']} avec {SHORTEST_MISSION['duree_jours']} jours")