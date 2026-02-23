"""Module pour la gestion des tâches liées à l'ajout \
    et à la suppression de missions dans un fichier JSON."""

import json

# Écrivez une fonction ajouter_mission(chemin_json, nouvelle_mission) qui :

def ajouter_mission(chemin_json, nouvelle_mission):
    """Ajoute une nouvelle mission à un fichier JSON.

    Args:
        chemin_json (str): Chemin vers le fichier JSON contenant les missions.
        nouvelle_mission (dict): Dictionnaire contenant les informations de la nouvelle mission.

    Raises:
        ValueError: Si une mission avec le même ID existe déjà.
    """
    # 1.Charge les missions existantes.
    with open(chemin_json, 'r', encoding='utf-8') as json_file:
        missions = json.loads(json_file.read())
    # 2.Vérifie que l’id de la nouvelle mission n’existe pas déjà (sinon lève une ValueError).
    for mission in missions['missions']:
        if mission['id'] == nouvelle_mission['id']:
            raise ValueError(f"Une mission avec l'id {nouvelle_mission['id']} existe déjà.")
    # 3.Ajoute la mission à la liste.
    missions['missions'].append(nouvelle_mission)

    # 4.Sauvegarde le fichier JSON avec une indentation propre (indent=2).
    with open(chemin_json, 'w', encoding='utf-8') as json_file:
        json.dump(missions, json_file, ensure_ascii=False, indent=2)

    # 5.Ajoute un message de confirmation indiquant que la mission a été ajoutée avec succès.
    print(f"La mission avec l'id {nouvelle_mission['id']} a été ajoutée avec succès.")

def supprimer_mission(chemin_json, id_mission):
    """Supprime une mission d'un fichier JSON.

    Args:
        chemin_json (str): Chemin vers le fichier JSON contenant les missions.
        id_mission (str): ID de la mission à supprimer.

    Raises:
        ValueError: Si aucune mission avec l'ID spécifié n'existe.
    """
    # Chargeons les missions existantes.
    with open(chemin_json, 'r', encoding='utf-8') as json_file:
        missions = json.loads(json_file.read())
    # 2.Vérifions que l’id de la mission à supprimer existe (sinon lèvons une ValueError).
    mission_existe = False
    for mission in missions['missions']:
        if mission['id'] == id_mission:
            mission_existe = True
            break
    if not mission_existe:
        raise ValueError(f"Aucune mission avec l'id {id_mission} n'existe.")
    # 3.Supprimons la mission de la liste.
    missions['missions'] = [mission for mission in \
        missions['missions'] if mission['id'] != id_mission]

    # 4.Sauvegardons le fichier JSON avec une indentation propre (indent=2).
    with open(chemin_json, 'w', encoding='utf-8') as json_file:
        json.dump(missions, json_file, ensure_ascii=False, indent=2)

    # 5.Ajoutons un message de confirmation indiquant que la mission a été supprimée avec succès.
    print(f"La mission avec l'id {id_mission} a été supprimée avec succès.")


nouvelle = {
    "id": "MSN-006",
    "nom": "Proxima Relay",
    "destination": "Alpha Centauri (sonde)",
    "date_lancement": "2035-06-01",
    "statut": "théorique",
    "equipage": [],
    "duree_jours": 29200,
    "budget_millions_usd": 125000
}

ajouter_mission('mission_data/missions.json', nouvelle)
supprimer_mission('mission_data/missions.json', nouvelle['id'])
