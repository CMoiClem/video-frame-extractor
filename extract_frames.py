import cv2
import os

def extract_frames(video_path, output_dir, interval_seconds=1): #change interval here
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    cap = cv2.VideoCapture(video_path, cv2.CAP_FFMPEG)
    if not cap.isOpened():
        raise ValueError("Could not open video file")

    fps = int(cap.get(cv2.CAP_PROP_FPS))
    frame_interval = fps * interval_seconds
    frame_count = 0
    saved_count = 1

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        if frame_count % frame_interval == 0:
            cv2.imwrite(os.path.join(output_dir, f'frame_{saved_count}.png'), frame)
            saved_count += 1
        
        frame_count += 1

    cap.release()
    print(f"Extracted {saved_count - 1} frames")

if __name__ == "__main__":
    video_path = 'video.mp4' #change video path here
    output_dir = 'frames_folder' #change output path here
    extract_frames(video_path, output_dir)