import cv2


def converter(video_location):
    video = cv2.VideoCapture(video_location)
    counter = 0
    while (video.isOpened()):
        ret, frame = video.read()
        if ret:
            cv2.imwrite('images_from_video/image'+str(counter)+'.jpg', frame)
            counter = counter + 1
        else:
            break
    video.release()
    return True


if __name__ == '__main__':
    video_location = 'meklit-video.mp4'
    converter(video_location)
    print 'the job is done'
