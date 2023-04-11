import numpy as np
import cv2

MULTIPLIER = 1
def fillArray(a, b, c, d):
# left-up, right-up, right-down, left-down
    Points = np.array([[a, b], [a + c, b], [a + c, b + d], [a, b + d]])
    return Points


def initialize(a):
    if a == 1:
        im_src = cv2.imread("ReferenceImages/pomiary/pas1p.png")  # pas
        im_src = cv2.resize(im_src, (800 * MULTIPLIER, 600 * MULTIPLIER))
        pts_src = np.array([[153, 172], [464, 176], [522, 215], [72, 211]]) * MULTIPLIER  # pas
        pts_dst = np.array([[0, 0], [500, 0], [500, 600], [0, 600]])
        reference_point = np.array([[[410, 550]]])  # pas
        im_src = cv2.circle(im_src, (410, 550), 3, (0, 255, 255), -1)  # pas
        cap = cv2.VideoCapture("ReferenceImages/pomiary/pas.mp4")
        return im_src, pts_src, pts_dst, reference_point, cap
    elif a == 2:
        im_src = cv2.imread("ReferenceImages/pomiary/parking1p.PNG")  # parking cieslewskiego
        im_src = cv2.resize(im_src, (800 * MULTIPLIER, 600 * MULTIPLIER))
        pts_src = np.array([[353, 196], [598, 200], [759, 226], [322, 221]]) * MULTIPLIER  # parking cieslewskiego
        pts_dst = np.array([[0, 0], [555, 0], [555, 1000], [0, 1000]])
        reference_point = np.array([[[490, 528]]])  # kparking
        im_src = cv2.circle(im_src, (490, 528), 3, (0, 255, 255), -1)  # parking
        cap = cv2.VideoCapture("ReferenceImages/pomiary/parking1.mp4")
        return im_src, pts_src, pts_dst, reference_point, cap
    elif a == 3:
        im_src = cv2.imread("ReferenceImages/pomiary/cies1p.png")  # cies
        im_src = cv2.resize(im_src, (800 * MULTIPLIER, 600 * MULTIPLIER))
        pts_src = np.array([[344, 251], [556, 257], [772, 392], [219, 387]]) * MULTIPLIER  # chodnik
        pts_dst = np.array([[0, 0], [155, 0], [155, 500], [0, 500]])
        reference_point = np.array([[[490, 528]]])  # chodnik
        im_src = cv2.circle(im_src, (410, 520), 3, (0, 255, 255), -1)  # chodnik
        cap = cv2.VideoCapture("ReferenceImages/pomiary/cies.mp4")
        return im_src, pts_src, pts_dst, reference_point, cap