# cfg_yolo

Script to create your own .cfg to train a Darknet YOLO model


# How to use

First clone the repo or download it by clicking here: https://github.com/xaerincl/cfg_yolo/archive/refs/heads/main.zip


In order to create the .cfg file for your custom YOLOv4 model run:
```
$ python cfg_create.py -i yolov4.cfg -c <number of classes to train> 
```


Example 2:

If you want to train a tiny-yolov3 to detect 6 different classes you can run:
```
$ python cfg_create.py -i yolov3-tiny.cfg -c 6
```


Arguments
=========



| argument name                | default      |    Description               |           
|:-----------------------------|:------------------------|:-----------------------------|
| `"-input"`  or  `"-i"`       |                         | `"path to the .cfg"`         |      
| `"-classes"`  or  `"-c"`     |                         | `"How many classes to detect"`|      
| `"-num_images"`  or  `"-n"`  |   6000                  | `"OPTIONAL: Number of training images "`|     
| `"-width"`  or  `"-wi"`  |   416                  | `"OPTIONAL: network size- width "`|     
| `"-height"`  or  `"-he"`  |   416                  | `"OPTIONAL: network size- height "`|     
| `"-batches"`  or  `"-b"`  |   64                  | `"OPTIONAL: batch size during train  "`|  
| `"-subdivisions"`  or  `"-sub"`  |   32                  | `"OPTIONAL: subdivisions during train  "`| 
| `"-no_flip"`    |   True                  | `"OPTIONAL: use -no_flip to set flip=0 "`|   

only use -no_flip if you train the model to distinguish Left and Right objects as separate classes (left/right hand, left/right-turn on road signs, ...).

If you are in doubt about any parameter value you should check ![AlexeyAB darknet repo](https://github.com/AlexeyAB/darknet)

![AlexeyAB darknet repo](https://github.com/AlexeyAB/darknet)
