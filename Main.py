import cv2

class App:
    def __init__(self, camera: int = 0) -> None:
        self.camera = camera
        self.vid = cv2.VideoCapture(self.camera)
    
    def Loop(self):
        while True:
            ret, frame = self.vid.read()
            
            cv2.imshow('Window', frame)
            
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
        
        self.vid.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    App().Loop()