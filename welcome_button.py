from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect, QSize, QTime,
                            QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                           QFontDatabase, QGradient, QIcon, QImage,
                           QKeySequence, QLinearGradient, QPainter, QPalette,
                           QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
                               QMenuBar, QPushButton, QSizePolicy, QStatusBar,
                               QVBoxLayout, QWidget)


import sys


class Ui_PySide6(object):

    def setupUi(self, PySide6):
        if not PySide6.objectName():
            PySide6.setObjectName(u"PySide6")
        PySide6.resize(583, 450)
        self.centralwidget = QWidget(PySide6)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.name_line_edit = QLineEdit(self.centralwidget)
        self.name_line_edit.setObjectName(u"name_line_edit")

        self.verticalLayout.addWidget(self.name_line_edit)

        self.bt_1 = QPushButton(self.centralwidget)
        self.bt_1.setObjectName(u"bt_1")

        self.verticalLayout.addWidget(self.bt_1)

        self.outpyt_hello_label = QLabel(self.centralwidget)
        self.outpyt_hello_label.setObjectName(u"outpyt_hello_label")
        self.outpyt_hello_label.setTextFormat(Qt.PlainText)
        self.outpyt_hello_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.outpyt_hello_label)

        PySide6.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(PySide6)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 583, 21))
        PySide6.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(PySide6)
        self.statusbar.setObjectName(u"statusbar")
        PySide6.setStatusBar(self.statusbar)

        self.retranslateUi(PySide6)

        QMetaObject.connectSlotsByName(PySide6)


    def retranslateUi(self, PySide6):
        PySide6.setWindowTitle(QCoreApplication.translate("PySide6", u"PySide6", None))
        self.label.setText(QCoreApplication.translate("PySide6", u"\u041d\u0430\u0437\u043e\u0432\u0438 \u0441\u0432\u043e\u0435 \u0438\u043c\u044f", None))
        self.bt_1.setText(QCoreApplication.translate("PySide6", u"\u041a\u041d\u041e\u041f\u041a\u0410", None))
        self.outpyt_hello_label.setText("")


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_PySide6()
        self.ui.setupUi(self)
        self.ui.bt_1.clicked.connect(self.hello)

    def hello(self):
        text = self.ui.name_line_edit.text()
        if text == '':
            text = 'oo'
        self.ui.outpyt_hello_label.setText(f'ПРИВЕТ - {text}!!!')


if __name__ == '__main__':

    app = QApplication()
    window = Window()
    window.show()
    sys.exit(app.exec_())




















