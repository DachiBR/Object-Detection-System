# Object Detection Syste,

A real-time screw counting application using OpenCV and Tkinter for GUI.

## Features
- Real-time video feed from a connected USB camera.
- Capture and process frames to count Objects.
- Display the number of detected screws on the GUI.

## Technologies Used
- Python
- OpenCV
- Tkinter
- PIL (Python Imaging Library)

## File Descriptions
- `main.py`: Entry point of the application.
- `camera.py`: Contains the `Camera` class to handle video capturing.
- `item_detection.py`: Contains the function to detect objects in an image.
- `gui.py`: Contains the `ScrewCounterApp` class to create and manage the GUI.

## Future Improvements
- Enhance detection algorithm for better accuracy.
- Add support for different item types.
- Implement a logging system to keep track of counts over time.
