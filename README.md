# Image-to-text translate using Tesseract & OpenAI API
This project is using : 
- **Open AI _API_** to translate text
- **Tesseract-OCR** to collect text from image
- **Opencv** to enchanting image processing

# HOW TO INSTALL

1. After cloning this project go to this project directory
2. Create constant.py
3. Inside constant.py write
> api_key = 'YOUR-OPENAI-API-KEY'
4. [install tesseract-ocr](https://tesseract-ocr.github.io/tessdoc/Installation.html)
5. open terminal ( cmd in windows )
 
```
pip install pytesseract
pip install opencv-python
pip install openai
```

# HOW TO USE
1. Save your image at the root folder of this project.
2. At _translate.py_ change the string inside gambar var to your saved image.
> gambar = 'YOUR_IMAGE_NAME.YOUR_IMAGE_EXTENSION'

# IMPORTANT

This app only support **_alphabet_** languange.
Such as _english_, _germany_, _italy_, **etc.**
Image extension that supported is _jpeg_, _jpg_, _png_

# Future Update

1. Symbolic languange **and/or** _right-to-left_ recognation & translation.
2. Enchanting image processing.
3. Many more...
