from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

import sys


class Window(QMainWindow):

    def __init__(self):
        super(Window, self).__init__()

        # создание самого окна
        self.setWindowTitle('CLIC')
        self.setGeometry(300, 250, 500, 200)

        # создает поле для вывода текста - new_text "Надпись которая ..."
        self.new_text = QtWidgets.QLabel(self)

        # создает поле для вывода текста и указывает ее параметры
        self.main_text = QtWidgets.QLabel(self)
        self.main_text.setText('БАЗОВАЯ НАДПИСЬ')
        self.main_text.move(100, 100)
        self.main_text.adjustSize()

        # создает кнопку и указывает ее параметры
        self.btn = QtWidgets.QPushButton(self)
        self.btn.move(70, 150)
        self.btn.setText('КНОПКА')
        self.btn.setFixedWidth(200)
        # привязывает нажатие на кнопку к методу add_label
        self.btn.clicked.connect(self.add_label)

    # метод, в котором указан текст new_text, его размер
    def add_label(self):
        self.new_text.setText('Надпись которая показывается после нажания кнопки')
        self.new_text.move(100, 50)
        self.new_text.adjustSize()


if __name__ == '__main__':

    # sys.argv - дает сведения относительно системы на которой будет
    # запускаться программа. Отвечает за создание приложения в целом.
    app = QApplication(sys.argv)

    #объект который хранит определенное окно.(В этом случае одно)
    window = Window()

    #show - отображает выщесозданное окно.
    window.show()

    # указывает на параметры, корректоного выхода из приложения
    sys.exit(app.exec_())
