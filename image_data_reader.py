#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import os
import cv2
import numpy as np

class ImageDataReader():
    def __init__(self):
        super(ImageDataReader, self).__init__()
    
    # function to list all the files in a directory
    def list_files(self, dir):
        r = []
        for root, dirs, files in os.walk(dir):
            for name in files:
                r.append(os.path.join(root, name))
        return r

    # function to list all the files in a directory
    def load_images(self, imagefiles):
        train_image = []
        for imagefile in imagefiles:
            image = cv2.imread(imagefile)
            train_image.append(image)
        return train_image

    # function to return '.csv' file
    def find_annotations_files(files):
        sub = '.csv'
        return list(filter(lambda x: sub in x, files))

    def find_image_labels():
        return []

    def img_resize_to_black(image):
        target = np.zeros((720,960),dtype=np.uint8) ##change the size into (720,960) or any else.

        bgr_img = cv2.cvtColor(target, cv2.COLOR_GRAY2BGR)

        h = image.shape[0]
        w = image.shape[1]
        for i in range(h):
            for j in range(w):
                bgr_img[i, j, 0] = image[i, j, 0]
                bgr_img[i, j, 1] = image[i, j, 1]
                bgr_img[i, j, 2] = image[i, j, 2]

        return bgr_img

    def load_coco_image_data(self, dir):
        image_files = self.list_files(dir)
        images = self.load_images(image_files)
        train_label = ['Person','Person','Person','Person','Person','Person','Person','Person','Person','Person']
        train_boxes = [[(387.0, 71.1, 532.0, 393.1, 145.0, 322.0),
                      (494.31, 91.04, 506.01, 107.2, 11.7, 16.16),
                      (282.37, 86.79, 314.53, 183.81, 32.16, 97.02),
                      (526.17, 44.14, 616.67, 232.14, 90.5, 188.0),
                      (491.51, 81.19, 531.97, 166.53, 40.46, 85.34),
                      (477.88, 87.8, 491.58, 121.19999999999999, 13.7, 33.4),
                      (308.98, 76.76, 358.87, 225.49, 49.89, 148.73),
                      (71.97, 104.59, 131.46, 249.48, 59.49, 144.89),
                      (352.59, 136.15, 380.73999999999995, 166.99, 28.15, 30.84),
                      (52.18, 98.34, 74.07, 132.09, 21.89, 33.75),
                      (40.18, 94.65, 54.129999999999995, 117.2, 13.95, 22.55),
                      (3.3, 121.27, 86.53999999999999, 245.79, 83.24, 124.52),
                      (153.18, 61.92, 259.96000000000004, 179.74, 106.78, 117.82),
                      (26, 64, 639, 190, 613, 126)],
                     [(220.99, 263.96, 364.48, 474.90999999999997, 143.49, 210.95)],
                     [(0.0, 0.96, 133.07, 205.82000000000002, 133.07, 204.86)],
                     [(2.16, 1.98, 568.4499999999999, 480.0, 566.29, 478.02)],
                     [(1.44, 37.39, 425.71, 640.0, 424.27, 602.61),
                      (68.42, 124.92, 138.12, 228.99, 69.7, 104.07),
                      (3.51, 173.18, 94.46000000000001, 282.53, 90.95, 109.35),
                      (0.0, 130.16, 72.07, 198.12, 72.07, 67.96),
                      (350.97, 163.03, 427.0, 409.99, 76.03, 246.96)],
                     [(376.07, 114.71, 469.13, 355.56, 93.06, 240.85),
                      (177.67, 105.71, 283.71999999999997, 334.49, 106.05, 228.78),
                      (329.7, 140.59, 338.71999999999997, 166.78, 9.02, 26.19)],
                     [(22.96, 175.07, 276.95, 532.38, 253.99, 357.31)],
                     [(220.18, 64.14, 379.09000000000003, 300.59, 158.91, 236.45)],
                     [(354.5, 134.39, 458.35, 295.26, 103.85, 160.87)],
                     [(270.88, 154.67, 486.5, 474.30999999999995, 215.62, 319.64)]]
        return images, train_boxes, train_label

