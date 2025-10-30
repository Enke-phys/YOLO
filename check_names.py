from pathlib import Path

txt_dir = Path("/Users/enke/Projects/Hirnventile/YOLO/txt_Dateien")
img_dir = Path("/Users/enke/Projects/Hirnventile/YOLO/jpg+label")

txt_basenames = {path.stem for path in txt_dir.glob("*.txt")}
img_basenames = {path.stem for path in img_dir.glob("*.jpg")}

missing_txt = img_basenames - txt_basenames      # Bilder ohne passende TXT
missing_img = txt_basenames - img_basenames      # TXT ohne passendes Bild

print(f"{len(img_basenames)} JPG-Dateien gefunden.")
print(f"{len(txt_basenames)} TXT-Dateien gefunden.\n")

if missing_txt:
    print("Fehlende TXT-Dateien für:")
    for name in sorted(missing_txt):
        print(f"  {name}.jpg")
else:
    print("Alle JPG-Dateien haben eine passende TXT-Datei.")

print()

if missing_img:
    print("Fehlende JPG-Dateien für:")
    for name in sorted(missing_img):
        print(f"  {name}.txt")
else:
    print("Alle TXT-Dateien haben eine passende JPG-Datei.")
    