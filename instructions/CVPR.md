# Executing Semantic Hyperlapse - CVPR

Here we describe the steps to generate the hyperlapsed version of a input video using Semantic Hyperlapse - CVPR.

### Prerequisites ###

* [matlab](https://www.mathworks.com/products/matlab.html) - Mathworks Matlab 2015a
* [opencv](https://github.com/opencv/opencv) - Open Source Computer Vision Library (tested with version 2.4.13.7)

### Execution ###

To download and build the executable, do the following steps:

```
$ git clone https://github.com/verlab/SemanticFastForward_CVPR_2018.git
```
Download the linux modified version of OpticalFlow extractor from Poleg's EgoSampling work. Compile it and extract the flow field.

```
$ ./optflow -v /data/example.mp4 -c default-config.xml
```

Download subrepositories that compose the code:

```
$ cd /codes/SemanticFastForward_CVPR_2018
$ git submodule update --init --recursive
$ git submodule update --recursive --remote
```

Start Matlab and do:

```
$ cd /codes/SemanticFastForward_CVPR_2018/_SemanticFastForward_JVCI_2018;
$ addpath('SemanticScripts');
$ ExtractAndSave('/data/example.mp4', 'face');
$ exit;
```

Run YOLO object detector to extract objects.

```
$ cd /opt/darknet
$ ./darknet detector demo cfg/coco.data cfg/yolo.cfg yolo.weights /data/example.mp4 /data/example_yolo_raw.txt
$ cd /codes/SemanticFastForward_CVPR_2018/python_codes
$ python generate_yolo_descriptor.py /data/example.mp4 /data/example_yolo_raw.txt /data/example_yolo_desc.csv
```

Restart Matlab and do:
```
$ cd /codes/SemanticFastForward_CVPR_2018;
$ addpath('LLC');
$ accelerate_video_LLC('/data/example.mp4', 'face', 'Speedup', 5, 'GenerateVideo', true);
```

The video will be generated on the same dir of the input video.