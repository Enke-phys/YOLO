import os

# Pfade zu den Ordnern
folders = [
    "/Users/enke/Projects/Hirnventile/YOLO/data/labels/train",
    "/Users/enke/Projects/Hirnventile/YOLO/data/labels/val"
]

# Zähler für die Gesamtanzahl der gefundenen Dateien
total_files_with_mblue = 0

print("Suche nach Dateien mit 'm.blue' (Label 9)...\n")

for folder in folders:
    print(f"Prüfe Ordner: {folder}")
    count = 0
    
    # Durchsuche alle .txt-Dateien im Ordner
    for filename in os.listdir(folder):
        if not filename.endswith('.txt'):
            continue
            
        filepath = os.path.join(folder, filename)
        
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                for line in f:
                    # Überprüfe, ob die Zeile mit '9 ' beginnt
                    if line.strip().startswith('9 '):
                        print(f"  Gefunden in: {filename}")
                        count += 1
                        break  # Keine Notwendigkeit, weiter in der Datei zu suchen
                        
        except Exception as e:
            print(f"  Fehler beim Lesen von {filename}: {e}")
    
    print(f"  Gefundene Dateien in diesem Ordner: {count}\n")
    total_files_with_mblue += count

print(f"Gesamtanzahl der Dateien mit 'm.blue' (Label 9): {total_files_with_mblue}")