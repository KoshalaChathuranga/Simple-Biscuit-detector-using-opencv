# Webcam Object Detection Readme

## Overview
This repository contains a simple webcam object detection script implemented in Python using the OpenCV library. The script captures frames from the webcam, processes each frame to detect a specified color range (green), and draws a bounding box around the detected object.

## Features
- **Webcam Capture**: Captures frames from the default camera.
- **Color Detection**: Detects objects within a specified color range (here, green).
- **Bounding Box**: Draws a bounding box around the detected object.
- **FPS Display**: Calculates and displays the Frames Per Second (FPS).

## Prerequisites
- Python 3.x
- OpenCV library (`cv2`)
- NumPy library (`numpy`)

## How to Run
1. Make sure you have Python installed on your machine.
2. Install the required dependencies using the following command:
   
   pip install opencv-python numpy
   
3. Run the webcam object detection script by executing the following command in the terminal:
   
   python main.py

## File Structure
- **main.py**: Python script containing the webcam object detection code.

## Color Detection Details
- The color range for object detection is specified in the script using HSV values.
- Modify the \`lower_bound\` and \`upper_bound\` variables to adjust the color range.

<p align="center">
  <img width="400" height="200" src="https://drive.google.com/uc?id=1rEKbW6g_MxTl4np0cY7ZqnapVAoZxb65" alt="Your Image Alt Text">
</p>

## Credits
- This script was created by me.

Feel free to fork and modify the code, add new features, or use it as a starting point for your own projects. If you encounter any issues or have suggestions for improvement, please create an issue or submit a pull request. Happy coding!
