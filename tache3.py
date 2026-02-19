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
longest_mission = None
shortest_mission = None

for mission in missions["missions"]:
    if longest_mission is None or mission['duree_jours'] > longest_mission['duree_jours']:
        longest_mission = mission
    if shortest_mission is None or mission['duree_jours'] < shortest_mission['duree_jours']:
        shortest_mission = mission

print(f"\nMission la plus longue : {longest_mission['nom']} avec {longest_mission['duree_jours']} jours")
print(f"Mission la plus courte : {shortest_mission['nom']} avec {shortest_mission['duree_jours']} jours")