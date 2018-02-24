import face_recognition
import cv2
import speak
import os,time


class VideoLogin:

    def __init__(self):
        # Get a reference to webcam #0 (the default one)
        self.video_capture = cv2.VideoCapture(0)
        
        self.known_face_encodings,self.known_face_names = self.load_images_from_folder()
        
        # Initialize some variables
        self.face_locations = []
        self.face_encodings = []
        self.face_names = []
        self.process_this_frame = True


    def __del__(self):
        # Release handle to the webcam
        self.video_capture.release()
        

    #Return face encodings and face names for all images in folder
    def load_images_from_folder(self,folder="image\Login"):
        face_names = []
        face_encodings = []
        for filename in os.listdir(folder):
            img = cv2.imread(os.path.join(folder,filename))
            #print(os.path.join(folder,filename))
            if img is not None:
                face_encodings.append(face_recognition.face_encodings(img)[0])
                face_names.append(os.path.splitext(os.path.basename(filename))[0])
        return face_encodings,face_names


    def recognize(self):
        #Not Recognized
        rec = False
        #To get good Quality Image
        while not rec:
            # Grab a single frame of video
            ret, frame = self.video_capture.read()

            # Resize frame of video to 1/4 size for faster face recognition processing
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

            # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
            rgb_small_frame = small_frame[:, :, ::-1]

            # Only process every other frame of video to save time
            if self.process_this_frame:
                # Find all the faces and face encodings in the current frame of video
                self.face_locations = face_recognition.face_locations(rgb_small_frame)
                self.face_encodings = face_recognition.face_encodings(rgb_small_frame, self.face_locations)

                self.face_names = []
                for face_encoding in self.face_encodings:
                    # See if the face is a match for the known face(s)
                    matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
                    name = "Unknown"

                    # If a match was found in known_face_encodings, just use the first one.
                    if True in matches:
                        first_match_index = matches.index(True)
                        name = self.known_face_names[first_match_index]
                        speak.say(name+" You are recognized")
                        rec = True

                    self.face_names.append(name)

            self.process_this_frame = not self.process_this_frame


            # Display the results
            for (top, right, bottom, left), name in zip(self.face_locations, self.face_names):
                # Scale back up face locations since the frame we detected in was scaled to 1/4 size
                top *= 4
                right *= 4
                bottom *= 4
                left *= 4

                # Draw a box around the face
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

                # Draw a label with a name below the face
                cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

            # Display the resulting image
            #cv2.imshow('Video', frame)
            speak.say("Logging to Vision Aid")
            cv2.destroyAllWindows()

#Main method
def main():
    Video = VideoLogin()
    Video.recognize()

if __name__ == "__main__":
    main()
