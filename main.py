########################################################################################################################
# @author: Amato Francesco
########################################################################################################################

# PREVIOUS INFORMATION:

# OPENCV is an opensource computer-vision library, provided by some people who write some useful code (for example
# pre-trained classifiers, in this case we are going to use some pre-trained classifiers on "frontal faces")

# To download opencv see this link: https://pypi.org/project/opencv-python/

# You have also to download, in the same folder of this script, another file, which contains the pre-trained classifier that I
# mentioned before (.xml file).
# You can find what I am saying at this link (read the copyright section before downloading & using it) : 
#      https://github.com/opencv/opencv/tree/master/data/haarcascades/haarcascade_frontalface_default.xml

# You can find many other Haar Cascade data at this link... check if you're interested:
#      https://github.com/opencv/opencv/tree/master/data/haarcascades

########################################################################################################################
# SCRIPT:

import cv2

# Load some pre-trained data on face "frontals" from opencv (haar cascade algorithm)
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Capture video from your video-camera ( 0 stands for your default video-camera)
video_capture = cv2.VideoCapture(0)

# Iterate face detection for every frame captured by your video-camera
while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    # We must have to convert our frame to grayscale, because of how Haar Cascade works
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces (apply haar cascade algorithm to our img, to see how many faces there are)
    # Those are the coordinates of all the faces that are found (face_coordinates is an array of array, which contains
    # each coordinates for each face which has been detected)
    faces = faceCascade.detectMultiScale(gray)

    # Now we want to put a rectangle around each face (color green in this case... change color attributes if you're
    # interested on different rectangle colour)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Show the result of the detection
    cv2.imshow('Detecting faces', frame)

    # Wait that the "q button" on the keyboard is been pressed, to then close the detecting app
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        # When everything is done, release the capture
        video_capture.release()
        cv2.destroyAllWindows()

# Many other features can be added to this software, for example it can be implemented both face detection both
# face recognition
