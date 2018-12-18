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
import numpy as np

import pdb
#pdb.set_trace()


split360_dir =  '/media/md33a/360_4tb_external/360_projects/GWU_capstone/lanterns_split360/'   #For testing


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

#Open 19 files in target directory
def OpenCV_wrap(split360_dir):
    
    #Get file list
    split360_files = os.listdir(split360_dir)
    
    #Get of files in split360_dir
    num_split360_files =len(split360_files)
    
    #If num files not 19, end funtion
    if len(split360_files) != 19:
        print('num_split360_files in split360_dir = %s' % (str(num_split360_files)))
        print('Total number of files must == 19')
        print('Make sure all 360round split files are present in the split360_dir and no other files')
        return split360_files
    
    txt_filename = [file for file in split360_files if re.match('\S*\.txt',file) is not None][0]
    wav_filename = [file for file in split360_files if re.match('(\S*\.wav)',file) is not None][0]
    video_filenames = [file for file in split360_files if file not in [txt_filename,wav_filename]]
    
    round360_list = []
    
    #Open 17 videos and append to video list
    for v in video_filenames:
    
        #Create a VideoCapture object and read from input video file
        cap = cv2.VideoCapture(split360_dir + video_filenames[0])
     
        #Check if video file opened successfully
        if (cap.isOpened()== False): 
            print("Error opening video stream or file")
     
        round360_list.append(cap)
     
    #When everything done, release the video capture object
    cap.release()
     
    #Closes all the frames
    cv2.destroyAllWindows()
    
    return (round360_list, video_filenames, txt_filename, wav_filename)



#%%
#Define Function OpenCV_PlayAll()
###Plays each video in directory containing split 360 Round files (17 video files)

def OpenCV_PlayAll(split360_dir):
    
    #Get file list
    split360_files = os.listdir(split360_dir)
    
    #Get of files in split360_dir
    num_split360_files =len(split360_files)
    
    #If num files not 19, end funtion
    if len(split360_files) != 19:
        print('num_split360_files in split360_dir = %s' % (str(num_split360_files)))
        print('Total number of files must == 19')
        print('Make sure all 360round split files are present in the split360_dir and no other files')
        return split360_files
    
    txt_filename = [file for file in split360_files if re.match('\S*\.txt',file) is not None][0]
    wav_filename = [file for file in split360_files if re.match('(\S*\.wav)',file) is not None][0]
    video_filenames = [file for file in split360_files if file not in [txt_filename,wav_filename]]
    
    video_counter = 0
    
    #Open 17 videos and append to video list
    for v in video_filenames:
    
        #Create a VideoCapture object and read from input video file
        cap = cv2.VideoCapture(split360_dir + v)
     
        #Check if video file opened successfully
        if (cap.isOpened()== False): 
            print('Error opening video stream or file')
        else:
            print('Playing Video %s -- %s' % (str(video_counter),str(v)))
     
        # Read until video is completed
        while(cap.isOpened()):
            # Capture frame-by-frame
            ret, frame = cap.read()
            if ret == True:
                # Display the resulting frame
                cv2.imshow('Frame',frame)
     
            # Press Q on keyboard to  exit
            if cv2.waitKey(1000) & 0xFF == ord('q'):
                break
     
            # Break the loop
            else: 
                break
        
        video_counter += 1
     
    #When everything done, release the video capture object
    cap.release()
     
    #Closes all the frames
    cv2.destroyAllWindows()
    
    return None







#%%
#Additional Wrappers
#Additional wrapper functions for the decoded/split 360 round data will be added below






