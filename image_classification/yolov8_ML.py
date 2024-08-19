# train and apply models for grass flowering image classification

# general training method
python
from ultralytics import YOLO
# Load a model to use for initial weights, based on https://docs.ultralytics.com/tasks/classify/
model = YOLO("yolov8n-cls.yaml")  # build a new model from YAML
model = YOLO("yolov8n-cls.pt")  # load a pretrained model (recommended for training)
model = YOLO("yolov8n-cls.yaml").load("yolov8n-cls.pt")  # build from YAML and transfer weights
results = model.train(data="ML/Switchgrass_ML2", epochs=100, imgsz=640, resume=True) # update directory as needed for each species/model

# validate model by running on test set, previously unseen by model
python
from ultralytics import YOLO
model=YOLO("/yolov8/runs/classify/train9/weights/best.pt") # here, provide path to desired model; update as needed for each species
metrics=model.val(imgsz=640, batch=1)
source = "ML/Switchgrass_ML2_test/flowering" # this directory contains the test images from Switchgrass_ML2; update as needed for each species/model
source = "ML/Switchgrass_ML2_test/not_flowering"  # this directory contains the test images from Switchgrass_ML2; update as needed for each species/model
# Run inference on the source
results = model(source, save_txt=True) 
                      
