Work on Linux Ubuntu 18.04 with RU text in pdf

## Requerements

wand

cv2

pytesseract

Для распозвания русского текста:

sudo apt-get install tesseract-ocr-rus

Что бы был доступ к чтению и записи pdf с помощью библиотеки wand

/etc/ImageMgick-6/policy.xml

<plicy domain='coder' rights='read|write' pattern='PDF' />
