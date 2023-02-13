import errno
import cv2
import openai
import pytesseract
import numpy as np
import tkinter as tk
import os
import shutil
import re

def detect_image_lang(img_path):
    try:
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        osd = pytesseract.image_to_osd(img_path)
        script = re.search("Script: ([a-zA-Z]+)\n", osd).group(1)
        conf = re.search("Script confidence: (\d+\.?(\d+)?)", osd).group(1)
        return script, float(conf)
    except Exception as e:
        return None, 0.0

script_name, confidence = detect_image_lang("text-japanese.png")
