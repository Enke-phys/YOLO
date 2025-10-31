#Training starten
#yolo detect train \
#  model=yolov9e.pt \
#  data=/Users/enke/Projects/Hirnventile/YOLO/data/dataset.yaml \
#  device=0 \
#  epochs=50 \
#  imgsz=640 \
#  batch=16 \
#  workers=4 \
#  optimizer=AdamW \
#  lr0=0.001 \
#  weight_decay=0.0005 \

#Validierung starten
#yolo detect val \
#  data=/Users/enke/Projects/Hirnventile/YOLO/data/dataset.yaml \
#  model=runs/detect/train3/weights/best.pt \
#  device=cpu

#Inferenz starten
yolo predict \
  model=/Users/enke/Projects/Hirnventile/YOLO/runs/detect/bestv2.pt \
  source=/Users/enke/Projects/Hirnventile/YOLO/VP_Shunts_Externe_Validierung \
  max_det=1 \
  iou=0.45