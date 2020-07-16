# Prerequisite
- Ubuntu 18.04
- GTX 1080Ti
- [Nvidia Driver >= 440](#jump)
- Cuda >= 10.2
- cuDNN >= 7.6.5
- CMake >= 3.12
- OpenCV >= 3.2


# Preparation
```bash
$ git clone https://github.com/AlexeyAB/darknet.git
$ 
```

# How to train (to detect your custom objects):
Training Yolo V4-Tiny:
1. Downlaod [file with the first 29-convolutional layers of yolov4-tiny](https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v4_pre/yolov4-tiny.conv.29)
2. Create file `yolo-obj.cfg` with the same content as in `yolov4-custom.cfg` (or copy `yolov4-custom.cfg` to `yolo-obj.cfg)` and:

- change line batch to [`batch=64`](https://github.com/AlexeyAB/darknet/blob/0039fd26786ab5f71d5af725fc18b3f521e7acfd/cfg/yolov3.cfg#L3)

- change line subdivisions to [`subdivisions=16`](https://github.com/AlexeyAB/darknet/blob/0039fd26786ab5f71d5af725fc18b3f521e7acfd/cfg/yolov3.cfg#L4)

- change line max_batches to (`classes*2000` but not less than number of training images, but not less than number of training images and not less than `6000`), f.e. [`max_batches=6000`](https://github.com/AlexeyAB/darknet/blob/0039fd26786ab5f71d5af725fc18b3f521e7acfd/cfg/yolov3.cfg#L20) if you train for 3 classes

- change line steps to 80% and 90% of max_batches, f.e. [`steps=4800,5400`](https://github.com/AlexeyAB/darknet/blob/0039fd26786ab5f71d5af725fc18b3f521e7acfd/cfg/yolov3.cfg#L22)

- set network size `width=416 height=416` or any value multiple of 32, e.g. 224

- change line   `classes=80 ` to your number of objects in each of 3 `[yolo]`-layers

- change [`filters=255`] to filters=(classes + 5)x3 in the 3 `[convolutional]` before each `[yolo]` layer, keep in mind that it only has to be the last `[convolutional]` layers before each of the `[yolo]` layers 


So if `classes=1` then should be `filters=18`. If `classes=2` then write `filters=21`.


<span id="jump">Install Nvidia Driver</span>

![](resources/1.png)
