# Anther detection in citizen science images

Made using Roboflow to label and augment images as well as to train a model. Model at: https://app.roboflow.com/grass-flowering/big-bluestem-anthers/visualize/1. Chose to focus on big bluestem because its anthers remain on the plant longer after flowering and show clearer distinctions between fresh and old/dead anthers.

Goal: can a fast, easy model trained on relatively few images successfully identify live anthers in multiple grass species?

- Input data: 24 research grade images of big bluestem obtained from iNaturalist: 16 with live anthers labelled, 8 null (no live anthers visible)
- Augmentation: rotation, shear, brightness, exposure, and blur to account for inconsistencies in citizen science images
- --> 211 total images for model after augmentation

## Results:
Applied model to big bluestem but also Indiangrass and switchgrass because of similarities in anthers. Generally, poor results, but Indiangrass anther detection actually performed better than image classification in that species.
- Big bluestem:
  - 
