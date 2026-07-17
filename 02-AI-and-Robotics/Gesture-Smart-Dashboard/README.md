# 🎨 Gesture-Controlled Smart Dashboard

A real-time computer vision application built with **Python** and **OpenCV** that allows users to draw virtually using a colored object as a digital pen.

The project tracks a predefined color in real time, detects its position, and converts its movement into smooth drawing strokes on a virtual canvas.

---

## ✨ Features

- 🎥 Real-time webcam processing
- 🎯 Color-based object tracking using HSV color space
- 🖌️ Virtual drawing canvas
- 🧹 Clear canvas with a keyboard shortcut
- ⚡ Interactive HSV color calibration tool
- 🧩 Modular and object-oriented architecture
- 💻 Cross-platform Python implementation

---

## 📂 Project Structure

```text
Gesture-Controlled-Smart-Dashboard/
│
├── main.py
├── calibration.py
│
├── modules/
│   ├── camera_utils.py
│   ├── color_tracker.py
│   └── virtual_paint.py
│
├── requirements.txt
└── README.md
```

---

## 🛠 Technologies Used

- Python 3.x
- OpenCV
- NumPy

---

## 🚀 How It Works

The application follows this processing pipeline:

```text
Webcam
   │
   ▼
Capture Frame
   │
   ▼
Convert BGR → HSV
   │
   ▼
Generate Binary Mask
   │
   ▼
Morphological Filtering
   │
   ▼
Contour Detection
   │
   ▼
Object Center Detection
   │
   ▼
Virtual Canvas Drawing
   │
   ▼
Merge with Live Camera Feed
   │
   ▼
Display Final Output
```

---

## 🎯 Modules

### 📷 camera_utils.py

Responsible for:

- Opening the webcam
- Camera initialization
- Auto-exposure warm-up

---

### 🎨 color_tracker.py

Responsible for:

- HSV color segmentation
- Binary mask generation
- Noise removal
- Contour detection
- Object center estimation

---

### ✏️ virtual_paint.py

Responsible for:

- Creating a virtual drawing canvas
- Storing tracked points
- Drawing continuous strokes
- Merging the drawing with the camera frame

---

### 🎛 calibration.py

Interactive utility for selecting the optimal HSV range.

Features:

- Live HSV sliders
- Real-time mask preview
- Automatic HSV value generation

---

## ⌨️ Keyboard Controls

| Key | Action |
|-----|--------|
| **C** | Clear canvas |
| **Q** | Quit application |

---

## 🎥 Demo

![Demo](assets/demo.gif)

Example:

```
assets/demo.gif
assets/screenshot.png
```

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/Gesture-Controlled-Smart-Dashboard.git
```

Navigate into the project:

```bash
cd Gesture-Controlled-Smart-Dashboard
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python main.py
```

---

## 🧠 Computer Vision Concepts Used

- HSV Color Space
- Color Thresholding
- Binary Masks
- Morphological Operations
- Contour Detection
- Minimum Enclosing Circle
- Bitwise Image Operations


---

## 👩‍💻 Author

**Mona Al-Mutairi**

Computer Science Student

Interested in:

- Artificial Intelligence
- Computer Vision
- Machine Learning
- Deep Learning

---

## ⭐ If you like this project

Consider giving it a ⭐ on GitHub.
