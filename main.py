# Python=3.10.12

import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Model
from scipy.spatial.distance import cosine
from tensorflow.keras.applications import ResNet101
from tensorflow.keras.preprocessing import image as img_preprocess
from tensorflow.keras.applications.resnet import preprocess_input


gpu_devices = tf.config.experimental.list_physical_devices('GPU')

if gpu_devices:
    for device in gpu_devices:
        tf.config.experimental.set_memory_growth(device, True)
    # Set per-process GPU memory fraction
    tf.config.experimental.set_virtual_device_configuration(
        gpu_devices[0],
        [tf.config.experimental.VirtualDeviceConfiguration(memory_limit=int(0.5 * 1024))]
    )
else:
    pass

base_model = ResNet101(weights='imagenet', include_top=True)
model = Model(inputs=base_model.input, outputs=base_model.get_layer('avg_pool').output)

def preprocess_image(image_path):
    binary_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    rgb_image = cv2.cvtColor(binary_image, cv2.COLOR_GRAY2RGB)
    rgb_image = cv2.resize(rgb_image, (224, 224))
    img_array = np.array(rgb_image, dtype=np.float32)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)

    return img_array

def cosine_similarity(feature_vector1, feature_vector2):
    return 1 - cosine(feature_vector1, feature_vector2)

def findSignatureSimilarity(binary_image_path1, binary_image_path2, THRESHOLD):
    binary_image1 = preprocess_image(binary_image_path1)
    binary_image2 = preprocess_image(binary_image_path2)

    feature_vector1 = model.predict(binary_image1).flatten()
    feature_vector2 = model.predict(binary_image2).flatten()

    similarity_score = cosine_similarity(feature_vector1, feature_vector2)
    
    if similarity_score >= THRESHOLD:
        return "Matched"
    else:
        return "Unmatched"


image_path1, image_path2 = "test_1.jpg", "test_2.jpg"
THRESHOLD = 0.8
result = findSignatureSimilarity(image_path1, image_path2, THRESHOLD)
print(result)