from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):    
    
    def __style__(self):
        with open('./style.qss', 'r') as f: style = f.read()
        return style
    
    def setupUi(self, Form):
        Form.setObjectName('Form')
        Form.resize(390, 530)
        
        Form.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        Form.setStyleSheet(self.__style__())

        self.fr_fondo = QtWidgets.QFrame(Form)
        self.fr_fondo.setGeometry(QtCore.QRect(10, 10, 370, 510))
        self.fr_fondo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr_fondo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_fondo.setObjectName('fr_fondo')

        self.lbl_ecuaciones = QtWidgets.QLabel(self.fr_fondo)
        self.lbl_ecuaciones.setGeometry(QtCore.QRect(10, 50, 350, 110))

        font = QtGui.QFont()
        font.setFamily('Arial')
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)

        self.lbl_ecuaciones.setFont(font)
        self.lbl_ecuaciones.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lbl_ecuaciones.setStyleSheet('')
        self.lbl_ecuaciones.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_ecuaciones.setObjectName('lbl_ecuaciones')

        self.btn_cerrar = QtWidgets.QPushButton(self.fr_fondo)
        self.btn_cerrar.setGeometry(QtCore.QRect(320, 20, 21, 21))
        self.btn_cerrar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_cerrar.setObjectName('btn_cerrar')
        self.btn_cerrar.setText('')

        self.btn_minimizar = QtWidgets.QPushButton(self.fr_fondo)
        self.btn_minimizar.setGeometry(QtCore.QRect(280, 20, 21, 21))
        self.btn_minimizar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_minimizar.setObjectName('btn_minimizar')
        self.btn_minimizar.setText('')

        self.lbl_title = QtWidgets.QLabel(self.fr_fondo)
        self.lbl_title.setGeometry(QtCore.QRect(20, 12, 251, 41))

        font = QtGui.QFont()
        font.setFamily('arial')
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)

        self.lbl_title.setFont(font)
        self.lbl_title.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_title.setObjectName('lbl_title')

        self.btn_opc1 = QtWidgets.QPushButton(self.fr_fondo)
        self.btn_opc1.setGeometry(QtCore.QRect(29, 160, 311, 55))
        self.btn_opc1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_opc1.setObjectName('btn_opc1')

        self.btn_opc2 = QtWidgets.QPushButton(self.fr_fondo)
        self.btn_opc2.setGeometry(QtCore.QRect(30, 230, 311, 55))
        self.btn_opc2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_opc2.setObjectName('btn_opc2')

        self.btn_opc3 = QtWidgets.QPushButton(self.fr_fondo)
        self.btn_opc3.setGeometry(QtCore.QRect(30, 300, 311, 55))
        self.btn_opc3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_opc3.setObjectName('btn_opc3')

        self.btn_opc4 = QtWidgets.QPushButton(self.fr_fondo)
        self.btn_opc4.setGeometry(QtCore.QRect(30, 370, 311, 55))
        self.btn_opc4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_opc4.setObjectName('btn_opc4')

        self.btn_continuar = QtWidgets.QPushButton(self.fr_fondo)
        self.btn_continuar.setGeometry(QtCore.QRect(60, 440, 251, 50))

        font = QtGui.QFont()
        font.setFamily('arial')
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)

        self.btn_continuar.setFont(font)
        self.btn_continuar.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.btn_continuar.setObjectName('btn_continuar')

        self.retranslateUi(Form)

        self.btn_cerrar.clicked.connect(Form.close)
        self.btn_minimizar.clicked.connect(Form.showMinimized)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate('Form', 'Math'))
        
        self.lbl_ecuaciones.setText(_translate('Form', 'x - 1y = 4x + 6y'))
        self.lbl_title.setText(_translate('Form', 'Resuelve'))
        
        self.btn_opc1.setText(_translate('Form', 'x=10'))
        self.btn_opc2.setText(_translate('Form', 'x=20'))
        self.btn_opc3.setText(_translate('Form', 'x=30'))
        self.btn_opc4.setText(_translate('Form', 'x=40'))
        
        self.btn_continuar.setText(_translate('Form', 'Comprueba'))

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

#* Author: Francisco Velez
