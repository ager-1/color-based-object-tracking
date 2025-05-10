# Real-Time Color-Based Object Tracking using OpenCV

This Python program uses OpenCV to track objects of a specific color in real time through your webcam. It identifies objects based on their HSV color range and highlights them with bounding rectangles.

## Features

- Real-time webcam input using OpenCV.
- Color detection using HSV color space.
- Tracks and highlights objects of a selected color.
- Displays both the original frame and the binary mask.

## How It Works

1. User is prompted to input a color (`red`, `green`, `blue`, `yellow`).
2. The program sets the HSV range based on the selected color.
3. It captures frames from the webcam.
4. Converts each frame to HSV color space.
5. Applies masking to isolate the specified color.
6. Detects contours and draws bounding boxes around the colored object.
7. Press `q` to quit the application.

## Language
- Python 3.13

## Libraries
- OpenCV
- Numpy