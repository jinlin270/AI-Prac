# -*- coding: utf-8 -*-
"""simple_train_yolo.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1gperMUaocWZS_1XJwIjsEH70bDNnH0DT
"""


curr_dir = "/Users/linjin/Downloads/Yolo"


import os

from ultralytics import YOLO

# import torch

# Model
# model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

# Load a model
model = YOLO("yolov5n.pt")  # load pre trained model

# Use the model
results = model.train(
    data=os.path.join(curr_dir, "google_colab_config.yaml"),
    epochs=2,
    verbose=True,
)  # train the model

model.save("yolov5_weights.pt")

# results = model.val()

# results = model("/Users/linjin/Downloads/Yolo/Data/Test/images/0.jpg")
# success = model.export(format="onnx")


# !scp -r /content/runs curr_dir