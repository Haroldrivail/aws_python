"""Module pour la gestion des tâches liées à l'analyse de la télémétrie d'une mission spatiale."""
import json
import os

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

            # 1. Affiche un tableau resume de chaque telemetrie
            print('Phase                | Altitude        | Vitesse   | Carburant |')
            print('---------------------|-----------------|-----------|-----------|--------')
            for telemetrie in data['releves']:
                phase = telemetrie['phase']
                ALTITUDE = f"{telemetrie['altitude_km']} km"
                VITESSE = f"{telemetrie['vitesse_km_s']} km/s"
                CARBURANT = f"{telemetrie['carburant_pct']}%"
                print(f'{phase:<20} | {ALTITUDE:<15} | {VITESSE:<9} | {CARBURANT:<9} |')

            # 2. Calcule la consommation moyenne de carburant par jour entre
            # le premier et le dernier relevé.
            moyenne_carburant_jour = sum((telemetrie['carburant_pct']) 
                                         / len(data['releves']) for telemetrie in data['releves'])
            print(f"\nLa consommation moyenne de carburant par \
                  jour entre le premier et le dernier relevé est {moyenne_carburant_jour}\n")

            alertes = []
            with open(ALERTE_PATH, 'w', encoding="utf-8") as json_file:
                # 3. Identifie tous les relevés contenant au moins une
                # alerte (systèmes ≠ "nominal").
                for telemetrie in data['releves']:
                    if telemetrie['systemes']['propulsion'] != "nominal":
                        print(f"Alerte détectée lors de la phase \
                            '{telemetrie['phase']}' (propulsion \
                                : {telemetrie['systemes']['propulsion']})")
                        alertes.append(f"Alerte détectée lors de la phase \
                             '{telemetrie['phase']}' (propulsion \
                             : {telemetrie['systemes']['propulsion']})")
                    elif telemetrie['systemes']['support_vie'] != "nominal":
                        print(f"Alerte détectée lors de la phase \
                             '{telemetrie['phase']}' (support_vie \
                             : {telemetrie['systemes']['support_vie']})")
                        alertes.append(f"Alerte détectée lors de la phase \
                             '{telemetrie['phase']}' (support_vie \
                             : {telemetrie['systemes']['support_vie']})")
                    elif telemetrie['systemes']['navigation'] != "nominal":
                        print(f"Alerte détectée lors de la phase \
                             '{telemetrie['phase']}' (navigation \
                             : {telemetrie['systemes']['navigation']})")
                        alertes.append(f"Alerte détectée lors de la phase \
                             '{telemetrie['phase']}' (navigation \
                             : {telemetrie['systemes']['navigation']})")
                    elif telemetrie['systemes']['communication'] != "nominal":
                        print(f"Alerte détectée lors de la phase \
                             '{telemetrie['phase']}' (communication \
                             : {telemetrie['systemes']['communication']})")
                        alertes.append(f"Alerte détectée lors de la phase \
                             '{telemetrie['phase']}' (communication \
                             : {telemetrie['systemes']['communication']})")

                # 4. Sauvegarde la liste des alertes dans
                # mission_data/rapports/alertes_systemes.json.
                json.dump({"alertes": alertes}, json_file, indent=2)
                if alertes:
                    print(f"\n✅ Alertes sauvegardées dans '{ALERTE_PATH}'")
                else:
                    print(f"\nAucune alerte détectée, fichier \
                        '{ALERTE_PATH}' créé avec une liste vide.")
        else:
            print(f"Fichier '{file_name}' vide.")
except FileNotFoundError:
    print(f"Fichier introuvable : {CHEMIN}")
except json.JSONDecodeError as e:
    print(f"JSON invalide dans {CHEMIN} : {e}")
except KeyError as e:
    print(f"Clé manquante dans le JSON: {e}")
    print("Veuillez vérifier la structure du fichier JSON.")
