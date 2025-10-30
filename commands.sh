#Training starten
yolo detect train \
  model=yolov9e.pt \
  data=/Users/enke/Projects/Hirnventile/YOLO/data/dataset.yaml \
  device=0 \
  epochs=50 \
  imgsz=640 \
  batch=16 \
  workers=4 \
  optimizer=AdamW \
  lr0=0.001 \
  weight_decay=0.0005 \

#Validierung starten
#yolo detect val \
#  data=/Users/enke/Projects/Hirnventile/YOLO/data/dataset.yaml \
#  model=runs/detect/train/weights/best.pt

#Inferenz starten
#yolo predict \
#  model=runs/detect/train/weights/best.pt \
#  source=/Pfad/zu/Testbildern