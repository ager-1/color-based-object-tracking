import cv2
import numpy as np 

# The below function is used to track the color of an object in a video stream using OpenCV.
# It captures video from the webcam, converts the frame to HSV color space, and creates a mask for the specified color range.
def tracking():
    cap=cv2.VideoCapture(0)
    lower_color=np.array(lc)  #lower color range
    upper_color=np.array(uc)  #upper color range
    while True:
        ret,frame=cap.read()
        if not ret:
            print("Failed to capture image")
            break
        hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV) #convert to HSV
        mask=cv2.inRange(hsv,lower_color,upper_color) #create mask
        contours,_=cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE) #find contours
        for cnt in contours:
            area=cv2.contourArea(cnt)
            if area>500:
                x,y,w,h=cv2.boundingRect(cnt) #bounding box
                cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2) #draw rectangle
                cv2.putText(frame,"Object",(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,0,0),2) #put text
        cv2.imshow("Color Tracking", frame) #show original frame
        cv2.imshow("Mask",mask) #show mask
        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break
    cap.release()
    cv2.destroyAllWindows()

# The below function is used to get the color range from the user and set the lower and upper color range.
def main():
    color_choice=input("Enter color (red, green, blue, yellow): ").strip().lower() #user input for color
    global lc #lower color range
    global uc #upper color range
    if color_choice == "red": #red color range
        lc=[0,120,70]
        uc=[10,255,255]
    elif color_choice == "green": #green color range
        lc=[40,40,40]
        uc=[80,255,255]
    elif color_choice == "blue": #blue color range
        lc=[100,150,0]
        uc=[140,255,255]
    elif color_choice == "yellow": #yellow color range
        lc=[20,100,100]
        uc=[30,255,255]
    else:
        print("Invalid color choice.") 
        exit() 
    tracking()

if __name__=="__main__":
    main()
