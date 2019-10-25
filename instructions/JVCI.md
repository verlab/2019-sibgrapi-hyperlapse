# Executing Semantic Hyperlapse - JVCI

Here we describe the steps to generate the hyperlapsed version of a input video using Semantic Hyperlapse - JVCI.

### Prerequisites ###

* [matlab](https://www.mathworks.com/products/matlab.html) - Mathworks Matlab 2015a
* [opencv](https://github.com/opencv/opencv) - Open Source Computer Vision Library (tested with version 2.4.13.7)

### Execution ###

To download and build the executable, do the following steps:

```
$ git clone https://github.com/verlab/SemanticFastForward_JVCI_2018.git
```
Download the linux modified version of OpticalFlow extractor from Poleg's EgoSampling work. Compile it and extract the flow field.

```
$ ./optflow -v /data/example.mp4 -c default-config.xml
```

Start Matlab and do:

```
$ addpath('SemanticScripts');
$ ExtractAndSave('/data/example.mp4', 'face');
$ SpeedupVideo('/data', 'Example', 'face', 'Speedup', 5);
```

The video will be generated on **out** dir, under input video directory.

Compile Egocentric stabilizer. Create an experiment file, and run it over the accelerated video:

```
$ cd /codes/SemanticFastForward_ECCVW_2016/AcceleratedVideoStabilizer
$ mkdir build; cd build; cmake ..; make; 
$ ./EgoStabilizer /data/JVCI_files/egostabilizer_example.xml
```