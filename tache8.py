"""Module pour la gestion des tâches liées à la navigation spatiale."""

import navigation

if __name__ == "__main__":
    corps = navigation.charger_corps_celestes()
    d = navigation.distance_interplanetaire("Terre", "Mars", corps)
    print(f"Distance Terre-Mars : {d:.2f} millions km")
    t = navigation.temps_trajet(d, 11.0)
    print(f"Temps de trajet à 11 km/s : {t:.0f} jours")
    print(f"Poids d'un astronaute (80 kg) sur Mars : {navigation.poids_sur_corps(80, 3.72):.1f} N")
