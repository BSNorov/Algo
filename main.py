import os
from PyQt5.QtWidgets import (
    QApplication, QWidget,
    QFileDialog,
    QLabel, QPushButton, QListWidget,
    QHBoxLayout, QVBoxLayout
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

from PIL import Image
from PIL import ImageFilter
from PIL.ImageFilter import SHARPEN


app = QApplication([])

win = QWidget()
win.resize(700, 500)
win.setWindowTitle('Easy Editor')

lb_image = QLabel("Картинка")
lb_image.setAlignment(Qt.AlignCenter)

btn_dir = QPushButton("Папка")
lw_files = QListWidget()

btn_left = QPushButton("Лево")
btn_right = QPushButton("Право")
btn_flip = QPushButton("Зеркало")
btn_sharp = QPushButton("Резкость")
btn_bw = QPushButton("Ч/Б")
btn_reset = QPushButton("Сброс фильтров")


row = QHBoxLayout()
col1 = QVBoxLayout()
col2 = QVBoxLayout()

col1.addWidget(btn_dir)
col1.addWidget(lw_files)

col2.addWidget(lb_image, 95)

row_tools = QHBoxLayout()
row_tools.addWidget(btn_left)
row_tools.addWidget(btn_right)
row_tools.addWidget(btn_flip)
row_tools.addWidget(btn_sharp)
row_tools.addWidget(btn_bw)
row_tools.addWidget(btn_reset)

col2.addLayout(row_tools)

row.addLayout(col1, 20)
row.addLayout(col2, 80)

win.setLayout(row)

workdir = ''


def filter(files, extensions):
    result = []

    for filename in files:
        for ext in extensions:
            if filename.lower().endswith(ext):
                result.append(filename)
                break

    return result


def chooseWorkdir():
    global workdir

    directory = QFileDialog.getExistingDirectory(
        win,
        "Выберите папку",
        workdir if workdir else os.getcwd()
    )

    if directory:
        workdir = directory
        return True

    return False


def showFilenamesList():
    extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']

    if not chooseWorkdir():
        return

    filenames = filter(os.listdir(workdir), extensions)
    filenames.sort()

    lw_files.clear()
    lb_image.clear()
    lb_image.setText("Картинка")

    workimage.image = None
    workimage.original_image = None
    workimage.filename = None

    for filename in filenames:
        if os.path.isfile(os.path.join(workdir, filename)):
            lw_files.addItem(filename)


class ImageProcessor:
    def __init__(self):
        self.image = None
        self.dir = None
        self.filename = None
        self.save_dir = "Modified"
        self.original_image = None

    def loadImage(self, filename):
        """Загружает изображение и сохраняет его оригинал."""

        self.filename = filename
        fullname = os.path.join(workdir, filename)

        try:
            with Image.open(fullname) as img:
                self.image = img.copy()
                self.original_image = img.copy()

        except (OSError, ValueError) as error:
            print(f"Ошибка загрузки изображения: {error}")

            self.image = None
            self.original_image = None
            self.filename = None

    def saveImage(self):
        """Сохраняет изменённое изображение в подпапку Modified."""

        if self.image is None or self.filename is None:
            return None

        path = os.path.join(workdir, self.save_dir)
        os.makedirs(path, exist_ok=True)

        fullname = os.path.join(path, self.filename)

        try:
            image_to_save = self.image.copy()

            if image_to_save.mode not in ("RGB", "L", "RGBA"):
                image_to_save = image_to_save.convert("RGB")

            if self.filename.lower().endswith((".jpg", ".jpeg")):
                if image_to_save.mode != "RGB":
                    image_to_save = image_to_save.convert("RGB")

            image_to_save.save(fullname)
            return fullname

        except (OSError, ValueError) as error:
            print(f"Ошибка сохранения изображения: {error}")
            return None

    def updateImage(self):
        """Сохраняет и отображает изменённое изображение."""

        if self.image is None:
            return

        image_path = self.saveImage()

        if image_path:
            self.showImage(image_path)

    def do_bw(self):
        if self.image is None:
            return

        self.image = self.image.convert("L")
        self.updateImage()

    def do_left(self):
        if self.image is None:
            return

        self.image = self.image.transpose(Image.Transpose.ROTATE_90)
        self.updateImage()

    def do_right(self):
        if self.image is None:
            return

        self.image = self.image.transpose(Image.Transpose.ROTATE_270)
        self.updateImage()

    def do_flip(self):
        if self.image is None:
            return

        self.image = self.image.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
        self.updateImage()

    def do_sharpen(self):
        if self.image is None:
            return

        self.image = self.image.filter(SHARPEN)
        self.updateImage()

    def showImage(self, path):
        """Отображает изображение с сохранением пропорций."""

        if not os.path.exists(path):
            return

        pixmapimage = QPixmap(path)

        if pixmapimage.isNull():
            return

        w = lb_image.width()
        h = lb_image.height()

        pixmapimage = pixmapimage.scaled(
            w,
            h,
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )

        lb_image.setPixmap(pixmapimage)

    def resetImage(self):
        """Сбрасывает все изменения и возвращает оригинал."""

        if self.original_image is None:
            return

        self.image = self.original_image.copy()

        original_path = os.path.join(workdir, self.filename)
        self.showImage(original_path)

        modified_path = os.path.join(
            workdir,
            self.save_dir,
            self.filename
        )

        if os.path.isfile(modified_path):
            try:
                os.remove(modified_path)
            except OSError as error:
                print(f"Ошибка удаления изменённого файла: {error}")


def showChosenImage():
    if lw_files.currentRow() < 0:
        return

    filename = lw_files.currentItem().text()

    workimage.loadImage(filename)

    if workimage.image is not None:
        image_path = os.path.join(workdir, filename)
        workimage.showImage(image_path)


workimage = ImageProcessor()

btn_dir.clicked.connect(showFilenamesList)

lw_files.currentRowChanged.connect(showChosenImage)

btn_bw.clicked.connect(workimage.do_bw)
btn_left.clicked.connect(workimage.do_left)
btn_right.clicked.connect(workimage.do_right)
btn_sharp.clicked.connect(workimage.do_sharpen)
btn_flip.clicked.connect(workimage.do_flip)
btn_reset.clicked.connect(workimage.resetImage)

win.show()

app.exec()
