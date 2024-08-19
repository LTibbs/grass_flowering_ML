# Image classification in citizen science images
Made using yolov8 image classification task (see https://docs.ultralytics.com/tasks/classify/).

Objective: can a model based on all available iNaturalist images successfully classify images as flowering or not flowering in multiple grass species?

Input data: research-grade iNaturalist images taken by Dec 31, 2022, which were downloaded via GBIF and split 80/20/10 into training, testing, and validation sets. Images were manually scored as flowering or not based on the presence or absence of visible live anthers. Models were trained for each species individually as well as for all three species together, using [yolov8_ML.py](https://github.com/LTibbs/grass_flowering_ML/blob/main/image_classification/yolov8_ML.py).

## Details:
- Switchgrass
  - Input data: 6768 manually-scored images (495 flowering, 6273 not flowering).
  - Resulting model: [SwitchgrassML2_best.pt](https://github.com/LTibbs/grass_flowering_ML/blob/main/image_classification/SwitchgrassML2_best.pt)
  - Results on validation data: ![switchgrass_confusion_matrix_classification.png](https://github.com/LTibbs/grass_flowering_ML/blob/main/image_classification/switchgrass_confusion_matrix_classification.png)
