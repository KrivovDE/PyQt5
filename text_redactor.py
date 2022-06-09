from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenuBar, QMenu, QFileDialog

import sys


class Window(QMainWindow):

    def __init__(self):
        super(Window, self).__init__()

        # создание сомого окна
        self.setWindowTitle('REDACTOR')
        self.setGeometry(300, 250, 350, 200)

        # создание поля для отображения текста
        self.text_edit = QtWidgets.QTextEdit(self)
        self.setCentralWidget(self.text_edit)

        # создание меню
        self.create_menu_bar()

    def create_menu_bar(self):

        # создаем глобальный объект меню
        self.menu_bar = QMenuBar(self)
        self.setMenuBar(self.menu_bar)

        # создаем pfrkflreменю
        self.file_menu = QMenu('ФАЙЛ', self)
        self.menu_bar.addMenu(self.file_menu)

        # создаем объекты внутри меню
        self.file_menu.addAction('Открыть', self.action_clicked)
        self.file_menu.addAction('Сохранить', self.action_clicked)

    @QtCore.pyqtSlot() # обрабатывает нажитие на различные пункты меню
    def action_clicked(self):

        # self.sender() - педоставляет всю информацию об объекте на который нажали
        action = self.sender()

        if action.text() == 'Открыть':

            # Открываем файл
            try:
                fname = QFileDialog.getOpenFileName(self)[0]
                f = open(fname, 'r')
                with f:
                    data = f.read()
                    self.text_edit.setText(data)
                    f.close()
            except FileNotFoundError:
                self.text_edit.setText('Выберите файл')

        # Закрываем файл
        elif action.text() == 'Сохранить':
            try:
                fname = QFileDialog.getSaveFileName(self)[0]
                f = open(fname, 'w')
                text = self.text_edit.toPlainText()
                f.write(text)
                f.close()
            except FileNotFoundError:
                self.text_edit.setText('Выберите файл')


if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())


