# video-frame-extractor
A simple Python script to extract frames from a video at specified intervals.

### Features
- Extract frames at custom intervals (default is 1 second).
- Error handling for video reading and frame writing.

### Requirements
- Python
- OpenCV (`pip install opencv-python`)

### Frame Naming Convention
Frames are saved with the naming convention frame_X.png, where X starts from 1 and increments for each frame saved. 
This means:
- The first frame saved will be frame_1.png.
- Subsequent frames follow this sequence, e.g., frame_2.png, frame_3.png, etc.
- No leading zeros for single or double-digit frame numbers, making the file names straightforward and clean.

### How It Works
Opens a video file using OpenCV.
Calculates which frames to save based on the video's FPS and the desired interval.
Saves frames as PNG files in the specified output directory. Each frame file follows the frame_X.png format.
