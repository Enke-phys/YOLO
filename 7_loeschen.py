import os

# Pfade zu den Ordnern mit den Label-Dateien
label_folders = [
    "/Users/enke/Projects/Hirnventile/YOLO/data/labels/train",
    "/Users/enke/Projects/Hirnventile/YOLO/data/labels/val"
]

# Debug-Ausgabe
print("Starte die Bereinigung...")
print(f"Aktuelles Arbeitsverzeichnis: {os.getcwd()}")

# Durchsuche jeden Ordner
for folder in label_folders:
    print(f"\nVerarbeite Ordner: {folder}")
    
    # Überprüfe ob der Ordner existiert
    if not os.path.exists(folder):
        print(f"  FEHLER: Ordner existiert nicht: {folder}")
        continue
        
    # Zähler für Dateien
    total_files = 0
    processed_files = 0
    
    # Gehe durch alle .txt-Dateien im Ordner
    for filename in os.listdir(folder):
        if not filename.endswith('.txt'):
            continue
            
        total_files += 1
        filepath = os.path.join(folder, filename)
        
        try:
            # Lese die Datei ein
            with open(filepath, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            # Behalte nur die Zeilen, die nicht mit "7 " beginnen
            original_count = len(lines)
            filtered_lines = [line for line in lines if not line.strip().startswith('7 ')]
            new_count = len(filtered_lines)
            
            # Wenn sich die Anzahl der Zeilen geändert hat, schreibe die Datei neu
            if new_count != original_count:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.writelines(filtered_lines)
                print(f"  Bereinigt: {filename} - {original_count - new_count} Einträge entfernt")
                processed_files += 1
                
        except Exception as e:
            print(f"  FEHLER bei {filename}: {str(e)}")
    
    print(f"Fertig mit {folder}")
    print(f"  Verarbeitete Dateien: {processed_files} von {total_files}")

print("\nBereinigung abgeschlossen.")