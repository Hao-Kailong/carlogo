import keras
import numpy as np
import os
from keras.applications.mobilenet import MobileNet, preprocess_input
import json


class MobileNetHandler:
    def __init__(self, weight_path, label2index):
        self.label2index = json.load(open(label2index, encoding='utf-8'))
        self.index2label = {v: k for k, v in self.label2index.items()}
        self.model = MobileNet(
            input_shape=(256, 256, 3),
            dropout=0.1,
            include_top=True,
            weights=None, 
            classes=len(self.label2index),
        )
        self.model.load_weights(weight_path)
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


class Factory:
    mobilenet = None

    @classmethod
    def genMobilenet(cls):
        if cls.mobilenet is not None:
            return cls.mobilenet
        else:
            cls.mobilenet = MobileNetHandler(
                weight_path='data/weights/ckpt1/weights.h5',
                label2index='data/LABEL2INDEX.json',
            )
            return cls.mobilenet





