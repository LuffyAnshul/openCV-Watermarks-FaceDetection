import cv2
import os

filename = 'video.avi'  # .avi, .mp4
frames_per_seconds = 24.0
my_res = '720p'

# ffmpeg- audio recording
# Set resolution for the video capture


def change_res(capture, width, height):
    capture.set(3, width)
    capture.set(4, height)


# Standard Video Dimensions Sizes
STD_DIMENSIONS = {
    "480p": (640, 480),
    "720p": (1280, 720),
    "1080p": (1920, 1080),
    "4k": (3840, 2160),
}


def get_dims(capture, res='1080p'):
    width, height = STD_DIMENSIONS['480p']
    if res in STD_DIMENSIONS:
        width, height = STD_DIMENSIONS[res]
    change_res(capture, width, height)
    return width, height
# Video Encoding, might require additional installs


VIDE0_TYPE = {
    'avi': cv2.VideoWriter_fourcc(*'XVID'),
    'mp4': cv2.VideoWriter_fourcc(*'XVID'),
}


def get_video_type(filename):
    filename, ext = os.path.splitext(filename)
    if ext in VIDE0_TYPE:
        return VIDE0_TYPE[ext]
    return VIDE0_TYPE['avi']


capture = cv2.VideoCapture(0)
dims = get_dims(capture, res=my_res)
video_type_cv2 = get_video_type(filename)

out = cv2.VideoWriter(filename, video_type_cv2, frames_per_seconds, dims)

while True:
    # Capture frame-by-frame
    ret, frame = capture.read()
    out.write(frame)
    # Display the resulting frame
    cv2.imshow('frame', frame)  # image show
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
capture.release()
out.release()
cv2.destroyAllWindows()
