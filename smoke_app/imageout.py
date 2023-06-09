import torch
from matplotlib import pyplot as plt
import numpy as np
import cv2

model = torch.hub.load('ultralytics/yolov5', 'custom', path='weights/yolov5ss.pt', force_reload=True)

def photo(image):
    results = c_model(img)
    return results