import json
import os

# 1. Tentons d’ouvrir et chargeons un fichier JSON, puis retournons 'None' en cas d’erreur.
def charger_json_securise(chemin):
    file_name = os.path.basename(chemin)

    try:
        with open(chemin, 'r', encoding="utf-8") as f:
            content = f.read()
            if content:
                data = json.loads(content)
                print(f"✅ {file_name} chargé avec succès ({len(data['missions'])} missions).")
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
    # Cas 1 : fichier normal
    data = charger_json_securise("mission_data/missions.json")

    # # Cas 2 : fichier inexistant
    data = charger_json_securise("mission_data/fantome.json")

    # Cas 3 : créons un fichier corrompu pour tester
    with open("mission_data/corrompu.json", "w") as f:
        f.write("Corrompu { json }")
    data = charger_json_securise("mission_data/corrompu.json")


main()
