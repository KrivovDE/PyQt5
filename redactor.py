from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenuBar, QMenu, \
    QFileDialog

import sys

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle('REDACTOR')
        self.setGeometry(300, 250, 350, 200)

        self.text_edit = QtWidgets.QTextEdit(self)
        self.setCentralWidget(self.text_edit)

        self.create_menu_bar()

    def create_menu_bar(self):
        self.menuBar = QMenuBar(self)
        self.setMenuBar(self.menuBar)

        self.fileMenu = QMenu('&ФАЙЛ', self)
        self.menuBar.addMenu(self.fileMenu)

        self.fileMenu.addAction('Открыть', self.action_clicked)
        self.fileMenu.addAction('Сохранить', self.action_clicked)

    @QtCore.pyqtSlot()
    def action_clicked(self):
        action = self.sender()

        if action.text() == 'Открыть':
            try:
                fname = QFileDialog.getOpenFileName(self)[0]
                f = open(fname, 'r')
                with f:
                    data = f.read()
                    self.text_edit.setText(data)
                    f.close()
            except FileNotFoundError:
                self.text_edit.setText('Выберите файл')

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
    import sys

    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())


