import cv2
import numpy as np

# 이미지 불러오기
image_path = '1.bmp'
image = cv2.imread(image_path)

# 이미지 크기 조정 (새로운 크기 지정)
new_width = 400
new_height = int(image.shape[0] * (new_width / image.shape[1]))
resized_image = cv2.resize(image, (new_width, new_height))

# 그레이스케일로 변환
gray = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

# 이미지 히스토그램 평활화
equ = cv2.equalizeHist(gray)

# 가우시안 블러로 이미지 필터링
blurred = cv2.GaussianBlur(equ, (5, 5), 0)

# 이진화
_, binary = cv2.threshold(blurred, 127, 255, cv2.THRESH_BINARY_INV)

# 에지 검출 (Canny 사용)
edges = cv2.Canny(binary, 30, 70)

# 결과 이미지 출력
cv2.imshow('Resized Image', resized_image)
cv2.imshow('Gray Image', gray)
cv2.imshow('Histogram Equalized Image', equ)
cv2.imshow('Blurred Image', blurred)
cv2.imshow('Binary Image', binary)
cv2.imshow('Edges Image', edges)

cv2.waitKey(0)
