import os
import datetime
import shutil

# 1. Utilisons os.path.join() pour construire tous les chemins (portabilité).
base_dir = 'mission_data'
archives_dir = os.path.join(base_dir, 'archives')
rapports_dir = os.path.join(base_dir, 'rapports')
journal_bord_path = os.path.join(base_dir, 'journal_bord.txt')
rapport_path = os.path.join(rapports_dir, 'rapport_systeme.txt')


# 2. Copions journal_bord.txt dans mission_data/archives/ en le renommant avec la date du jour : journal_bord_2026-02-18.txt (utilisez le module datetime).
os.system(f'move {journal_bord_path} {archives_dir}/journal_bord_{datetime.datetime.now().strftime("%Y-%m-%d")}.txt')


# 3. Créons un fichier mission_data/rapports/rapport_systeme.txt contenant :
with open(rapport_path, 'w', encoding='utf-8') as f:
    # Le résultat de os.getcwd()
    f.write(f"Repertoire courant : {os.getcwd()}\n\n")

    # La liste des variables d’environnement liées à Python (os.environ) — filtrez celles contenant "PYTHON" ou "PATH".
    f.write("Variables d'environnement liees a Python ou PATH :\n")
    for key, value in os.environ.items():
        if 'PYTHON' in key or 'PATH' in key:
            f.write(f"{key} = {value}\n")

    # L’espace disque si disponible (bonus avec shutil.disk_usage()).
    try:
        usage = shutil.disk_usage(os.getcwd())
        f.write("\nEspace disque :\n")
        f.write(f"Total : {usage.total // (1024*1024)} Mo\n")
        f.write(f"Utilisé : {usage.used // (1024*1024)} Mo\n")
        f.write(f"Libre : {usage.free // (1024*1024)} Mo\n")
    except Exception as e:
        f.write(f"\nImpossible d'obtenir l'espace disque : {e}\n")


# 4. Affichons un résumé des opérations effectuées.
print("Résumé des opérations effectuées:")
print(f"- Construction des chemins de fichiers avec 'os.path.join()' pour une meilleure portabilite.")
print(f"- Deplacement de 'journal_bord.txt' vers '{archives_dir}' avec un nom incluant la date actuelle.")
print(f"- Creation du rapport systeme dans '{rapport_path}' avec les informations sur le repertoire courant, les variables d'environnement et l'espace disque.")
    