from PIL import Image
from PIL import ImageOps


class ImageEditor():
    def __init__(self, filename):
        self.filename = filename
        self.original = None
        self.changed = list()


    def open(self):
        try:
            self.original = Image.open(self.filename)
        except:
            print('Файл не найден!')
        self.original.show()


    def do_left(self):
        # Используем ImageOps для зеркального отражения
        flipped = ImageOps.mirror(self.original)
        self.changed.append(flipped)

        # Автоматический нейминг отредактированных картинок
        temp_filename = self.filename.split('.')
        new_filename = temp_filename[0] + str(len(self.changed)) + '.jpg'

        flipped.save(new_filename)


    # Бонус. обрезать детёныша коалы
    def do_cropped(self):
        box = (250, 100, 600, 400) #лево, верх, право, низ
        cropped = self.original.crop(box)
        self.changed.append(cropped)

        # Бонус. Автоматический нейминг отредактированных картинок
        temp_filename = self.filename.split('.')
        new_filename = temp_filename[0] + str(len(self.changed)) + '.jpg'

        cropped.save(new_filename)


MyImage = ImageEditor('original.jpg')
MyImage.open()

MyImage.do_left()
MyImage.do_cropped()

for im in MyImage.changed:
    im.show()
