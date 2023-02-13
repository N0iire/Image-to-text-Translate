# Image-to-text translate using Tesseract & OpenAI API
This project is using : 
- **Open AI _API_** to translate text
- **Tesseract-OCR** to collect text from image
- **Opencv** to enchanting image processing

# Requirement

From [pytesseract](https://pypi.org/project/pytesseract/)
<br>
- Python-tesseract requires Python 3.6+
- You will need the Python Imaging Library (PIL) (or the Pillow fork). Under Debian/Ubuntu, this is the package python-imaging or python3-imaging.
- Install [Google Tesseract-OCR](https://github.com/tesseract-ocr/tesseract) (additional info how to install the engine on Linux, Mac OSX and Windows). You must be able to invoke the tesseract command as tesseract. If this isn’t the case, for example because tesseract isn’t in your PATH, you will have to change the “tesseract_cmd” variable `pytesseract.pytesseract.tesseract_cmd`. Under Debian/Ubuntu you can use the package tesseract-ocr. For Mac OS users. please install homebrew package tesseract.
- More information is on the [pytesseract](https://pypi.org/project/pytesseract/) documentation.
- OPEN AI API [Key](https://platform.openai.com/docs/api-reference/introduction) 

# HOW TO INSTALL

1. After cloning this project go to the project directory
2. Create constant.py
3. Inside constant.py write
> api_key = 'YOUR-OPENAI-API-KEY'
4. open terminal ( cmd in windows )
 
```
pip install pytesseract
pip install pillow
pip install tk
pip install opencv-python
pip install openai
```

## If issues appear this may help you
`pip install --upgrade pip`

# HOW TO USE

1. Save your image at the root folder of this project.
> example : " C:\Image-to-text-Translate\ "
2. At _translate.py_ change the value inside `gambar` variable to your image name and extention.
> gambar = 'YOUR_IMAGE_NAME.YOUR_IMAGE_EXTENSION' (**_example_**) : `gambar = myimage.png`
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
<br>Such as _english_, _germany_, _italy_, **etc.**
<br>Image extension that supported is _jpeg_, _jpg_, _png_

# Future Update

1. Symbolic languange **and/or** _right-to-left_ recognation & translation.
2. Enchanting image processing.
3. Many more...

# License & How to Contribute
### This project is open for everyone who want to use, feel free to use it.
<br>
But if you can, please don't delete my github username in the `translate.py` file. Thanks!
