import keras
import numpy as np
import os
from keras.applications.mobilenet import preprocess_input
import json


class MobileNetHandler:
    def __init__(self, model_path, label2index):
        self.model = keras.models.load_model(model_path)
        self.label2index = json.load(open(label2index, encoding='utf-8'))
        self.index2label = {v: k for k, v in self.label2index.items()}
        self.image_size = (256, 256)

    def process(self, path):
        matrix = keras.utils.load_img(path, color_mode='rgb', target_size=self.image_size)
        matrix = np.stack([matrix], axis=0)
        matrix = preprocess_input(matrix)
        return matrix

    def predict(self, inputs):
        """
        inputs: (batch, 256, 256, 3)
        """
        outputs = self.model.predict(inputs)
        index = np.argmax(outputs, axis=1)
        prob = np.max(outputs, axis=1)
        name = np.asarray([self.index2label.get(i, '') for i in index])
        return index, prob, name





