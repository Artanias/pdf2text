import cv2
import os
from parser import Parser
from wand.image import Image as wi
from pytesseract import image_to_string


class TesseractPDFParser(Parser):

    def __init__(self, name_upload_file_w_path,
                 name_json_res_w_path='temp.json'):
        # The variable path_to_document is hidden directly
        self.__name_upload_file_w_path = name_upload_file_w_path
        self.__name_json_res_w_path = name_json_res_w_path

    @property
    def path_to_document(self):
        return self.__name_upload_file_w_path

    @property
    def path_to_json_out(self):
        return self.__name_json_res_w_path

    def parse_document(self):
        pdf = wi(filename=self.path_to_document, resolution=250)
        pdfImage = pdf.convert('jpeg')
        text = ""
        for img in pdfImage.sequence:
            page = wi(image=img)
            page.save(filename="./tmp.jpg")
            img2 = cv2.imread('./tmp.jpg')
            text += " "
            text += image_to_string(img2, lang='rus')

        with open('text.txt', 'w') as f:
            f.write(text)
        os.remove('./tmp.jpg')


assert issubclass(TesseractPDFParser, Parser)
assert isinstance(TesseractPDFParser('None'), Parser)
