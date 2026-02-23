# --- navigation.py ---

import json
import math
import os

def distance_interplanetaire(corps1, corps2, donnees_corps):
    """
    Calcule la distance approximative entre deux corps célestes
    basée sur leur distance au Soleil (en millions de km).
    Retourne la valeur absolue de la différence.
    """
    for corp in donnees_corps:
        if corp['nom'] == corps1:
            distance1 = corp['distance_soleil_mkm']
        if corp['nom'] == corps2:
            distance2 = corp['distance_soleil_mkm']
    return abs(distance1 - distance2)
    

def temps_trajet(distance_mkm, vitesse_km_s):
    """
    Calcule le temps de trajet en jours.
    distance en millions de km, vitesse en km/s.
    """
    distance_km = distance_mkm * 1000000
    temps_secondes = distance_km / vitesse_km_s
    temps_jours = (int)(math.ceil(temps_secondes / (60 * 60 * 24)))
    return temps_jours

def delta_v(gravite_depart, gravite_arrivee, altitude_orbite_km):
    """
    Estimation simplifiée du delta-v nécessaire (en km/s).
    Formule simplifiée : sqrt(2 * g_depart * alt) + sqrt(2 * g_arrivee * alt)
    (les altitudes sont converties en mètres)
    """
    alt_m = altitude_orbite_km * 1000
    delta_v_depart = math.sqrt(2 * gravite_depart * alt_m)
    delta_v_arrivee = math.sqrt(2 * gravite_arrivee * alt_m)
    return delta_v_depart + delta_v_arrivee

def poids_sur_corps(masse_kg, gravite_m_s2):
    """Calcule le poids (en Newtons) sur un corps céleste."""
    return masse_kg * gravite_m_s2

def charger_corps_celestes(chemin="mission_data/corps_celestes.json"):
    """Charge le fichier des corps célestes avec gestion d'erreur."""
    file_name = os.path.basename(chemin)

    try:
        with open(chemin, 'r', encoding="utf-8") as f:
            content = f.read()
            if content:
                data = json.loads(content)
                print(f"✅ {file_name} chargé avec succès.")
                return data['corps_celestes']
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