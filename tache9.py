"""Module pour la validation des missions et la vérification du carburant."""

from exceptions import valider_mission, NavigationError, CarburantError, verifier_carburant

if __name__ == "__main__":
    # Cas valide
    try:
        valider_mission({"id": "MSN-001", "nom": "Test", "destination": "Mars",
                        "date_lancement": "2028-01-01", "statut": "planifiée",
                        "equipage": [], "duree_jours": 680, "budget_millions_usd": 5000})
        print("✅ Mission valide")
    except NavigationError as e:
        print(f"❌ {type(e).__name__}: {e}")

    # Cas invalide : durée négative
    try:
        valider_mission({"id": "MSN-999", "nom": "Bad", "destination": "Lune",
                        "date_lancement": "2028-01-01", "statut": "test",
                        "equipage": [], "duree_jours": -5, "budget_millions_usd": 100})
    except NavigationError as e:
        print(f"❌ {type(e).__name__}: {e}")

    # Cas carburant critique
    try:
        verifier_carburant({"carburant_pct": 7.5, "phase": "approche_mars"})
    except CarburantError as e:
        print(f"🔴 {e}")
