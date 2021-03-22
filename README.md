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


Usage
=====

::

    usage: argdown [-h] [-] [--license] [--header HEADER]
                   [--usage-header USAGE_HEADER] [--ref-header REF_HEADER]
                   [--args-header ARGS_HEADER] [-s] [-r] [-e HIERARCHY] [-d] [-t]
                   [--header-depth HEADER_DEPTH] [--encoding ENCODING]
                   [-f FUNCTION] [-v]
                   [src_file [src_file ...]]
    

Arguments
=========
Quick reference table
---------------------
+------+-------------------+-------------------------+---------------------------+
|Short |Long               |Default                  |Description                |
+------+-------------------+-------------------------+---------------------------+
|``-h``|``--help``         |                         |Show help                  |
+------+-------------------+-------------------------+---------------------------+
|``-`` |                   |                         |Read from STDIN            |
+------+-------------------+-------------------------+---------------------------+
|      |``--license``      |                         |Print license              |
+------+-------------------+-------------------------+---------------------------+




| argument name                | default `dest_name`     |    Description               |           
|:-----------------------------|:------------------------|:-----------------------------|
| `"--long"`                   | `"long"`                | 
| `"--long", "-s"`             | `"long"`                |
| `"-s", "--long1", "--long2"` | `"long1"`               |
| `"-s", "-x"`                 | `"s"`                   |
