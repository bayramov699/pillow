from PIL import Image
import urllib.request



content = {
    'welcome' : 'Welcome, with this program you can change your photos: ',
    'img_input' : 'Please, enter an image url or path: ',
    'change' : 'What do you want to change?: ',
    'methods' : 'choose 1 for show, 2 for resize, 3 for convert, 4 for rotate'
}

class ChangeImage:

    def __init__(self, image_data):
        self.image_data = image_data

    def show_img(self):
        img = Image.open(self.image_data)
        print("Please, wait. I`ll show you your image")
        img.show()

    def resize_img(self, width, height):
        self.width = width
        self.height = height
        img = Image.open(self.image_data)
        resized_img = img.resize((width, height))
        resized_img.save('resized.jpg')
        print(f'Your image new size is {resized_img.size} and save to your main folder.')

    def convert_img(self, mode):
        self.mode = mode
        img = Image.open(self.image_data)
        converted_img = img.convert(mode=self.mode)
        converted_img.save('converted_img.jpg')
        print('Your image converted and save as converted_img.jpg to your main folder')

    def rotate_img(self, degree):
        self.degree = degree
        img = Image.open(self.image_data)
        rotated_img = img.rotate(self.degree)
        rotated_img.save('rotated_img.jpg')
        print('Your image rotated and save as rotated_img.jpg to your main folder')


print(content['welcome'])
print(content['img_input'])
img_input = input()

img_data = img_input.replace(" ", "")
# print(img_data)
if img_data[:4] == "http":
    urllib.request.urlretrieve(img_data, "sample.jpg")

    img = ChangeImage("sample.jpg")
else:
    img = ChangeImage(img_data)


print(content['change'])
print(content['methods'])
method = input('Choose method: ')

if method == '1':
    img.show_img()

elif method == '2':
    width = int(input('Please, enter new width: '))
    height = int(input('Please, enter new height: '))
    img.resize_img(width, height)

elif method == '3':
    mode = input('Please, enter new mode: (for example: L, LA, 1):')
    img.convert_img(mode)

elif method == '4':
    degree = int(input('Please, enter new degree: '))
    img.rotate_img(degree)

    