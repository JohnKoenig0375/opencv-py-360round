#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Title: Round360 Module for OpenCV-Python
Author: John Koenig
Project: opencv-py-360round
Version: 0.1.0
Date: 02DEC2018
Purpose: Provide a python wrapper to the OpenH264 package for data from the Samsung 360 Round Camera
Contact: JohnKoenig0375@gmail.com
Description:
    This module is in the planning phase
    It is designed to 
"""


#%%
#Import necessary libraries
import cv2
import os
import re

#%%
#Define Encoded File Format

#TODO
# - Define Samsung file id layout (I need this information from Samsung)


#%%
#Define Function LoadRaw360Round()
### Load a raw 360round data file (*.SLS)

#TODO
# - Load raw 360round data file


#%%
#Define Function DecodeOpenH264()
###Create OpenH264 decode/split command for raw 360round data

#TODO
# - Concatenate a custom command (string) for OpenH264 decode/split
# - Run custom OpenH264 command


#%%
#Define Function OpenCV_wrap()
###Wrap decoded/split 360round data in open-cv-pyton object

#TODO 
# - Point to the directory containing the decoded/split 360round data files
# - Load 17 video files into OpenCV
# - Load 1 audio file into [to be determined]
# - Load 1 distance file into python dictionary

split360_dir =  '/media/md33a/360_4tb_external/360_projects/GWU_capstone/lanterns_split360/'

#def OpenCV_wrap(split360_dir):
    
#Get file list
split360_files = os.listdir(split360_dir)

#Get of files in split360_dir
num_split360_files =len(split360_files)

#If num files not 19, end funtion
if len(split360_files) != 19:
    print('num_split360_files in split360_dir = %s' % (str(num_split360_files)))
    print('Total number of files must == 19')
    print('Make sure all 360round split files are present in the split360_dir and no other files')
    #return files

txt_filename = [file for file in split360_files if re.match('\S*\.txt',file) is not None][0]
wav_filename = [file for file in split360_files if re.match('(\S*\.wav)',file) is not None][0]
video_filenames = [file for file in split360_files if file not in [txt_filename,wav_filename]]

#for v in video_filenames:
    




'''
return txt_file_index


test = OpenCV_wrap(split360_dir)

print(test)
'''


#%%
#Additional Wrappers
#Additional wrapper functions for the decoded/split 360 round data will be added below






