# Faster-R-CNN
This repository is created for an NUS-DSA5204 project report to study object detection model performance for video dataset.

## Faster R-CNN Model
Faster R-CNN is a two-stage detection framework (with object proposals). The model first feeds its input to a CNN (Resnet50) to generate feature maps. Then, Region proposal network is applied to these feature maps. This returns the object proposals along with their labels. In the next step, a Region of Interest (RoI) pooling layer is applied on these proposals to bring down all the proposals to the same size. Finally, the proposals are passed to a fully connected layer which has a SoftMax layer and a linear regression layer at its top, to classify and output the bounding boxes for objects. Faster R-CNN uses RPN (region proposal network) to generate effective and efficient region proposals. Also, its accuracy is higher than R-CNN and Fast R-CNN. However, Training Faster R-CNN is complicated, not efficient for real time applications
## Model Algorithm:
Feed the input image to the CNN to generate a convolutional feature map.<br />
Region proposal network is applied on these feature maps. This returns the object proposals along with their objectness score.<br />
A Region of Interest (RoI) pooling layer is applied on these proposals to bring down all the proposals to the same size.<br />
Finally, the proposals are passed to a fully connected layer which has a SoftMax layer and a linear regression layer at its top, to classify and output the bounding boxes for objects.<br />
## Advantages
Propose RPN for generating effective & efficient REGION PROPOSALs, replacement of selective search. <br />
Improved accuracy as compared to R-CNN and Fast R-CNN. <br />
## Disadvantage
Training is complicated, not efficient for real time applications.

## Source Code Structure:
### keras_frcnn
Maintains core network layer for the Faster-R-CNN. References: https://github.com/kbardool/keras-frcnn
### model_evaluation_results
This folder stores evaluation results of Faster R-CNN for Train and AirPlane class for IoU = 50% and IoU = 75%. This includes a csv file and Precision-Recall plot.
### model_config_pickle
This folder stores the config pickle file for Train and AirPlane class.
### model_weights
This folder stores the checkpoints of Train and AirPlane class for same domain (COCO-COCO, YTBB-YTBB) and transfer domain cases (COCO-YTBB, YTBB-COCO) for IoU=50% and 75%.
### annotation files
Set of files, which has COCO/YTBB dataset images with bounding box details
### training, testing (bounding box) and evaluation (metrics) Jupyter Notebooks
Set of jupyter notebooks created for same domain (COCO-COCO, YTBB-YTBB) and transfer domain (COCO-YTBB, YTBB-COCO) for: </br>
Training the models </br>
Creating bounding boxes  </br>
Finding accuracy over IoU = 0.5 and 0.75  </br>
