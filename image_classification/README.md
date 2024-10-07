# Image classification in citizen science images
Made using yolov8 image classification task (see https://docs.ultralytics.com/tasks/classify/).

Objective: can a model based on all available iNaturalist images successfully classify images as flowering or not flowering in multiple grass species?

Input data: research-grade iNaturalist images taken by Dec 31, 2022, which were downloaded via GBIF and split 80/20/10 into training, testing, and validation sets. Images were manually scored as flowering or not based on the presence or absence of visible live anthers. Models were trained for each species individually as well as for all three species together, using [yolov8_ML.py](https://github.com/LTibbs/grass_flowering_ML/blob/main/image_classification/yolov8_ML.py).

## Details:
- Switchgrass - main species of interest
  - Input data: 6768 manually-scored images (495 flowering, 6273 not flowering).
  - Resulting model: [SwitchgrassML2_best.pt](https://github.com/LTibbs/grass_flowering_ML/blob/main/image_classification/SwitchgrassML2_best.pt)
  - Results on test data: ![switchgrass_confusion_matrix_classification.png](https://github.com/LTibbs/grass_flowering_ML/blob/main/image_classification/switchgrass_confusion_matrix_classification.png)
  - General conclusion: of switchgrass images predicted as flowering, 96% were actually flowering. This was enough to recover the expected trend of flowering time by latitude, and therefore sufficient for our goals.
 
- Big Bluestem -
  - Input data: 8005 manually-scored images (489 flowering, 7516 not flowering).
  - Resulting model: [BigBluestemML_best.pt](https://github.com/LTibbs/grass_flowering_ML/blob/main/image_classification/BigBluestemML_best.pt)
  - Results on test data: ![BigBluestem_confusion_matrix_classification.png](https://github.com/LTibbs/grass_flowering_ML/blob/main/image_classification/bigbluestem_confusion_matrix_classification.png)
  - Of big bluestem images predicted as flowering, 92% were actually flowering.
 
- Indiangrass -
  - Input data: 10127 manually-scored images (175 flowering, 9952 not flowering)
  - Resulting model: [IndiangrassML_best.pt](https://github.com/LTibbs/grass_flowering_ML/blob/main/image_classification/IndiangrassML_best.pt)
  - Results on test data: ![Indiangrass_confusion_matrix_classification.png](https://github.com/LTibbs/grass_flowering_ML/blob/main/image_classification/Indiangrass_confusion_matrix_classification.png)
  - Poor results (only 3% of predicted flowering images were actually flowering), potentially due to relative lack of flowering input images available to train in this species.

- Three species -
  - Input data: 24167 manually-scored images (758 flowering, 23409 not flowering)
  - Resulting model: [three_species_ML_best.pt](https://github.com/LTibbs/grass_flowering_ML/blob/main/image_classification/three_species_ML_best.pt)
  - Results on test data: ![three_species_confusion_matrix_classification.png](https://github.com/LTibbs/grass_flowering_ML/blob/main/image_classification/three_species_confusion_matrix_classification.png)
  - Of images predicted as flowering, 77% were actually flowering
