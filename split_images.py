import random
import shutil
from pathlib import Path

SOURCE_IMAGE_DIR = Path("/Users/enke/Projects/Hirnventile/YOLO/jpg+label")
SOURCE_LABEL_DIR = Path("/Users/enke/Projects/Hirnventile/YOLO/txt_Dateien")
TRAIN_IMAGE_DIR = Path("/Users/enke/Projects/Hirnventile/YOLO/data/images/train")
VAL_IMAGE_DIR = Path("/Users/enke/Projects/Hirnventile/YOLO/data/images/val")
TRAIN_LABEL_DIR = Path("/Users/enke/Projects/Hirnventile/YOLO/data/labels/train")
VAL_LABEL_DIR = Path("/Users/enke/Projects/Hirnventile/YOLO/data/labels/val")
TRAIN_RATIO = 0.8
RANDOM_SEED = 42  # anpassen oder entfernen

def clear_directory(directory: Path):
    for entry in directory.iterdir():
        if entry.is_file():
            entry.unlink()


def main():
    TRAIN_IMAGE_DIR.mkdir(parents=True, exist_ok=True)
    VAL_IMAGE_DIR.mkdir(parents=True, exist_ok=True)
    TRAIN_LABEL_DIR.mkdir(parents=True, exist_ok=True)
    VAL_LABEL_DIR.mkdir(parents=True, exist_ok=True)

    clear_directory(TRAIN_IMAGE_DIR)
    clear_directory(VAL_IMAGE_DIR)
    clear_directory(TRAIN_LABEL_DIR)
    clear_directory(VAL_LABEL_DIR)

    images = sorted(SOURCE_IMAGE_DIR.glob("*.jpg"))
    if not images:
        print(f"Keine JPG-Dateien in {SOURCE_IMAGE_DIR}")
        return

    random.Random(RANDOM_SEED).shuffle(images)
    split_idx = int(len(images) * TRAIN_RATIO)
    train_images = sorted(images[:split_idx], key=lambda p: p.name)
    val_images = sorted(images[split_idx:], key=lambda p: p.name)

    for img_path in train_images:
        shutil.copy2(img_path, TRAIN_IMAGE_DIR / img_path.name)
        label_src = SOURCE_LABEL_DIR / (img_path.stem + ".txt")
        if label_src.exists():
            shutil.copy2(label_src, TRAIN_LABEL_DIR / label_src.name)
        else:
            print(f"Warnung: Keine Label-Datei für {img_path.name}")

    for img_path in val_images:
        shutil.copy2(img_path, VAL_IMAGE_DIR / img_path.name)
        label_src = SOURCE_LABEL_DIR / (img_path.stem + ".txt")
        if label_src.exists():
            shutil.copy2(label_src, VAL_LABEL_DIR / label_src.name)
        else:
            print(f"Warnung: Keine Label-Datei für {img_path.name}")

    print(f"{len(train_images)} Bilder nach {TRAIN_IMAGE_DIR} kopiert.")
    print(f"{len(val_images)} Bilder nach {VAL_IMAGE_DIR} kopiert.")

if __name__ == "__main__":
    main()