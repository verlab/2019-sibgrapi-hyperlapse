# Executing Semantic Hyperlapse - ECCW

Here we describe the steps to generate the hyperlapsed version of a input video using Semantic Hyperlapse - ECCW.

### Prerequisites ###

* [matlab](https://www.mathworks.com/products/matlab.html) - Mathworks Matlab 2015a
* [opencv](https://github.com/opencv/opencv) - Open Source Computer Vision Library (tested with version 2.4.13.7)
* [boost](https://www.boost.org/) - Boost C++ library (tested with version 1.5)
* [armadillo](http://arma.sourceforge.net/) - Armadillo C++ library for linear algebra (tested with version 9.800.1 -- Horizon Scraper)

### Execution ###

To download and build the executable, do the following steps:

```
$ git clone https://github.com/verlab/SemanticFastForward_ECCVW_2016.git
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
$ ExtractAndSave('/data/example.mp4', 'face');
$ [~, non_semantic, semantic] = GetSemanticRanges('/data/example_face_extracted.mat');
$ SpeedupVideo('/data/ouput/eccw', 'Example', 'face', 3, 14, [10,250], [50,3000], [0,100], [500,8], 'Speedup', 5);
```

The video will be generated on **out** dir, under input video directory.

Compile Egocentric stabilizer. Create an experiment file, and run it over the accelerated video:

```
$ cd /codes/SemanticFastForward_ECCVW_2016/AcceleratedVideoStabilizer
$ mkdir build; cd build; cmake ..; make;
$ ./EgoStabilizer /data/egostabilizer_example.xml
```
