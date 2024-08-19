# Image classification in citizen science images
Made using yolov8 image classification task (see https://docs.ultralytics.com/tasks/classify/).

Input data: research-grade iNaturalist images taken by Dec 31, 2022, which were downloaded via GBIF and split 80/20/10 into training, testing, and validation sets. Images were manually scored as flowering or not based on the presence or absence of visible live anthers.

## Details:
- Switchgrass
  - Input data: 6768 manually-scored images (495 flowering, 6273 not flowering).
  - Results on validation data: 
