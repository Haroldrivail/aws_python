"""Module pour la gestion des tâches liées au chargement sécurisé de fichiers JSON."""

import json
import os

# 1. Tentons d’ouvrir et chargeons un fichier JSON, puis retournons 'None' en cas d’erreur.
def charger_json_securise(chemin):
    """Charge un fichier JSON de manière sécurisée, en gérant les erreurs courantes."""
    file_name = os.path.basename(chemin)

    try:
        with open(chemin, 'r', encoding="utf-8") as f:
            content = f.read()
            if content:
                data = json.loads(content)
                print(f"✅ {file_name} chargé avec succès.")
                return data
            else:
                print(f"Fichier '{file_name}' vide.")
                return None
    except FileNotFoundError:
        print(f"Fichier introuvable : {chemin}")
        return None
    except json.JSONDecodeError as e:
        print(f"JSON invalide dans {chemin} : {e}")
        return None
    except KeyError as e:
        print(f"Clé manquante dans le JSON: {e}")
        return None
# Testons la fonction avec différents scénarios
def main():
    """Test de la fonction charger_json_securise avec différents scénarios."""

    # Cas 1 : fichier normal
    charger_json_securise("mission_data/missions.json")

    # # Cas 2 : fichier inexistant
    charger_json_securise("mission_data/fantome.json")

    # Cas 3 : créons un fichier corrompu pour tester
    with open("mission_data/corrompu.json", "w", encoding="utf-8") as f:
        f.write("Corrompu { json }")
    charger_json_securise("mission_data/corrompu.json")


main()
