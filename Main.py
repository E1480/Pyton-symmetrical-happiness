import cv2

class App:
    def __init__(self) -> None:
        self.vid = cv2.VideoCapture(0)
    
    def Loop(self):
        while True:
            ret, frame = self.vid.read()
            
            cv2.imshow('frame', frame)
            
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
        
        self.vid.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    App().Loop()