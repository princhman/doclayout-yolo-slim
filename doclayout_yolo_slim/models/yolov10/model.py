from doclayout_yolo_slim.engine.model import Model
from doclayout_yolo_slim.nn.tasks import YOLOv10DetectionModel
from .predict import YOLOv10DetectionPredictor

class YOLOv10(Model):

    def __init__(self, model="yolov10n.pt", task=None, verbose=False):
        super().__init__(model=model, task=task, verbose=verbose)

    @property
    def task_map(self):
        """Map head to model, trainer, validator, and predictor classes."""
        return {
            "detect": {
                "model": YOLOv10DetectionModel,
                "predictor": YOLOv10DetectionPredictor,
            },
        }
