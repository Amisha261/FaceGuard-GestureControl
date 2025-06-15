import os
import cv2
from tensorflow.keras.layers import Conv2D, Flatten, Dense, MaxPooling2D, Dropout
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizer import Adam
import numpy as np

def load_and_preprocess_images(image_dir, label, target_size=(64, 64)):
    images = []
    labels = []

    for image_file in os.listdir(image_dir):
        image_path = os.path.join(image_dir, image_file)
        img = cv2.imread(image_path)

        if img is None:
            continue

        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        resized_img = cv2.resize(gray_img, target_size)
        normalized_img = resized_img / 255.0

        images.append(normalized_img)
        labels.append(label)

    images = np.array(images).reshape(-1, target_size[0], target_size[1], 1)
    return images, labels

def create_model(input_size = [], loss = "", model_name = "face_rec" ,config = None):
    model = Sequential()

    model.add(Conv2D(32, (3, 3), activation='relu', input_shape=tuple(input_size)))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))

    model.add(Conv2D(64, (3, 3), activation='relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))

    model.add(Flatten())
    model.add(Dense(128, activation='relu'))
    model.add(Dropout(0.5))

    # Softmax layer for two categories
    model.add(Dense(2, activation='softmax'))  # Two output classes: Person and Others

    # Compile the model using categorical crossentropy
    model.compile(optimizer=Adam(learning_rate=0.0001), loss=loss, metrics=['accuracy'])

    model.save(f'{config.Model_dir}/{model_name}.h5')

    return model
