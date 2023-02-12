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
3. If you wanna change the translated language, go to line 70 and change the following code:
```
response = openai.Completion.create(
    engine=model_engine,
    prompt="translate '" + text + "' to Bahasa",
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

```
to

```
response = openai.Completion.create(
    engine=model_engine,
    prompt="translate '" + text + "' to YOUR_LANGUAGE_CHOICE",
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)
```

# IMPORTANT

This app only support **_alphabet_** languange.
Such as _english_, _germany_, _italy_, **etc.**
Image extension that supported is _jpeg_, _jpg_, _png_

# Future Update

1. Symbolic languange **and/or** _right-to-left_ recognation & translation.
2. Enchanting image processing.
3. Many more...
