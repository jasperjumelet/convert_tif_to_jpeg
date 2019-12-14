from PIL import Image
from os import listdir

images_train = [x for x in listdir('trainconv')]
for image in images_train:
	im = Image.open("trainconv/" + image)
	im.save("train/" + image[:-4] + ".jpeg")

images_test = [x for x in listdir('testconv')]
for image in images_test:
	im = Image.open("testconv/" + image)
	im.save("test/" + image[:-4]) + ".jpeg"
