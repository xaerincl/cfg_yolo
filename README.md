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
|      |``--header``       |``Arguments and Usage``  |Header text                |
+------+-------------------+-------------------------+---------------------------+
|      |``--usage-header`` |``Usage``                |Header text                |
+------+-------------------+-------------------------+---------------------------+
|      |``--ref-header``   |``Quick reference table``|Header text                |
+------+-------------------+-------------------------+---------------------------+
|      |``--args-header``  |``Arguments``            |Header text                |
+------+-------------------+-------------------------+---------------------------+
|``-s``|``--spacey``       |                         |Blank lines after headers  |
+------+-------------------+-------------------------+---------------------------+
|``-r``|``--rst``          |                         |Generate rst               |
+------+-------------------+-------------------------+---------------------------+
|``-e``|``--hierarchy``    |``#=-*+.``               |rst header order           |
+------+-------------------+-------------------------+---------------------------+
|``-d``|``--hide-default`` |                         |Hide default arg values    |
+------+-------------------+-------------------------+---------------------------+
|``-t``|``--truncate-help``|                         |Truncate help in this table|
+------+-------------------+-------------------------+---------------------------+
|      |``--header-depth`` |``1``                    |Header depth of top header |
+------+-------------------+-------------------------+---------------------------+
|      |``--encoding``     |``utf-8``                |Input file encoding        |
+------+-------------------+-------------------------+---------------------------+
|``-f``|``--function``     |``None``                 |Function to call in file   |
+------+-------------------+-------------------------+---------------------------+
|``-v``|``--version``      |                         |Show version               |
+------+-------------------+-------------------------+---------------------------+


