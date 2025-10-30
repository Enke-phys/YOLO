#Training starten
yolo detect train \
  model=yolov8n.pt \
  data=/Users/enke/Projects/Hirnventile/YOLO/data/dataset.yaml \
  device=cpu \
  epochs=50 \
  imgsz=50 \
  batch=4 \
  workers=1

#Validierung starten
#yolo detect val \
#  data=/Users/enke/Projects/Hirnventile/YOLO/data/dataset.yaml \
#  model=runs/detect/train/weights/best.pt

#Inferenz starten
#yolo predict \
#  model=runs/detect/train/weights/best.pt \
#  source=/Pfad/zu/Testbildern