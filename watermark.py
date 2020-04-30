import numpy as np
import cv2

from utils import CFEVideoConf, image_resize

cap = cv2.VideoCapture(0)

save_path = 'saved-media/watermarks.mp4'
frames_per_seconds = 24
config = CFEVideoConf(cap, filepath=save_path, res='720p')
out = cv2.VideoWriter(save_path, config.video_type, frames_per_seconds, config.dims)

img_path = 'images/logos/cfe-coffee.jpg'
logo = cv2.imread(img_path, -1)
watermark = image_resize(logo, height=100, width=200)
watermark = cv2.cvtColor(watermark, cv2.COLOR_BGR2BGRA)
# grayscale watermark
cv2.imshow('watermark', watermark)


while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # print(frame[50, 150])  # numpy array's
    # start_cord_x = 50
    # start_cord_y = 150
    # color = (255, 0, 0)  # BGR 0- 255
    # stroke = 2
    # w = 100
    # h = 200
    # end_core_x = start_cord_x + w
    # end_core_y = start_cord_y + h
    # cv2.rectangle(frame, (start_cord_x, start_cord_y), (end_core_x, end_core_y), color, stroke)
    #
    # print(frame[start_cord_x: end_core_x, start_cord_y: end_core_y])

    frame_h, frame_w, frame_c = frame.shape
    # print(frame.shape)
    # overlay with 4 channels BGR and Alpha
    overlay = np.zeros((frame_h, frame_w, 4), dtype='unit8')


    # out.write(frame)
    # Display the resulting frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()