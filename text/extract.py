from PIL import Image
import pytesseract

from config import config


pytesseract.pytesseract.tesseract_cmd = config['tesseract_path']


def extract_text(filename):
    im = Image.open(filename)
    text = pytesseract.image_to_string(im, config="--psm 6")
    return text
