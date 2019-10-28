# Executing Semantic Hyperlapse - ICIP

Here we describe the steps to generate the hyperlapsed version of a input video using Semantic Hyperlapse - ICIP.

### Prerequisites ###

* [matlab](https://www.mathworks.com/products/matlab.html) - Mathworks Matlab 2015a
* [opencv](https://github.com/opencv/opencv) - Open Source Computer Vision Library (tested with version 2.4.13.7)

### Execution ###

To download and build the executable, do the following steps:

```
$ git clone https://github.com/verlab/SemanticFastForward_ICIP_2016.git
```
Download the linux modified version of OpticalFlow extractor from Poleg's EgoSampling work. Compile it and extract the flow field.

```
$ wget https://github.com/verlab/2019-sibgrapi-hyperlapse/blob/master/src/Vid2OpticalFlowCSV.tar.gz
$ tar xvzf Vid2OpticalFlowCSV.tar.gz
$ cd Vid2OpticalFlowCSV; make;
$ ./optflow -v /data/example.mp4 -c default-config.xml
```

Start Matlab and do:

```
$ addpath('SemanticScripts');
$ ExtractAndSave('/data/example.mp4');
$ [~, non_semantic, semantic] = GetSemanticRanges('/data/example_face_extracted.mat');
$ [semantic_speed, non_semantic_speed] = SpeedupOptimization(non_semantic, semantic, 5, 100, 15, 20, 0);
$ SpeedupVideo('/data', 'Example', semantic_speed, non_semantic_speed, [10,250], [50,3000], [0,100], [500,8], 'Speedup', 5);
```

The video will be generated on **out** dir, under output video directory.
