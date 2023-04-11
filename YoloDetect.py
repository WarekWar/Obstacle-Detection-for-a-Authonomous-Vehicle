import cv2

CONFIDENCE_THRESHOLD = 0.4
NMS_THRESHOLD = 0.3
MULTIPLIER = 1

FONTS = cv2.FONT_HERSHEY_COMPLEX
COLORS = [(255,0,0),(255,0,255),(0, 255, 255), (255, 255, 0), (0, 255, 0), (255, 0, 0)]
GREEN =(0,255,0)
BLACK =(0,0,0)

class_names = []
with open("classes.txt", "r") as f:
    class_names = [cname.strip() for cname in f.readlines()]
#  setttng up opencv net
yoloNet = cv2.dnn.readNet('yolov4-tiny.weights', 'yolov4-tiny.cfg')

yoloNet.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
yoloNet.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA_FP16)

model = cv2.dnn_DetectionModel(yoloNet)
model.setInputParams(size=(416, 416), scale=1 / 255, swapRB=True)

def objectDetector(image):

    classes, scores, boxes = model.detect(image, CONFIDENCE_THRESHOLD, NMS_THRESHOLD)
    # creating empty list to add objects data
    data_list =[]
    for (classid, score, box) in zip(classes, scores, boxes):
        # define color of each, object based on its class id
        if(classid ==0 or classid==1 or classid==2 or classid==3 or classid==5 or classid==7):
            color= COLORS[int(classid) % len(COLORS)]

            label = "%s : %f" % (class_names[classid[0]], score)

            # draw rectangle on and label on object
            cv2.rectangle(image, box, color, 2)
            cv2.putText(image, label, (box[0], box[1]-14), FONTS, 0.5, color, 2)

            # getting the data
            # 1: class name  2: object width in pixels, 3: position where have to draw text(distance)
            if classid ==0: # person class id
                data_list.append([class_names[classid[0]],box[0], box[1], box[2], box[3]])
            elif classid ==2: # car class id
                data_list.append([class_names[classid[0]],box[0], box[1], box[2], box[3]])


    return data_list