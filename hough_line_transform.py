import cv2
import numpy as np

img = cv2.imread('VR.png')

# グレースケールに変換
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# ぼかし処理
gray = cv2.blur(gray, (5, 5))

# エッジ検出を用いて二値化
edges = cv2.Canny(gray, 130, 200, apertureSize = 3)
# ハフ変換で直線を検出
lines = cv2.HoughLines(edges, 0.1, np.pi/180, 300)

# 検出した直線毎にループ
for line in lines:
    # 原点から直線までの距離と直線の法線横軸のなす角度を取得
    rho, theta = line[0]
    # 検出した直線を描画するために、結ぶ２点を計算
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * rho
    y0 = b * rho
    x1 = int(x0 + 1000*(-b))
    y1 = int(y0 + 1000*(a))
    x2 = int(x0 - 1000*(-b))
    y2 = int(y0 - 1000*(a))

    #検出した直線を描画
    cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

cv2.imwrite('houghlines.png', img)