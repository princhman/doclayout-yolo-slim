from doclayout_yolo_slim.models import YOLOv10
import sys
import doclayout_yolo_slim

sys.modules['doclayout_yolo'] = doclayout_yolo_slim
model = YOLOv10(model="doclayout_yolo_docsynth300k_imgsz1600.pt")

results = model.predict("image.png")
print(results)
