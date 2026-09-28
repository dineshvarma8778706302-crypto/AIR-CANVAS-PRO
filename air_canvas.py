import cv2
import mediapipe as mp
import numpy as np
import math  # <-- Distance calculate panna ithu thevai

# MediaPipe setup
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)

cap = cv2.VideoCapture(0)

# Variables
px, py = 0, 0
canvas = None
draw_color = (0, 255, 0)
brush_size = 6  # Default brush size

while True:
    success, frame = cap.read()
    if not success:
        break
        
    frame = cv2.flip(frame, 1)
    h, w, c = frame.shape
    
    if canvas is None:
        canvas = np.zeros_like(frame)
        
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_frame)
    
    # TOP HEADER: Color Palette Buttons
    cv2.rectangle(frame, (20, 10), (120, 70), (255, 0, 0), cv2.FILLED)
    cv2.putText(frame, "BLUE", (35, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
    
    cv2.rectangle(frame, (140, 10), (240, 70), (0, 255, 0), cv2.FILLED)
    cv2.putText(frame, "GREEN", (150, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
    
    cv2.rectangle(frame, (260, 10), (360, 70), (0, 0, 255), cv2.FILLED)
    cv2.putText(frame, "RED", (290, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
    
    cv2.rectangle(frame, (380, 10), (500, 70), (50, 50, 50), cv2.FILLED)
    cv2.putText(frame, "CLEAR", (405, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
    
    # HAND TRACKING & DRAWING LOGIC
    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            index_tip = hand_landmarks.landmark[8]
            middle_tip = hand_landmarks.landmark[12]
            
            # --- PUTHU LOGIC: Thumb & Pinky Distance ---
            thumb_tip = hand_landmarks.landmark[4]
            pinky_tip = hand_landmarks.landmark[20]
            
            tx, ty = int(thumb_tip.x * w), int(thumb_tip.y * h)
            px_pinky, py_pinky = int(pinky_tip.x * w), int(pinky_tip.y * h)
            
            # Distance calculate pandrom
            distance = math.hypot(tx - px_pinky, ty - py_pinky)
            
            # Distance-a brush size-ku (2 to 35 pixels) map pandrom
            brush_size = int(np.interp(distance, [30, 250], [2, 35]))
            # ---------------------------------------------
            
            index_pip = hand_landmarks.landmark[6]
            middle_pip = hand_landmarks.landmark[10]
            
            cx, cy = int(index_tip.x * w), int(index_tip.y * h)
            
            index_is_up = index_tip.y < index_pip.y
            middle_is_up = middle_tip.y < middle_pip.y
            
            # MODE 1: HOVER / SELECTION MODE
            if index_is_up and middle_is_up:
                px_prev, py_prev = 0, 0
                cv2.circle(frame, (cx, cy), 15, draw_color, cv2.FILLED)
                
                if cy < 75:
                    if 20 <= cx <= 120: draw_color = (255, 0, 0)
                    elif 140 <= cx <= 240: draw_color = (0, 255, 0)
                    elif 260 <= cx <= 360: draw_color = (0, 0, 255)
                    elif 380 <= cx <= 500: canvas = np.zeros_like(frame)
                        
            # MODE 2: DRAW MODE
            elif index_is_up and not middle_is_up:
                # Pointer circle size-um dynamic aaga maarum
                cv2.circle(frame, (cx, cy), brush_size, draw_color, cv2.FILLED)
                
                if cy > 75:
                    if px_prev == 0 and py_prev == 0:
                        px_prev, py_prev = cx, cy
                    
                    # Brush size variable-a inga line thickness-ku pass pandrom
                    cv2.line(canvas, (px_prev, py_prev), (cx, cy), draw_color, brush_size)
                    px_prev, py_prev = cx, cy
    else:
        px_prev, py_prev = 0, 0
            
    # Video frame and canvas blend
    frame = cv2.add(frame, canvas)
    
    cv2.imshow("Air Canvas Pro - Dynamic Brush", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()