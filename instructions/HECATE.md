# Executing Yahoo HECATE

Here we describe the steps to generate the summarized subshot-based video using Yahoo HECATE.

### Prerequisites ###

* [opencv](https://github.com/opencv/opencv) - Open Source Computer Vision Library (tested with version 2.4.13.7)
* [ffmpeg](https://github.com/FFmpeg/FFmpeg) - Fast-Forward MPEG

OpenCV must be compiled with ffmpeg support !

### Execution ###

To download and build the executable, do the following steps:

```
$ git clone https://github.com/yahoo/hecate.git
$ cd hecate
$ vim Makefile.config
 - Set INCLUDE_DIRS and LIBRARY_DIRS to where your 
   opencv library is installed. Usually under /usr/local.
 - If your OpenCV version is 2.4.x, comment out the line 
   OPENCV_VERSION := 3
 - Save and exit
$ make all
$ make distribute
```

To generate the summarized video with **5 seconds**, just do:

```
$ ./distribute/bin/hecate -i /data/example.mp4 --generate_mov --lmov 5 -o /data/output/hecate
```

where **-i** is the input video, **-lmov** is the video output size and  **-o** is the output dir.