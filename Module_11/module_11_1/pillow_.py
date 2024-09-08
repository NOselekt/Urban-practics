from PIL import Image

image = Image.open('0.png')
image = image.resize((1920, 1080))
image = image.convert('L')
image.save('1.png')