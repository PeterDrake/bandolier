# Adapted from https://doc.qt.io/qtforpython-6/gettingstarted.html#getting-started
import sys
import random
from PySide6 import QtCore, QtWidgets

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        # self.hello = ["Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]
        # self.button = QtWidgets.QPushButton("Click me!")
        # self.text = QtWidgets.QLabel("Hello World",
        #                              alignment=QtCore.Qt.AlignCenter)
        self.layout = QtWidgets.QVBoxLayout(self)
        for i in range(4):
            row = QtWidgets.QGroupBox() #outer containing box for each row
            layout = QtWidgets.QHBoxLayout(row)
            button = QtWidgets.QPushButton(f'Copy {i}')
            #button.sizePolicy().setVerticalPolicy(QtWidgets.QSizePolicy.Policy.Expanding)
            button.setSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Expanding)
            text = QtWidgets.QPlainTextEdit(f'Line {i}')  #labels for each line
            layout.addWidget(button)
            layout.addWidget(text)
            row.setLayout(layout)
            self.layout.addWidget(row)
        # self.layout.addWidget(self.text)
        # self.layout.addWidget(self.button)
            button.clicked.connect(self.magic)
        self.setWindowTitle('Bandolier')

    @QtCore.Slot()
    def magic(self):
        #self.text.setText(random.choice(self.hello))    #no longer needed
        print("Hey, I've been clicked")

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())
