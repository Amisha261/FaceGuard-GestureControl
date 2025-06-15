import numpy as np
from tensorflow.keras.utils import to_categorical
import cv2
import os
from sklearn.preprocessing import LabelEncoder
from sklearn.utils import shuffle
import mediapipe as mp
from utils import load_and_preprocess_images
import joblib
import cv2
import numpy as np

def train_model(model = None, config = None):
    positive_images, positive_labels = load_and_preprocess_images(config.User_photo_dir, 'User')
    negative_images, negative_labels = load_and_preprocess_images(config.Mixed_photo_dir, 'Others')

    X, y = np.vstack((positive_images, negative_images)), np.hstack((positive_labels, negative_labels))

    label_encoder = LabelEncoder()
    y_encoded = label_encoder.fit_transform(y)

    if not os.path.exists(os.path.abspath(f"{config.Model_dir}/label_encoder.pkl")):
        joblib.dump(label_encoder, f"{config.Model_dir}/label_encoder.pkl")

    y_categorical = to_categorical(y_encoded, num_classes=2)

    x, y_categorical = shuffle(X, y_categorical, random_state=42)

    # Train the model
    model.fit(X, y_categorical, epochs=20, batch_size=32, validation_split=0.2)

    return model