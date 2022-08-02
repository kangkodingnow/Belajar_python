
from PIL import Image

im = Image.open("51. Mengunakan dan Install Eksternal Package dengan pip/farhan.jpeg")

print("format file:" + im.format)
print("ukuran file:" + str(im.size))
print("mode file:" + im.mode)

im.show()