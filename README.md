# Face_Feature_Detection
Facial feature detection in Linux with Python

face_utils.py and facial_landmarks.py use the pre-trained facial landmark detector in dlib to overlay label
facial landmarks in images.

## Instructions

These instruction targeted to builds in Linux.
Specifically, Windows Subsystem for Linux (WSL) and Python 3.6 in Visual Studio Code.

Install Dependencies:
```
$ sudo -H apt-get install build-essential cmake
$ sudo -H apt-get install libgtk-3-dev
$ sudo -H apt-get install libboost-all-dev
$ pip3 install numpy
$ pip3 install scipy
$ pip3 install scikit-image
$ pip3 install opencv-python
$ pip3 install dlib
```
See comments in cv_imports.py and run to import useful packages for computer vision.







