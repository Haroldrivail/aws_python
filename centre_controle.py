"""Module pour la gestion du centre de contrôle des missions spatiales."""

import os
import json
from navigation import charger_corps_celestes, poids_sur_corps
import exceptions
from tache6 import ajouter_mission, supprimer_mission

# Programme centre_controle.py qui fonctionne comme
#  un tableau de bord interactif en ligne de commande :

# 1. Option 1 : Charger et afficher missions.json (réutiliser Tâche 3).
f = open('mission_data/missions.json', 'r', encoding="utf-8")
missions = json.loads(f.read())
print("✅ missions.json chargé avec succès")

# 2. Option 2 : Demander un ID et afficher tous les détails, incluant
#le poids d’un astronaute de 80 kg sur la destination
#  (utiliser navigation.py et corps_celestes.json).
ID = input("\nEntrez l'ID de la mission pour voir les détails : ")
corps = charger_corps_celestes()
mission = next((m for m in missions["missions"] if m['id'] == ID), None)
if mission:
    print(f"[{mission['id']}] {mission['nom']} → {mission['destination']} \
        | {mission['duree_jours']} jours | Equipage: {len(mission['equipage'])} \
            | Budget: {mission['budget_millions_usd']} M$")
    # Trouver la gravité de la destination
    destination_info = next((corp for corp in corps if corp['nom'] == mission['destination']), None)
    if destination_info:
        gravite = destination_info['gravite_m_s2']
        poids_astronaute = poids_sur_corps(80, gravite)
        print(f"Poids d'un astronaute (80 kg) sur \
            {mission['destination']} : {poids_astronaute:.1f} N")
    else:
        print("Gravité de la destination inconnue.")

# 3. Option 3 : Saisie interactive + validation (réutiliser Tâches 6 et 9).
nouvelle_mission = {
    "id": "MSN-006",
    "nom": "Proxima Relay",
    "destination": "Alpha Centauri (sonde)",
    "date_lancement": "2035-06-01",
    "statut": "théorique",
    "equipage": [],
    "duree_jours": 29200,
    "budget_millions_usd": 125000
}

supprimer_mission('mission_data/missions.json', nouvelle_mission['id'])

try:
    exceptions.valider_mission(nouvelle_mission)
    print("✅ Mission valide")
    ajouter_mission('mission_data/missions.json', nouvelle_mission)
except exceptions.CarburantError as e:
    print(f"🔴 {e}")
except exceptions.TrajectoireError as e:
    print(f"❌ {type(e).__name__}: {e}")
except exceptions.MissionDataError as e:
    print(f"❌ {type(e).__name__}: {e}")
except exceptions.NavigationError as e:
    print(f"❌ {type(e).__name__}: {e}")

# 4. Option 4 : Afficher le dernier relevé de telemetrie.json
# avec indicateurs colorés :🟢 Carburant > 50%, 🟡 entre 20-50%, 🔴 < 20%.
# Chargeons les fichier telemetrie.json et écrivons un script qui :
CHEMIN = 'mission_data/telemetrie.json'
file_name = os.path.basename(CHEMIN)
ALERTE_PATH = 'mission_data/rapports/alertes_systemes.json'

try:
    with open(CHEMIN, 'r', encoding="utf-8") as f:
        content = f.read()
        if content:
            data = json.loads(content)
            print(f"✅ {file_name} chargé avec succès.\n")
            dernier_releve = data['releves'][-1]
        else:
            print(f"Fichier '{file_name}' vide.")
except FileNotFoundError:
    print(f"Fichier introuvable : {CHEMIN}")
except json.JSONDecodeError as e:
    print(f"JSON invalide dans {CHEMIN} : {e}")
except KeyError as e:
    print(f"Clé manquante dans le JSON: {e}")
    print("Veuillez vérifier la structure du fichier JSON.")


# 5. Option 5 : Calculateur utilisant navigation.py — l’utilisateur
# choisit départ et arrivée, le programme affiche distance, temps de trajet estimé et delta-v.

# 6. Option 6 : Scanner toute la télémétrie et lister les anomalies (réutiliser Tâche 7).

# 7. Option 7 : Recherche par mot-clé dans journal_bord.txt (réutiliser Tâche 1).

# 8. Option 8 : Générer mission_data/rapports/rapport_complet.json
# contenant un résumé de toutes les missions, les alertes, et les statistiques.

# 9. Option 9 : Afficher l’arborescence complète de mission_data/ avec os (réutiliser Tâche 2).
