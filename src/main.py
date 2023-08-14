"""
@software{yolov8_ultralytics,
  author       = {Glenn Jocher and Ayush Chaurasia and Jing Qiu},
  title        = {YOLO by Ultralytics},
  version      = {8.0.0},
  year         = {2023},
  url          = {https://github.com/ultralytics/ultralytics},
  orcid        = {0000-0001-5950-6979, 0000-0002-7603-6750, 0000-0003-3783-7069},
  license      = {AGPL-3.0}
}
"""
import wandb
from wandb.yolov8 import add_wandb_callback
from ultralytics import YOLO

if __name__ == '__main__':

    # Load a model
    model = YOLO('yolov8m-seg.pt')  # load a pretrained model (recommended for training)
    # Add W&B callback for Ultralytics
    add_wandb_callback(model, enable_model_checkpointing=True)

    # Train the model
    results = model.train(project="book-yolo8m-seg", data="../datasets/dataset.yaml", epochs=20, imgsz=640, batch=4, device="cpu")
    model.val()
    
    # Export the model
    model.export(format="torchscript")

    # Finish the W&B run
    wandb.finish()