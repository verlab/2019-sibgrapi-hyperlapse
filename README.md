# Uniform Fast-Forward

This repository contains code to perform uniform sampling on a input video.
To run it, just specify the following params:

```bash
python uniform_sampling.py -v < video_filename > -s < speedup_rate > -o < output_dir >
```

| Options                     | Description                         | Type      | Example                       |
| --------------------------: | ----------------------------------- | --------- | ----------------------------- |
| ` < video_filename > `      | Path and filename of the video.     | _String_  | `~/Data/MyVideos/myVideo.mp4` |
| ` < speedup_rate > `        | Speed-up rate                       | _Integer_ | `20`                          |
| ` < output_dir > `          | Path to save the output file.       | _String_  | `~/Data/MyVideos/out`         |

### Prerequisites ###

The code runs in **Python 2.7**, with the libraries **tqdm and opencv**.

* [tqdm](https://github.com/tqdm/tqdm) - A progress bar for Python CLI
* [opencv](https://github.com/opencv/opencv) - Open Source Computer Vision Library (tested with version 4.0)

All of these libraries could be installed using [pip](https://pypi.python.org/pypi/pip) (Python Package Index).

```
sudo -H pip install tqdm opencv
```

### Institution ###

Federal University of Minas Gerais (UFMG)  
Computer Science Department  
Belo Horizonte - Minas Gerais -Brazil 

### Laboratory ###

![VeRLab](https://www.dcc.ufmg.br/dcc/sites/default/files/public/verlab-logo.png)

**VeRLab:** Laboratory of Computer Vison and Robotics   
https://www.verlab.dcc.ufmg.br
