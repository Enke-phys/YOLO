import os
import glob
import json
import shutil

# Pfad zu den Vorhersagen
predictions_dir = "runs/detect/predict"
labels_dir = os.path.join(predictions_dir, "labels")

# Erstelle einen neuen Ordner für die gefilterten Ergebnisse
output_dir = os.path.join(predictions_dir, "best_predictions")
os.makedirs(output_dir, exist_ok=True)

# Gehe durch alle Label-Dateien
for label_file in glob.glob(os.path.join(labels_dir, "*.txt")):
    best_confidence = -1
    best_line = None
    
    # Lese die Label-Datei
    with open(label_file, 'r') as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) >= 6:  # Format: class x_center y_center width height confidence
                confidence = float(parts[5])
                if confidence > best_confidence:
                    best_confidence = confidence
                    best_line = line
    
    # Speichere nur die beste Vorhersage
    if best_line:
        output_file = os.path.join(output_dir, os.path.basename(label_file))
        with open(output_file, 'w') as f:
            f.write(best_line)

print(f"Die besten Vorhersagen wurden in {output_dir} gespeichert.")