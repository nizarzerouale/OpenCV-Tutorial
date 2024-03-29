# OpenCV Tutorial

This repository contains a series of Python scripts and Jupyter notebooks designed to introduce and demonstrate various concepts and techniques in computer vision using OpenCV. The tutorials range from camera calibration and stereo image processing to 3D effects and depth map creation.

## Project Structure
.

├── 3D_effect.py 

├── Camera_Calibration.ipynb 

├── Camera_Calibration.py 

├── calibration_data.npz 

├── calibresult.png 

├── create_disparity_map.py 

├── epipolar_geometry_demo.py 

├── left*.jpg 

├── right.jpg
 
├── tsukuba_l.png 

└── tsukuba_r.png 

### Descriptions

- **3D_effect.py**: Demonstrates how to overlay a 3D object on a 2D image using camera calibration data.
- **Camera_Calibration.ipynb/.py**: Scripts for performing camera calibration to obtain camera matrix and distortion coefficients.
- **calibration_data.npz**: Saved camera calibration parameters obtained from `Camera_Calibration.py`.
- **calibresult.png**: The result of applying camera calibration to an image.
- **create_disparity_map.py**: Creates a disparity map from stereo images, useful for depth estimation.
- **epipolar_geometry_demo.py**: Illustrates the concepts of epipolar geometry, epipolar lines, and epipoles using stereo images.
- **left*.jpg & right.jpg**: Stereo image pairs used in various demonstrations, including epipolar geometry and depth mapping.
- **tsukuba_l.png & tsukuba_r.png**: Another set of stereo images for depth map creation.

## Setup

Ensure you have Python installed on your system. This project requires OpenCV, NumPy, and Matplotlib libraries. You can install these dependencies using pip:

```bash
pip install opencv-python numpy matplotlib ```

##Usage
Each script can be run individually to demonstrate a specific concept:

To perform camera calibration and save the parameters:

```bash
python Camera_Calibration.py```
To generate a 3D effect on a chessboard image:

```bash
python 3D_effect.py```
To create a disparity map from a pair of stereo images:

```bash
python create_disparity_map.py```
To explore epipolar geometry:

```bash
python epipolar_geometry_demo.py```

Please refer to the comments within each script for further details on their operation and modifications.
