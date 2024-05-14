import numpy as np
import cv2 as cv
from time import sleep
from matplotlib import pyplot as plt


imagem = cv.imread("papagaio4.jpg")

#imagem = cv.cvtColor(imagem, cv.COLOR_BAYER_BG2BGR)


plt.imshow(imagem)
plt.show()
