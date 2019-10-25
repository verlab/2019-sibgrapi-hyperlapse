# Executing video-related scripts on Matlab

To read and write videos on matlab on linux, it should be necessary to perform two operations:

* Change libstdc++ used by Matlab
```
$ cd /usr/local/MATLAB/R2016a/sys/os/glnxa64
$ sudo mv libstdc++.so.6 libstdc++.so.6.old
```
* Install gstreamer/ffmpeg wrapper
```
$ add-apt-repository ppa:mc3man/gstffmpeg-keep
$ apt update
$ apt-get install gstreamer0.10-ffmpeg
```

After that, Matlab should allow to read and write video files.