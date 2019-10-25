# Executing Uniform sampling

Here we describe the steps to generate the traditional fast-forward version from an input video.

### Prerequisites ###

* [opencv](https://github.com/opencv/opencv) - Open Source Computer Vision Library (tested with version 2.4.13.7)

OpenCV must be compiled with ffmpeg/gstreamer support !

### Execution ###

Download the python script and execute the code as following:

```
$ git clone https://github.com/verlab/2019-sibgrapi-hyperlapse.git
$ cd 2019-sibgrapi-hyperlapse
$ python uniform_sampling.py -i /data/example.mp4  -o /data/output/uniform -s 10
```
where **-i** is the input video, **-o** is the output dir and **-s** is the speed-up rate.