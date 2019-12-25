# Action Recognition on Realtime Application

This project is RGB base action recognition system that focus on real time application. We use KARD dataset to train this model. You can see more detail about dataset in [here](https://data.mendeley.com/datasets/k28dtm7tr6/1)

# Overview

* [Requirement](#requirement)
* [Dataset](#dataset)
* [Demo](#demo)
* [Evaluation](#evaluation)
* [Training](#training)
* [Performance](#performance)
* [Method](#method)
* [Note](#note)
* [Reference](#reference)

## Requirement

- keras

- tensorflow 1.14 (for using CuDNNLSTM)

- CUDA 10.0 

## Dataset
You can download dataset from [here](https://data.mendeley.com/datasets/k28dtm7tr6/1). Only RGB part is needed. Skeleton Joints and Depth data is not used. The structure of folder should be in this form
```
KARD-split
├── a01                   
│   ├── a01_s01_e01.mp4             
│   ├── a01_s01_e02.mp4            
│   ├── ...           
│   ├── a01_s10_e03     
├── a02                   
│   ├── a02_s01_e01.mp4             
│   ├── a02_s01_e02.mp4            
│   ├── ...           
│   ├── a02_s10_e03      
├── ....
├── ....
├── a18                   
│   ├── a18_s01_e01.mp4             
│   ├── a18_s01_e02.mp4            
│   ├── ...           
│   ├── a18_s10_e03   
└── ...
```
You can see more detail in dataset_list/trainlist.txt and dataset_list/testlist.txt

## Demo

Webcam or any camera is required for using demo. You can run demo by using the following command
```
python webcam.py
```
## Evaluation

You can use see the accuracy and confusion matrix of pretrain model by using below command.
```
python evaluate_model.py
```
## Training

You can try to train model and can change hyperparameters in the train.py file

```
python train.py
```


## Performance

Accuracy: around 87-89% (depend on which part of test set that is random)
Confusion Matrix: 
![alt text](https://github.com/peachman05/action-recognition-tutorial/blob/master/media/confusion_matrix.png "Confusion Matrix")

## Method

Input: 8 RGB frames

Output: 18 action classes

This project use RGB Difference as input. The idea is from this paper and this project. I use just only LSTM as core of model. You can see the detail of architecture in model_ML.py

## Note
If you want to change any parameter of train.py, evaluate_model.py and webcam.py, you can change it in the header of these files.


## Reference

### Example code

[https://stanford.edu/~shervine/blog/keras-how-to-generate-data-on-the-fly](https://stanford.edu/~shervine/blog/keras-how-to-generate-data-on-the-fly) Data generator on keras
[https://github.com/eriklindernoren/Action-Recognition](https://github.com/eriklindernoren/Action-Recognition) Sampling Idea

[https://github.com/AhmedGamal1496/online-action-recognition#Introduction](https://github.com/AhmedGamal1496/online-action-recognition#Introduction) RGB Difference Example

### Paper

Temporal Segment Networks for Action Recognition in Videos, Limin Wang, Yuanjun Xiong, Zhe Wang, Yu Qiao, Dahua Lin, Xiaoou Tang, and Luc Van Gool, TPAMI, 2018. [Arxiv Preprint](https://arxiv.org/abs/1705.02953)

### Dataset
[https://data.mendeley.com/datasets/k28dtm7tr6/1](https://data.mendeley.com/datasets/k28dtm7tr6/1)
