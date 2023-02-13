import cv2
import openai
import pytesseract
import numpy as np
import tkinter as tk
import os
import shutil
import constant

from PIL import Image, ImageTk

# This is made by N0iire at https://github.com/N0iire/Image-to-text-Translate


gambar = 'text-germany.png'

folder_name = 'temp'

# Menghapus file didalam folder temp
if not os.path.exists(folder_name):
    # Membuat folder jika folder belum ada
    os.makedirs(folder_name)
else:
    # Menghapus folder beserta isinya jika folder sudah ada
    shutil.rmtree(folder_name)
    os.makedirs(folder_name)


# Load gambar
img = cv2.imread(gambar)

# Rescale gambar
width = 350
height = 250
dim = (width, height)
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

# Menyimpan gambar hasl resize
cv2.imwrite('temp\img-resized.jpg', resized)

# Masukkan OpenAI Key anda

openai.api_key = constant.api_key

# Konversi gambar ke grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Otsu threshold untuk menghilangkan background
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Loop melalui setiap contour
for contour in contours:
    # Menentukan lokasi dan ukuran objek
    x, y, w, h = cv2.boundingRect(contour)
    
    # Gambar rectangel pada objek yang terdeteksi
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Menyimpan hasil segmentasi
cv2.imwrite('temp\contour.jpg', img)

# Konfigurasi tesseract
config = "eng"

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Ekstraksi teks dari gambar
text = pytesseract.image_to_string(thresh)

model_engine = "text-davinci-003"
response = openai.Completion.create(
    engine=model_engine,
    prompt="translate '" + text + "' to Bahasa", #Change to your prefered language
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

# Mendapatkan hasil terjemahan
translation = response["choices"][0]["text"].strip()


# Tampilkan hasil deteksi
root = tk.Tk()


# Gambar asli
img_asli = Image.open('temp\img-resized.jpg')

img_1 = ImageTk.PhotoImage(img_asli)

# Gambar Segmentasi
contour = cv2.imread('temp\contour.jpg')

resized_contour = cv2.resize(contour, dim, interpolation = cv2.INTER_AREA)

cv2.imwrite('temp\contour-resized.jpg', resized_contour)

img_contour = Image.open('temp\contour-resized.jpg')

img_2 = ImageTk.PhotoImage(img_contour)

# GUI

root.title("Deteksi dan Terjemahan")

# Tampilkan gambar asli
image_origin = tk.Label(root, image=img_1)

image_origin.grid(row=0, column=0)

# Tampilkan gambar segmentasi
image_segmen = tk.Label(root, image=img_2)


image_segmen.grid(row=0, column=1)

# Tampilkan text yang terdeteksi
label_text_detected = tk.Label(root, text="Detected Text : \n" + text)

label_text_detected.grid(row=1, column=0)

# Mendefinisikan ukuran font dan ukuran window
font_size = 10
window_width = 800

# Mendapatkan jumlah karakter yang dapat ditampilkan pada satu baris
characters_per_line = window_width // font_size

# Membagi teks menjadi beberapa baris
text_lines = [translation[i:i+characters_per_line] for i in range(0, len(translation), characters_per_line)]

# Menampilkan teks dengan tkinter
label_text_translate = tk.Label(root, text="Translated Text : \n" + "\n".join(text_lines), font=("Helvetica", font_size))
label_text_translate.grid(row=1, column=1)

# Run GUI
root.mainloop()