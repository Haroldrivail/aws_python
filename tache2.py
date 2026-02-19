import os

# 1. Vérifions que le dossier mission_data/ existe. Si non, affichons une erreur.
if not os.path.exists('mission_data'):
    print("Le repertoire 'mission_data' n'existe pas.")


# 2. Listons tous les fichiers du dossier avec leur taille en Ko.
print("📁 mission_data/")
for item in os.listdir('mission_data'):
    if os.path.isdir(os.path.join('mission_data', item)):
        print(f"  📁 {item}/ ({os.path.getsize(os.path.join('mission_data', item)) // 1024} Ko)")
    else:
        print(f"  📄 {item} ({os.path.getsize(os.path.join('mission_data', item)) // 1024} Ko)")


# 3. Créons un sous-dossier mission_data/rapports/ s’il n’existe pas déjà.
if not os.path.exists('mission_data/rapports'):
    os.makedirs("mission_data/rapports") # Create a new directory for reports


# 4. Créons un sous-dossier mission_data/archives/ s’il n’existe pas déjà.
if not os.path.exists('mission_data/archives'):
    os.makedirs("mission_data/archives") # Create a new directory for archives

# # 5. Affichons l’arborescence résultante.
print("📁 mission_data/")
for item in os.listdir('mission_data'):
    if os.path.isdir(os.path.join('mission_data', item)):
        print(f"  📁 {item}/ [cree]")
    else:
        print(f"  📄 {item} ({os.path.getsize(os.path.join('mission_data', item)) // 1024} Ko)")

