import cv2

#Use bilateral filter for edge-aware smoothing.
num_down = 2 # number of downsampling steps
num_bilateral = 3 # number of bilateral filtering steps

img_rgb = cv2.imread("kohli.jpg")

# downsample image using Gaussian pyramid
img_color = img_rgb
for _ in range(num_down):
   img_color = cv2.pyrDown(img_color)

# repeatedly apply small bilateral filter instead of
# applying one large filter
for _ in range(num_bilateral):
   img_color = cv2.bilateralFilter(img_color, d=9, sigmaColor=4, sigmaSpace=5)

# upsample image to original size
for _ in range(num_down):
   img_color = cv2.pyrUp(img_color)


#Use median filter to reduce noise
# convert to grayscale and apply median blur
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
img_blur = cv2.medianBlur(img_gray, 11)


#Use adaptive thresholding to create an edge mask
# detect and enhance edges
img_edge = cv2.adaptiveThreshold(img_blur, 255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,blockSize=7,C=2)



# Combine color image with edge mask & display picture
# convert back to color, bit-AND with color image
img_edge = cv2.cvtColor(img_edge, cv2.COLOR_GRAY2RGB)
img_cartoon = cv2.bitwise_and(img_color, img_edge)

# display
cv2.imshow("myCartoon", img_cartoon)
cv2.imshow("sketch",img_edge)

cv2.imwrite('myCartoon.png',img_cartoon)  #add a copy
cv2.imwrite('mySketch.png',img_edge)

if cv2.waitKey(0) & 0xff == 27:  
    cv2.destroyAllWindows() 