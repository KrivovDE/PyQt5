from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

import sys


# class Ui_MainWindow - сформирован при помощи QT Designer
class UiMainWindow(object):

    # метод является по сути, чем то вроде конструктора
    def setup_ui(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(400, 500)

        # создание самого окна
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_result = QtWidgets.QLabel(self.centralwidget)
        self.label_result.setGeometry(QtCore.QRect(0, 0, 400, 100))

        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)

        # создание поля ввода и вывода результатов
        self.label_result.setFont(font)
        self.label_result.setStyleSheet(
            "background-color: rgb(103, 103, 103);\n"
            "color: rgb(255, 255, 255);")
        self.label_result.setObjectName("label_result")

        # создание кнопки 7
        self.bt_7 = QtWidgets.QPushButton(self.centralwidget)
        self.bt_7.setGeometry(QtCore.QRect(0, 100, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.bt_7.setFont(font)
        self.bt_7.setStyleSheet("background-color: rgb(108, 255, 64);")
        self.bt_7.setObjectName("bt_7")

        # создание кнопки 8
        self.bt_8 = QtWidgets.QPushButton(self.centralwidget)
        self.bt_8.setGeometry(QtCore.QRect(100, 100, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.bt_8.setFont(font)
        self.bt_8.setStyleSheet("background-color: rgb(108, 255, 64);")
        self.bt_8.setObjectName("bt_8")

        # создание кнопки 9
        self.bt_9 = QtWidgets.QPushButton(self.centralwidget)
        self.bt_9.setGeometry(QtCore.QRect(200, 100, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.bt_9.setFont(font)
        self.bt_9.setStyleSheet("background-color: rgb(108, 255, 64);")
        self.bt_9.setObjectName("bt_9")

        # создание кнопки +
        self.bt_add = QtWidgets.QPushButton(self.centralwidget)
        self.bt_add.setGeometry(QtCore.QRect(300, 100, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.bt_add.setFont(font)
        self.bt_add.setStyleSheet("background-color: rgb(185, 237, 255);")
        self.bt_add.setObjectName("bt_add")

        # создание кнопки -
        self.bt_sub = QtWidgets.QPushButton(self.centralwidget)
        self.bt_sub.setGeometry(QtCore.QRect(300, 200, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.bt_sub.setFont(font)
        self.bt_sub.setStyleSheet("background-color: rgb(185, 237, 255);")
        self.bt_sub.setObjectName("bt_sub")

        # создание кнопки 6
        self.bt_6 = QtWidgets.QPushButton(self.centralwidget)
        self.bt_6.setGeometry(QtCore.QRect(200, 200, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.bt_6.setFont(font)
        self.bt_6.setStyleSheet("background-color: rgb(108, 255, 64);")
        self.bt_6.setObjectName("bt_6")

        # создание кнопки 4
        self.bt_4 = QtWidgets.QPushButton(self.centralwidget)
        self.bt_4.setGeometry(QtCore.QRect(0, 200, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.bt_4.setFont(font)
        self.bt_4.setStyleSheet("background-color: rgb(108, 255, 64);")
        self.bt_4.setObjectName("bt_4")

        # создание кнопки 5
        self.bt_5 = QtWidgets.QPushButton(self.centralwidget)
        self.bt_5.setGeometry(QtCore.QRect(100, 200, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.bt_5.setFont(font)
        self.bt_5.setStyleSheet("background-color: rgb(108, 255, 64);")
        self.bt_5.setObjectName("bt_5")

        # создание кнопки *
        self.bt_mul = QtWidgets.QPushButton(self.centralwidget)
        self.bt_mul.setGeometry(QtCore.QRect(300, 300, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.bt_mul.setFont(font)
        self.bt_mul.setStyleSheet("background-color: rgb(185, 237, 255);")
        self.bt_mul.setObjectName("bt_mul")

        # создание кнопки 1
        self.bt_1 = QtWidgets.QPushButton(self.centralwidget)
        self.bt_1.setGeometry(QtCore.QRect(0, 300, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.bt_1.setFont(font)
        self.bt_1.setStyleSheet("background-color: rgb(108, 255, 64);")
        self.bt_1.setObjectName("bt_1")

        # создание кнопки 2
        self.bt_2 = QtWidgets.QPushButton(self.centralwidget)
        self.bt_2.setGeometry(QtCore.QRect(100, 300, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.bt_2.setFont(font)
        self.bt_2.setStyleSheet("background-color: rgb(108, 255, 64);")
        self.bt_2.setObjectName("bt_2")

        # создание кнопки 3
        self.bt_3 = QtWidgets.QPushButton(self.centralwidget)
        self.bt_3.setGeometry(QtCore.QRect(200, 300, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.bt_3.setFont(font)
        self.bt_3.setStyleSheet("background-color: rgb(108, 255, 64);")
        self.bt_3.setObjectName("bt_3")

        # создание кнопки 0
        self.bt_0 = QtWidgets.QPushButton(self.centralwidget)
        self.bt_0.setGeometry(QtCore.QRect(0, 400, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.bt_0.setFont(font)
        self.bt_0.setStyleSheet("background-color: rgb(108, 255, 64);")
        self.bt_0.setObjectName("bt_0")

        # создание кнопки /
        self.bt_truediv = QtWidgets.QPushButton(self.centralwidget)
        self.bt_truediv.setGeometry(QtCore.QRect(300, 400, 100, 100))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.bt_truediv.setFont(font)
        self.bt_truediv.setStyleSheet("background-color: rgb(185, 237, 255);")
        self.bt_truediv.setObjectName("bt_truediv")

        # создание кнопки =
        self.bt_eq = QtWidgets.QPushButton(self.centralwidget)
        self.bt_eq.setGeometry(QtCore.QRect(100, 400, 200, 100))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.bt_eq.setFont(font)
        self.bt_eq.setStyleSheet("background-color: rgb(108, 255, 64);\n"
                                 "background-color: rgb(255, 103, 65);")
        self.bt_eq.setObjectName("bt_eq")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslate_ui(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # add_functions - добавляет различные обработчики событий к кнопкам
        self.add_functions()

        # чтобы после получения результата можно было выполнить слующую операцию
        # в теле функций меняется значение с False на True
        self.is_eq = False

    def retranslate_ui(self, MainWindow):

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Калькулятор"))
        self.label_result.setText(_translate("MainWindow", "0"))
        self.bt_7.setText(_translate("MainWindow", "7"))
        self.bt_8.setText(_translate("MainWindow", "8"))
        self.bt_9.setText(_translate("MainWindow", "9"))
        self.bt_add.setText(_translate("MainWindow", "+"))
        self.bt_sub.setText(_translate("MainWindow", "-"))
        self.bt_6.setText(_translate("MainWindow", "6"))
        self.bt_4.setText(_translate("MainWindow", "4"))
        self.bt_5.setText(_translate("MainWindow", "5"))
        self.bt_mul.setText(_translate("MainWindow", "*"))
        self.bt_1.setText(_translate("MainWindow", "1"))
        self.bt_2.setText(_translate("MainWindow", "2"))
        self.bt_3.setText(_translate("MainWindow", "3"))
        self.bt_0.setText(_translate("MainWindow", "0"))
        self.bt_truediv.setText(_translate("MainWindow", "/"))
        self.bt_eq.setText(_translate("MainWindow", "="))

    # при нажатии на кнопку (clicked.connect) через lambda вызываем метод
    #write_number, который принимает как аргумент text этой кнопки
    def add_functions(self):

        self.bt_0.clicked.connect(lambda: self.write_number(self.bt_0.text()))
        self.bt_1.clicked.connect(lambda: self.write_number(self.bt_1.text()))
        self.bt_2.clicked.connect(lambda: self.write_number(self.bt_2.text()))
        self.bt_3.clicked.connect(lambda: self.write_number(self.bt_3.text()))
        self.bt_4.clicked.connect(lambda: self.write_number(self.bt_4.text()))
        self.bt_5.clicked.connect(lambda: self.write_number(self.bt_5.text()))
        self.bt_6.clicked.connect(lambda: self.write_number(self.bt_6.text()))
        self.bt_7.clicked.connect(lambda: self.write_number(self.bt_7.text()))
        self.bt_8.clicked.connect(lambda: self.write_number(self.bt_8.text()))
        self.bt_9.clicked.connect(lambda: self.write_number(self.bt_9.text()))
        self.bt_add.clicked.connect(
            lambda: self.write_number(self.bt_add.text()))
        self.bt_sub.clicked.connect(
            lambda: self.write_number(self.bt_sub.text()))
        self.bt_mul.clicked.connect(
            lambda: self.write_number(self.bt_mul.text()))
        self.bt_truediv.clicked.connect(
            lambda: self.write_number(self.bt_truediv.text()))
        self.bt_eq.clicked.connect(self.results)

    def write_number(self, number):

        # поверяем если в label_result - 0 или предыдущий результат,
        # заполняем label_result аргументом  number из write_number
        if self.label_result.text() == '0' or self.is_eq:
            self.label_result.setText(number)
            self.is_eq = False

        # выводим на label_result то, что там уже есть и принимаемый
        # write_number аргумент (number)
        # Работа происходит со строковыми объектами.
        else:
            self.label_result.setText(self.label_result.text() + number)

    # производство математических действий
    def results(self):

        # если is_eq - не Folse - то есть знак = еще не нажимался, то ..
        if not self.is_eq:
            try:
                # eval - производит математические операциии со str-объектами
                res = eval(self.label_result.text())
                self.label_result.setText(f'{self.label_result.text()} = {str(res)}')
                self.is_eq = True

            # обработка именно математических ошибок пользователя
            # и уведомление его об этом, через новое окно
            except Exception:
                error = QMessageBox()
                error.setWindowTitle('ZeroDivisionError')
                error.setText('Это недопустимо"')
                error.setIcon(QMessageBox.Warning)
                error.setStandardButtons(QMessageBox.Ok)
                error.exec_()
                self.is_eq = True

        # обработка прочих ошибок пользователя
        # и уведомление его об этом, через новое окно
        else:
            error = QMessageBox()
            error.setWindowTitle('Ошибка')
            error.setText('Сейчас это действие выполнить нельзя')
            error.setIcon(QMessageBox.Warning)
            error.setStandardButtons(QMessageBox.Ok)
            error.exec_()


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = UiMainWindow()
    ui.setup_ui(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
