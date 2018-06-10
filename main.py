import sys

from PyQt5.QtWidgets import QApplication
import numpy as np
from napari.gui.image_widget import ImageWidget
from vispy import app, gloo, visuals, scene
app.use_app('pyqt5')

if __name__ == '__main__':

    # create an image
    h = 512
    w = 512
    Y, X = np.ogrid[-2.5:2.5:h * 1j, -2.5:2.5:w * 1j]
    image = np.empty((h, w), dtype=np.float32)
    image[:] = np.exp(- X ** 2 - Y ** 2)  # * (1. + .5*(np.random.rand(h, w)-.5))
    image[-30:] = np.linspace(0, 1, w)

    # starting
    application = QApplication(sys.argv)

    # opening an image widget for theb image:
    imgdis = ImageWidget(image, window_width=512, window_height=512)
    imgdis.show()


    sys.exit(application.exec_())