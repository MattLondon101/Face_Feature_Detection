# Face_Feature_Detection
Facial feature detection in Linux with Python

face_utils.py and facial_landmarks.py use the pre-trained facial landmark detector in dlib to overlay label
facial landmarks in images.

## Instructions

These instructions target builds in Linux,
specifically Windows Subsystem for Linux (WSL) and Python 3.6 in Visual Studio Code.
In Linux terminal run 'sudo -s' and enter password to run the program as root.

**Install Dependencies:**
```
$ sudo -H apt-get install build-essential cmake
$ sudo -H apt-get install libgtk-3-dev 
$ sudo -H apt-get install libboost-all-dev
$ pip3 install numpy
$ pip3 install scipy
$ pip3 install scikit-image
$ pip3 install imutils
$ pip3 install opencv-python
$ pip3 install dlib
```
See comments in cv_imports.py and run to import useful packages for computer vision.

**Label and Visualize Facial Landmarks**
The program is run with the following code structure:
```
$ python facial_landmarks.py --shape-predictor shape_predictor_68_face_landmarks.dat --image images/me1.jpg
```
me1.jpg is one of the example images in the images directory. You can add your own to the images directory.
Visualizations will appear in X11/XMING window.
Visualized images can be saved by right clicking image and clicking "Save Current Image".
Labeled example images are exhibited in the detected_images directory.


---
<p align="center">
Original Image
</p>
<p align="center">
  <img width="504" height="504" src="https://github.com/MattLondon101/Face_Feature_Detection/blob/master/images/me1.jpg?raw=true"
</p>

---
<p align="center">
Labelled Image
</p>
<p align="center">
<img width="504" height="504" src="https://github.com/MattLondon101/Face_Feature_Detection/blob/master/detected_images/me1.png?raw=true"
</p>

