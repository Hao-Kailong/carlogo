import keras
import json
from keras.applications.mobilenet import MobileNet, preprocess_input
from keras.utils import load_img
import numpy as np


label2index = json.load(open('data/LABEL2INDEX.json', encoding='utf-8'))
index2label = {v: k for k, v in label2index.items()}

model = MobileNet(
    input_shape=(256, 256, 3),
    dropout=0.1,
    include_top=True,
    weights=None, 
    classes=len(label2index),
)

model.load_weights('data/weights/ckpt1/weights.h5')

matrix = load_img(
    "data/images/吉利.jpg", 
    color_mode='rgb', 
    target_size=(256, 256))
matrix = np.stack([matrix], axis=0)
matrix = preprocess_input(matrix)


outputs = model.predict(matrix)
index = np.argmax(outputs, axis=1)
prob = np.max(outputs, axis=1)
name = np.asarray([index2label.get(i, '') for i in index])
print(index, prob, name)




