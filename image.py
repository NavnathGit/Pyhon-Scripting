from PIL import Image
img = Image.open('./Nav.JPG')
img.thumbnail((400, 200))
img.save('Nav2.jpg')

# png iamges are better to work with in web development
