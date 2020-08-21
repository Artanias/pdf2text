import cv2
import os
from wand.image import Image as wi 
from pytesseract import image_to_string


if __name__ == '__main__':
	# Enter file name in filename
	pdf = wi(filename='EFzmgIkebhjsvm2gJxNLhECbf0idXMOu.pdf', resolution=200)
	pdfImage = pdf.convert('jpeg')
	text = ""
	for img in pdfImage.sequence:
		page = wi(image=img)
		page.save(filename="./Images/tmp.jpg")
		img2 = cv2.imread('./Images/tmp.jpg')
		text += " "
		text += image_to_string(img2, lang='rus')

	with open('text.txt', 'w') as f:
		f.write(text)
	os.remove('./Images/tmp.jpg')