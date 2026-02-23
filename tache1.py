"""Module pour la gestion des tâches liées au journal de bord et aux alertes."""

# 1. Ouvrons le fichier mission_data/journal_bord.txt en lecture.
f = open('mission_data/journal_bord.txt', 'r', encoding='utf-8')


# 2. Affichons le nombre total de lignes (entrées du journal).
lines = f.readlines()
print(f"Journal de bord: {len(lines)} entrees")


# 3. Affichons uniquement les lignes contenant le mot "Alerte" ou "alerte" (insensible à la casse).
lines_with_alerts = [line for line in lines if 'alerte' in line.lower()]

print(f"--- Alertes detectees ({len(lines_with_alerts)}) ---")

for line in lines_with_alerts:
    print(line.strip())

print("✅ Fichier 'alertes.txt' cree.")
f.close()


# 4. Écrivons ces lignes d’alerte dans un nouveau fichier mission_data/alertes.txt.
f = open('mission_data/alertes.txt', 'w', encoding='utf-8')
f.writelines(lines_with_alerts)
f.close()