# 🎨 Air Canvas Pro - Virtual Hand-Tracking Drawing App

Air Canvas is a real-time Computer Vision application that allows you to draw in the air using just your fingers! Built with Python, OpenCV, and Google's MediaPipe, this project transforms your webcam into a virtual drawing board.

## ✨ Features

*   **✋ Real-Time Hand Tracking:** Accurately tracks 21 hand landmarks using MediaPipe.
*   **🧠 Smart Modes (Draw vs. Hover):** 
    *   Point your **Index Finger** to draw.
    *   Point both **Index & Middle Fingers** to pause drawing and just hover/select.
*   **🎨 Virtual Color Palette:** Select between Blue, Green, Red, or Clear the board by simply hovering over the on-screen buttons.
*   **🖌️ Dynamic Brush Size:** The thickness of your brush adjusts dynamically based on the distance between your **Thumb** and **Pinky Finger**. Bring them closer for a thin line, spread them apart for a thick stroke!

## 🛠️ Tech Stack

*   **Language:** Python
*   **Computer Vision:** OpenCV (`cv2`)
*   **Hand Tracking Model:** MediaPipe (`mediapipe`)
*   **Matrix Math:** NumPy (`numpy`)

## 🚀 Installation & Setup

**Note:** Ensure you are using **Python 3.10 or 3.11** for stable MediaPipe compatibility.

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/Air-Canvas-Pro.git](https://github.com/your-username/Air-Canvas-Pro.git)
   cd Air-Canvas-Pro