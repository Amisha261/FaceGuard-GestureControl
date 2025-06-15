# 👤 FaceGuard-GestureControl

A real-time face detection and hand gesture control system. This project enables a secure and intuitive interface where **face recognition is used as an authentication step**, and **hand gestures are used to control actions**. Ideal for security-aware, touch-free environments.

---

## 🚀 Features

* 📸 **Face Recognition** for identity verification
* ✋ **Hand Gesture Control** for real-time interaction
* 🔐 Personal training system using user’s own photos
* ⚙️ Easy configuration via `config.py`

---

## 📁 Project Structure

```
FaceGuard-GestureControl/
│
├── config.py               # Paths to training/testing image folders and settings
├── model_train.py          # Train face recognition on your images
├── mixed-images/           # Directory for storing mixed images (user + strangers)
├── user-images/            # Directory for storing the users's images
├── gesture_control.py      # Real-time hand gesture interface
├── utils/                  # Helper modules
├── requirements.txt        # Required packages
└── README.md               # This file
```

---

## ⚙️ Configuration

In the `config.py` file, set the following paths:

```python
User_photo_dir = "PATH/to/your_photo_directory" # Directory where the user's photos should reside
Mixed_photo_dir = "PATH/to/mixed_representation" # Directory where photos of mixed photos should reside
Model_dir = "./models"
```

> ✅ Make sure your **training directory contains only your images**.
> ✅ Testing directory should contain **a mix of your images and strangers’ images**.

---

## 👨‍💼 Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/Amisha261/FaceGuard-GestureControl
cd FaceGuard-GestureControl
```

### 2. Create and activate a Python 3.10 environment

Using `conda`:

```bash
conda create -n faceguard python=3.10
conda activate faceguard
```

Or using `venv`:

```bash
python3.10 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🧠 Training the Face Recognition Model through the face_recognition.ipynb file

```bash
python model_train.py
```

This script will:

* Read images from `TRAINING_DIR` in `config.py`
* Extract facial features
* Train and save the face recognition model

---

## ✋ Launching Gesture Control (Runs automatically when running the python notebook but if you want to run the program explicitly without face recognition)

```bash
python gesture_control.py
```

Once your face is authenticated, you can use gestures to interact with the system.

---

## 📌 Requirements (as per `requirements.txt`)

Typical packages used:

* `tensorflow` / `opencv-python` / `mediapipe`
* `scikit-learn`, `joblib`, `numpy`

> Use `pip freeze > requirements.txt` to update the file if you add new dependencies.

---

## 👨‍💻 Author

**Amisha Shah**
*Feel free to contribute or open issues!*

---