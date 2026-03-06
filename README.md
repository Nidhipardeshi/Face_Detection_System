Face Detection System

A real-time Face Detection System built using Python and OpenCV.
The system detects human faces through a webcam and highlights them with bounding boxes using computer vision techniques.
This project demonstrates the basic implementation of face detection using Haar Cascade classifiers.

Project Overview

The main objective of this project is to detect human faces in real-time using a webcam feed. The system processes video frames and applies a pre-trained Haar Cascade model to identify faces.
When a face is detected, the system draws a bounding box around it and can trigger an alarm if required.

Technologies Used: 
Python
OpenCV
Haar Cascade Classifier
Computer Vision

Project Structure
FACE_DETECTION_SYSTEM
│
├── haarcascade/
│   └── haarcascade_frontalface_default.xml
│
├── alarm.py
├── alarm.wav
├── face_detection.py
├── README.md
│
├── __pycache__/
└── .pycache/

How It Works:
The webcam captures live video frames.
Each frame is converted to grayscale for faster processing.
The Haar Cascade classifier scans the frame to detect faces.
If a face is detected:
  - A rectangle (bounding box) is drawn around the face.
  - An alarm sound can be triggered.

Installation: 
- Clone the repository:
git clone https://github.com/yourusername/face-detection-system.git
- Move to the project directory:
cd face-detection-system
- Install required libraries:
pip install opencv-python

How to Run the Project
Run the main script:
python face_detection.py

The webcam will open and start detecting faces in real-time.

Press q to exit the program.

Features: 
Real-time face detection
Webcam integration
Bounding box visualization
Alarm alert system

Future Improvements:
Face recognition (identify specific people)
Mask detection
Security monitoring system
Deep learning based face detection

Author
Nidhi Pardeshi
