import sys
from PySide6 import QtWidgets
import pyperclip

class Bandolier(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QtWidgets.QVBoxLayout(self)
        for i in range(6):
            row = QtWidgets.QGroupBox() #outer containing box for each row
            layout = QtWidgets.QHBoxLayout(row)
            button = QtWidgets.QPushButton(f'Copy')
            button.setSizePolicy(QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Expanding)
            text = QtWidgets.QTextEdit(f'')  #labels for each line
            layout.addWidget(button)
            layout.addWidget(text)
            row.setLayout(layout)
            self.layout.addWidget(row)
            button.clicked.connect(Bandolier.make_command(text))
        self.setWindowTitle('Bandolier')

    @staticmethod
    def make_command(text):
        return lambda : pyperclip.copy(text.toPlainText())


# From https://doc.qt.io/qtforpython-6/gettingstarted.html#getting-started
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = Bandolier()
    widget.resize(800, 600)
    widget.show()
    sys.exit(app.exec())
