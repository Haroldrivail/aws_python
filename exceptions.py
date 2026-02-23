# --- exceptions.py ---
"""Module pour la gestion des exceptions liées à la navigation et aux missions."""

import datetime

class NavigationError(Exception):
    """Classe de base pour les erreurs de navigation spatiale."""

class MissionDataError(NavigationError):
    """Données de mission invalides ou incomplètes."""

class TrajectoireError(NavigationError):
    """Paramètres de trajectoire invalides."""

class CarburantError(NavigationError):
    """Niveau de carburant critique ou invalide."""


# Ecrivez une fonction valider_mission(mission_dict) qui vérifie :
def valider_mission(mission_dict):
    """Valide les données d'une mission.

    Args:
        mission_dict (dict): Dictionnaire contenant les informations de la mission.

    Raises:
        MissionDataError: Si un champ obligatoire est manquant ou invalide.
        MissionDataError: Si la durée de la mission est négative ou nulle.
        MissionDataError: Si le budget de la mission est négatif ou nul.
        MissionDataError: Si la date de lancement est invalide.
        TrajectoireError: Si la durée de la mission n'est pas cohérente avec la distance.
    """
    # 1. Tous les champs obligatoires sont présents → sinon MissionDataError.
    champs_obligatoires = [
        "id",
        "nom",
        "destination",
        "date_lancement",
        "statut",
        "equipage",
        "duree_jours",
        "budget_millions_usd"
    ]
    for champ in champs_obligatoires:
        if champ not in mission_dict:
            raise MissionDataError(f"Le champ '{champ}' est manquant dans \
                les données de la mission.")
    # 2. La duree_jours est positive → sinon MissionDataError.
    if mission_dict['duree_jours'] <= 0:
        raise MissionDataError("La durée de la mission doit être un nombre positif de jours.")
    # 3. Le budget_millions_usd est positif → sinon MissionDataError.
    if mission_dict['budget_millions_usd'] <= 0:
        raise MissionDataError("Le budget de la mission doit être un nombre positif.")
    # 4. La date_lancement est au format valide → sinon MissionDataError.
    if not datetime.datetime.strptime(mission_dict['date_lancement'], '%Y-%m-%d'):
        raise MissionDataError("La date de lancement doit être au format 'YYYY-MM-DD'.")

    # 5. Si destination est un corps connu, vérifier que la durée
    # est cohérente avec la distance (marge ×10) → sinon TrajectoireError.
    destinations_connues = ["Mars", "Lune", "Europe(Jupiter)", "Titan(Saturne)"]
    for dest in destinations_connues:
        if dest in mission_dict['destination']:
            distance_km = {"Mars": 225000000, "Lune": 384400, "Europe(Jupiter)":\
                628300000, "Titan(Saturne)": 1275000000}
            duree_estimee_jours = distance_km[dest] / (30000 * 24)
            if mission_dict['duree_jours'] < duree_estimee_jours * 0.1 \
                or mission_dict['duree_jours'] > duree_estimee_jours * 10:
                raise TrajectoireError(f"La durée de la mission vers {dest} \
                    n'est pas cohérente avec la distance.")

# Écrivez aussi verifier_carburant(releve) qui : - Lève CarburantError
# si carburant_pct < 10. - Affiche un warning si carburant_pct < 30.
def verifier_carburant(releve):
    """Vérifie le niveau de carburant d'un relevé.

    Args:
        releve (dict): Dictionnaire contenant les informations du relevé.

    Raises:
        CarburantError: Si le niveau de carburant est critique (< 10%).
    """
    carburant_pct = releve['carburant_pct']
    if carburant_pct < 10:
        raise CarburantError("Niveau de carburant critique : moins de 10%.")
    elif carburant_pct < 30:
        print("Warning : Niveau de carburant inférieur à 30%.")
