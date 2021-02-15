#!/usr/bin/python3
#from PIL import Image
import cv2
import numpy
import pytesseract
import requests
import argparse
from io import BytesIO

#m, e, h
parser = argparse.ArgumentParser("Dictionary creator for s0urce.io")
parser.add_argument("dict")
args = parser.parse_args()

custom_oem_psm = r'--psm 8'
folder = args.dict
url = 'http://s0urce.io/client/img/word/' + folder + '/'

r = requests.get(url + str(0))

i = 0
while r.status_code == 200:
	#print(i)
	try:
		r = requests.get(url + str(i), timeout=3)
	except requests.Timeout:
		#print(str(i) + " words counted, ")
		break
#		img = Image.open(BytesIO(r.content))
	stream = BytesIO(r.content)
	img_read = cv2.imdecode(numpy.fromstring(stream.read(), numpy.uint8), 1)
	#img_denoising = cv2.fastNlMeansDenoisingColored(img_read, None, 16,16,7,21)
	img_color = cv2.cvtColor(img_read, cv2.COLOR_BGR2GRAY)
	img_blur = cv2.GaussianBlur(img_color,(5,5),0)
	ret3,img = cv2.threshold(img_blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
	text = pytesseract.image_to_string(img, lang='eng', config=custom_oem_psm)
	print(text.rstrip())
	#cv2.imshow(str(i), img)
	#cv2.waitKey(0)
	#cv2.destroyAllWindows()
	i += 1
