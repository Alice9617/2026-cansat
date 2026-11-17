import cv2
import numpy as np
from sklearn.cluster import DBSCAN

low_color1=np.array([0,50,50])
high_color1=np.array([6,255,255]) #赤色指定１
low_color2=np.array([174,50,50])
high_color2=np.array([180,255,255]) #赤色指定２
coordinates_x = {}
coordinates_y = {}
height = 1080
width = 1920

def detect_target(filepass):
    filepass="C:/Users/delic/Downloads/17m_20250917_150945.jpg"
    img=cv2.imread(filepass)

    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    mask1=cv2.inRange(hsv,low_color1,high_color1)
    mask2=cv2.inRange(hsv,low_color2,high_color2)
    mask=mask1+mask2                              #マスク作成
    masked_img=cv2.bitwise_and(img,img,mask=mask)

    gray=cv2.cvtColor(masked_img,cv2.COLOR_BGR2GRAY)
    _,binary=cv2.threshold(gray,0,255,cv2.THRESH_OTSU)

    kernel_dilate = np.ones((11, 11), np.uint8)
    kernel_erode = np.ones((5, 5), np.uint8)

    # 先に膨張させる
    dilated = cv2.dilate(
    binary,
    kernel_dilate,
    iterations=1
    )

    # そのあと収縮させる
    closed = cv2.erode(
    dilated,
    kernel_erode,
    iterations=1
    )

    temp= np.where(closed==255)                   #座標付与
    points = np.column_stack((temp[1], temp[0]))  #密集している座標を探す
    db = DBSCAN(eps=5, min_samples=20)
    labels = db.fit_predict(points)    
    valid_labels = labels[labels != -1]           #コーンのラベルだけ残す
    unique, counts = np.unique(valid_labels, return_counts=True)
    cone_label = unique[np.argmax(counts)]
    cone_points = points[labels == cone_label]

    top = cone_points[np.argmin(cone_points[:,1])]       #コーンのラベルの３点を習得
    left = cone_points[np.argmin(cone_points[:,0])]
    right = cone_points[np.argmax(cone_points[:,0])]
    
    coordinates_x["top"] = top[0]
    coordinates_y["top"] = top[1]
    coordinates_x["left"] = left[0]
    coordinates_y["left"] = left[1]
    coordinates_x["right"] = right[0]
    coordinates_y["right"] = right[1]
    
    cv2.line(img,(coordinates_x["top"],coordinates_y["top"]),(coordinates_x["right"],coordinates_y["right"]),(100,0,0),thickness=10,lineType=cv2.LINE_8,shift=0)
    cv2.line(img,(coordinates_x["right"],coordinates_y["right"]),(coordinates_x["left"],coordinates_y["left"]),(100,0,0),thickness=10,lineType=cv2.LINE_8,shift=0)
    cv2.line(img,(coordinates_x["left"],coordinates_y["left"]),(coordinates_x["top"],coordinates_y["top"]),(100,0,0),thickness=10,lineType=cv2.LINE_8,shift=0)

    cv2.imwrite("resultpre2.jpg",img)
    center_x = (top[0] + left[0] + right[0]) / 3 #コーンの重心のX座標を取得

    return center_x

center_x=detect_target("C:/Users/delic/Downloads/200cm (1).jpg")
print (center_x)
 