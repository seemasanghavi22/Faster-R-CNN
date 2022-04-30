# Faster-R-CNN
This repository is created to study Faster R-CNN object detection model performance for video dataset. It stores all the code and outcome required for Paper Reproduction for the below references: </br>
[1] Esteban Real, Jonathon Shlens, Stefano Mazzocchi, Xin Pan, Vincent
Vanhoucke. YouTube-BoundingBoxes: A Large High-Precision HumanAnnotated Data Set for Object Detection in Video, IEEE, 2017. </br>
[2] Enoch Arulprakash, Martin Aruldoss. A study on generic object detection with emphasis on future research directions. Journal of King Saud
University - Computer and Information Sciences. 2021 </br>

## Faster R-CNN Model
Faster R-CNN is a two-stage detection framework (with object proposals). </br>
The model first feeds its input to a CNN (Resnet50) to generate feature maps. </br>
Then, Region proposal network is applied to these feature maps. </br>
This returns the object proposals along with their labels. </br>
In the next step, a Region of Interest (RoI) pooling layer is applied on these proposals to bring down all the proposals to the same size. </br>
Finally, the proposals are passed to a fully connected layer which has a SoftMax layer and a linear regression layer at its top, to classify and output the bounding boxes for objects. </br>
Faster R-CNN uses RPN (region proposal network) to generate effective and efficient region proposals. </br>
Also, its accuracy is higher than R-CNN and Fast R-CNN. However, Training Faster R-CNN is complicated, not efficient for real time applications. </br>
### Model Algorithm:
Feed the input image to the CNN to generate a convolutional feature map.<br />
Region proposal network is applied on these feature maps. This returns the object proposals along with their objectness score.<br />
A Region of Interest (RoI) pooling layer is applied on these proposals to bring down all the proposals to the same size.<br />
Finally, the proposals are passed to a fully connected layer which has a SoftMax layer and a linear regression layer at its top, to classify and output the bounding boxes for objects.<br />
### Advantages
Propose RPN for generating effective & efficient REGION PROPOSALs, replacement of selective search. <br />
Improved accuracy as compared to R-CNN and Fast R-CNN. <br />
### Disadvantage
Training is complicated, not efficient for real time applications. </br>
## Model Training Methodology
Faster R-CNN is trained on a pre-trained ResNet50 to get the advantage of Transfer Learning. </br>
Training was done on COCO and YTBB Datasets of 1000 images each with 5 Epoch and 10 Epoch. </br>
New weights were generated for testing purpose - Checkpoints for 5 Epoch and 10 Epochs </br>
## Model Evaluation Methodology
Faster R-CNN is evaluated on COCO/YTBB models - to check AP accuracy and Bounding Box accuracy. </br>
Evaluation was done on COCO and YTBB Test Datasets of 300 images each - using 5 epoch and 10 epoch checkpoints. </br>
Test results was saved. </br>
Test Results: RecallPrecision Plot, AP values at IoU 50% and IoU 75% </br>
There were 32 cases evaluated accross Same Domain and Transfer Domain cases to calculate:</br>
AP@50% IoU </br>
AP@75% IoU </br>
AP small @50% IoU </br>
AP small @75% IoU </br>
AP medium @50% IoU </br>
AP medium @75% IoU </br>
AP large @50% IoU </br>
AP large @75% IoU </br>

## Source Code Folder Structure:
### Folder keras_frcnn 
Maintains core network layer for the Faster-R-CNN. References: https://github.com/kbardool/keras-frcnn
### Folder model_evaluation_results
This folder stores evaluation results of Faster R-CNN for Train and AirPlane class for IoU = 50% and IoU = 75%. This includes a csv file and Precision-Recall plot.
### Folder model_config_pickle
This folder stores the config pickle file for Train and AirPlane class.
### Folder model_weights
This folder stores the checkpoints of Train and AirPlane class for same domain (COCO-COCO, YTBB-YTBB) and transfer domain cases (COCO-YTBB, YTBB-COCO) for IoU=50% and 75%.
### Folder annotation files
Set of files, which has COCO/YTBB dataset images with bounding box details, a pre-requisite for Faster R-CNN model code.
### faster_rcnn_data_preprocessing.jpynb
This was used to do data pre-processing for COCO and YTBB boundinng boxes csv files to create annotation files required for Faster R-CNN.
### training, testing (bounding box) and evaluation (metrics) Jupyter Notebooks
Set of jupyter notebooks created for same domain (COCO-COCO, YTBB-YTBB) and transfer domain (COCO-YTBB, YTBB-COCO) for: </br>
#### Training the models - 8 Files </br>
Faster-RCNN-YTBB-TrainClass-Training-10Epoch.jpynb </br>
Faster-RCNN-YTBB-AirplaneClass-Training-10Epoch.jpynb </br>
Faster-RCNN-COCO-TrainClass-Training-10Epoch.jpynb </br>
Faster-RCNN-COCO-AirPlaneClass-Training-10Epoch.jpynb </br>
train_faster_rcnn-COCO-AIRPLANE-VEHICLE.jpynb </br>
train_faster_rcnn-COCO-TRAIN-VEHICLE.jpynb </br>
train_faster_rcnn-Y2BB-AIRPLANE-VEHICLE.jpynb </br>
train_faster_rcnn-Y2BB-TRAIN-VEHICLE.jpynb </br>
#### Testing the model for bounding boxes - 4 Files </br>
test_faster_rcnn-Y2BB-TRAIN-VEHICLE.jpynb </br>
test_faster_rcnn-Y2BB-AIRPLANE-VEHICLE.jpynb </br>
test_faster_rcnn-COCO-TRAIN-VEHICLE.jpynb </br>
test_faster_rcnn-COCO-AIRPLANE-VEHICLE.jpynb </br>
#### Testing the model for finding accuracy over IoU = 0.5 and 0.75 - 32 Files </br>
evaluate_faster_rcnn-YTBBModel-YTBBImages-TRAIN-VEHICLE.jpynb  </br>
evaluate_faster_rcnn-YTBBModel-YTBBImages-TRAIN-VEHICLE-Small_Images.jpynb  </br>
evaluate_faster_rcnn-YTBBModel-YTBBImages-TRAIN-VEHICLE-Medium_Images.jpynb  </br>
evaluate_faster_rcnn-YTBBModel-YTBBImages-TRAIN-VEHICLE-Large_Images.jpynb  </br>
evaluate_faster_rcnn-YTBBModel-YTBBImages-AIRPLANE-VEHICLE.jpynb  </br>
evaluate_faster_rcnn-YTBBModel-YTBBImages-AIRPLANE-VEHICLE-Small_Images.jpynb  </br>
evaluate_faster_rcnn-YTBBModel-YTBBImages-AIRPLANE-VEHICLE-Medium_Images.jpynb  </br>
evaluate_faster_rcnn-YTBBModel-YTBBImages-AIRPLANE-VEHICLE-Large_Images.jpynb  </br>
evaluate_faster_rcnn-COCOModel-COCOImages-AIRPLANE-VEHICLE.jpynb  </br>
evaluate_faster_rcnn-COCOModel-COCOImages-AIRPLANE-VEHICLE-Small_Images.jpynb  </br>
evaluate_faster_rcnn-COCOModel-COCOImages-AIRPLANE-VEHICLE-Medium_Images.jpynb  </br>
evaluate_faster_rcnn-COCOModel-COCOImages-AIRPLANE-VEHICLE-Large_Images.jpynb  </br>
evaluate_faster_rcnn-COCOModel-COCOImages-TRAIN-VEHICLE.jpynb  </br>
evaluate_faster_rcnn-COCOModel-COCOImages-TRAIN-VEHICLE-Small_Images.jpynb  </br>
evaluate_faster_rcnn-COCOModel-COCOImages-TRAIN-VEHICLE-Medium_Images.jpynb  </br>
evaluate_faster_rcnn-COCOModel-COCOImages-TRAIN-VEHICLE-Large_Images.jpynb  </br>
evaluate_faster_rcnn-COCOModel-YTBBImages-TRAIN-VEHICLE.jpynb  </br>
evaluate_faster_rcnn-COCOModel-YTBBImages-TRAIN-VEHICLE-Small_Images.jpynb  </br>
evaluate_faster_rcnn-COCOModel-YTBBImages-TRAIN-VEHICLE-Medium_Images.jpynb  </br>
evaluate_faster_rcnn-COCOModel-YTBBImages-TRAIN-VEHICLE-Large_Images.jpynb  </br>
evaluate_faster_rcnn-COCOModel-YTBBImages-AIRPLANE-VEHICLE.jpynb  </br>
evaluate_faster_rcnn-COCOModel-YTBBImages-AIRPLANE-VEHICLE-Small_Images.jpynb  </br>
evaluate_faster_rcnn-COCOModel-YTBBImages-AIRPLANE-VEHICLE-Medium_Images.jpynb  </br>
evaluate_faster_rcnn-COCOModel-YTBBImages-AIRPLANE-VEHICLE-Large_Images.jpynb  </br>
evaluate_faster_rcnn-YTBBModel-COCOImages-TRAIN-VEHICLE.jpynb  </br>
evaluate_faster_rcnn-YTBBModel-COCOImages-TRAIN-VEHICLE-Small_Images.jpynb  </br>
evaluate_faster_rcnn-YTBBModel-COCOImages-TRAIN-VEHICLE-Medium_Images.jpynb  </br>
evaluate_faster_rcnn-YTBBModel-COCOImages-TRAIN-VEHICLE-Large_Images.jpynb  </br>
evaluate_faster_rcnn-YTBBModel-COCOImages-AIRPLANE-VEHICLE.jpynb  </br>
evaluate_faster_rcnn-YTBBModel-COCOImages-AIRPLANE-VEHICLE-Small_Images.jpynb  </br>
evaluate_faster_rcnn-YTBBModel-COCOImages-AIRPLANE-VEHICLE-Medium_Images.jpynb  </br>
evaluate_faster_rcnn-YTBBModel-COCOImages-AIRPLANE-VEHICLE-Large_Images.jpynb  </br>

###### NOTE: These Jupyter Notebooks can be run, provided folder structure is maintained.
It also needs YTBB and COCO Datasets, which are not uploaded in this github repository due to space constraint. </br>
But results are saved in the notebook. </br>
