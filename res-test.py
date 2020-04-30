import cv2

capture = cv2.VideoCapture(0)


def make_1080():
    capture.set(3, 1920)
    capture.set(4, 1080)


def make_720():
    capture.set(3, 1280)
    capture.set(4, 720)


def make_480():
    capture.set(3, 640)
    capture.set(4, 480)


def change_res(width, height):
    capture.set(3, width)
    capture.set(4, height)


def rescale_frame(frame, percent=75):
    scale_percent = 75
    width = int(frame.shape[1] * scale_percent / 100)
    height = int(frame.shape[0] * scale_percent / 100)
    dim = (width, height)
    return cv2.resize(frame, dim, interpolation=cv2.INTER_AREA)


# make_1080()
while True:
    # Capture frame-by-frame
    ret, frame = capture.read()

    frame = rescale_frame(frame, percent=30)
    cv2.imshow('frame', frame)  # image show
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
capture.release()
cv2.destroyAllWindows()