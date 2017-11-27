# Problem Statement - Samsung's Hand Gesture Recognition

The zip file contains three files
1. hand_gesture_vgg16_final.ipynb - This is the main file. Documented everything there.
2. under_sample_Point.py   -   This file is used to under sample few classes and upsample other classes
3. Test_Predictions.ipynb  -  This is used to load trained models and make predictions for test dataset
4. mlp_model_6_73.h5   -   The weights file used to load a trained model for classification
5. keepcalm_test_predictions.csv - Final test submission file. 

High level Approach 
1. Up sampling class 'A' and under sampling class 'Five' and 'Point' has reduced misclassifications. Hence the move.
2. Used VGG16 net to get it's 1st fully connected layer's output as feature representations for images.
3. Used these representations to classify gestures with an MLP. (2 hidden layers, used dropout, Cross-Entropy Loss)
4. Used Data Augmentation. Helped in increasing accuracy.
5. Center cropped all images. Most of the images were located at the center of the image.
   (Cropping proved to increase accuracy big time. Boosted the accuracy by 10%.)
6. Plotting Epochs Vs Accuracy to identify threshold for over-fitting.
7. Plotting Test images and its predicted labels for visual analysis. Helps know where the network is getting confused.
8. Analysing Validation data's confusion matrix also helped in identifying where the misclassifications were happening.

Results:
Test results are state of the art (as of this time). ~ 75% accuracy

Hardware Configuration:
Processor: Intel Xeon
RAM : 256 GB
Graphics Card: GTX 1080Ti (11 GB Memory)

Software Configuraion:
Python - 2.7
Keras - 2.0.8  (Tensorflow Backend, 1.4.0)
Jupyter Notebook - 1.0.0 

Contributors: Jayanth Rasamsetti and Vivek Bakaraju
Date: November, 2017
