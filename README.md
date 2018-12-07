Welcome to opencv-py-360round

This repository is the final research product for capstone research by John Koenig in the Master of Data Science program at George Washington University in Washington, DC. (Research submitted 07DEC2018)

Download the project presentation here:
https://drive.google.com/file/d/1ZMl7sQl35cH1tLFPfZ0df5Eb3Mn2k9a3/view?usp=sharing

Download the techincal paper here:
https://drive.google.com/file/d/1EwymAORlaahkZ8iOKA238A8-sJoia4WN/view?usp=sharing

This project introduces a new workflow for preparing 360 video data for data science research and operations. Additionally, the researcher will propose a custom Python software package, which is designed to facilitate computer vision and data science on 360 video data.

##The Camera for Data Science - Samsung 360 Round
Among the pro 360 video cameras that are currently commercially available, the Samsung 360 Round stands out as uniquely suited for data science research. This camera was designed by Samsung and launched in October 2017. Though the camera was not designed specifically for data science, the researcher concludes that it is currently the best option for the 360 data scientist to conduct advanced research on 360 videos.

There are several features of the Samsung 360 Round that make it uniquely capable for data science. Most importantly, the camera is designed to be operated remotely through the Samsung 360 Round software suite. This capability could enable the data scientist to control and operate the camera through a Python API or the camera could be operated through automated scripts designed by the data scientist. The camera has additional features which are of interest to the 360 data scientist - stereo lenses (producing 3D video), an RJ45 port, the ability to record to Solid State Drive (SSD), 4k resolution, and a dust/water resistant camera housing.

No other 360 camera has this unique combination of features.


##Project Statement and Methodology
The researcher will attempt to develop an open-source solution that will enable data scientists with a new capability to decode and process raw 360 video files from the Samsung 360 Round camera by using a convenient Python software package.

The methodology for this project will be exploratory and the researcher will develop all necessary software in order to decode a test 360 video file using a custom Python software package and load it into a computer vision framework for processing and analysis.

The purpose of this project is to enable other data scientists to easily conduct research on raw data from the Samsung 360 Round. This paper will conclude by outlining a technology roadmap for the future of data science research on 360 video data.


##opencv-py-360round - Alpha Version
The initial version of the opencv-py-360round package will be an alpha version that is still in the development and testing phase. This new project will be based on a fork of the existing opencv-python software package and will build four separate pre-built distributions that will include all the original functionality of opencv-python with 2 new capabilities.

First, opencv-py-360round will include additional code in the setup.py file for opencv-python that will install openh264 as a dependency in each of the four built distributions. Second, a new module will be added that will be named “round360.” The round360 module will contain all of the new functionality necessary in order to send raw 360 video data to openh264 for decoding. The round360 module will also include code necessary to download the test video file (described above) and run the testing function. There is no planned support for encoding in the H.264 codec.

Once the raw 360 data is decoded/split, the round360 module will take the 17 split videos and load them into OpenCV as video captures. This will complete the data science workflow for 360 video data and the data will then be ready for processing and analysis.



