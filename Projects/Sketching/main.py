import cv2

image=cv2.imread("19.jpg")
cv2.imshow("Image",image)
cv2.waitKey(0)

gray_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("New",gray_image)
cv2.waitKey(0)

inverted_image=255-gray_image
cv2.imshow("Inverted",inverted_image)
cv2.waitKey(0)
blurred=cv2.GaussianBlur(inverted_image,(21,21),0)
''
inverted_blurred=255-blurred
pencil_sketch=cv2.divide(gray_image,inverted_blurred,scale=256.0)
cv2.imshow('Sketch',pencil_sketch)
cv2.waitKey(0)

cv2.imshow('Original Image',image)
cv2.imshow('Pencil Sketch',pencil_sketch)
cv2.waitKey(0)

