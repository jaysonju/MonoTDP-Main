# MonoTDP

This is the official implementation of "Geometry Uncertainty Projection Network for Monocular 3D Object Detection".

Download the KITTI dataset from [KITTI website](http://www.cvlibs.net/datasets/kitti/eval_object.php?obj_benchmark=3d), including left color images, camera calibration matrices and training labels.

Clone this project and then go to the code directory:

    git clone https://github.com/jaysonju/MonoTDP.git
    cd code

We train the model on the following environments:

    Python 3.6
    Pytorch 1.1
    Cuda 9.0

You can build the environment easily by installing the requirements:

    conda env create -f requirements.yml
    conda activate MonoTDP



## Citation

If you find our work useful in your research, please consider citing:

    @article{li2023monotdp,
      title={Monotdp: Twin depth perception for monocular 3d object detection in adverse scenes},
      author={Li, Xingyuan and Liu, Jinyuan and Lei, Yixin and Ma, Long and Fan, Xin and Liu, Risheng},
      journal={arXiv preprint arXiv:2305.10974},
      year={2023}
    }
