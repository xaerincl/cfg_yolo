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



| argument name                | default ``     |    Description               |           
|:-----------------------------|:------------------------|:-----------------------------|
| `"-input"`  or  `"-i"`       |                         | `"path to the .cfg"`         |      
| `"-classes"`  or  `"-c"`     |                         | `"How many classes to detect"`|      
| `"-num_images"`  or  `"-n"`  |   6000                  | `"OPTIONAL: Number of training images "`|     
| `"--long"`                   | `"long"`                | `"long"`                     |    
| `"--long"`                   | `"long"`                | `"long"`                     |    
| `"--long"`                   | `"long"`                | `"long"`                     |    
| `"--long"`                   | `"long"`                | `"long"`                     |    
