from functions_ import Obtener_ecuacion, Obtener_numeros
from Ui_Math import Ui_Form, QtWidgets, QtCore, QtGui
import sys

class MainApp(QtWidgets.QMainWindow): 

    def __init__(self, parent=None, *args): 
        super(MainApp, self).__init__(parent=parent) 

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.newForm()
        self.ui.btn_continuar.clicked.connect(self.func_continuar)

        #* Mover ventana
        self.ui.fr_fondo.mouseMoveEvent = self.mover_ventana
	  
    ##* mover ventana
    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()

    def mover_ventana(self, event):
        try:
            if self.isMaximized() == False: 
                if event.buttons() == QtCore.Qt.LeftButton:
                    self.move(self.pos() + event.globalPos() - self.clickPosition)
                    self.clickPosition = event.globalPos()
                    event.accept()
        except: pass
    
    def newForm(self):
        self.modoCont = 'comprueba'
        self.btn_cont = False
        self.opcSelec = ''

        self.info = Obtener_ecuacion(0)
        nums = Obtener_numeros(self.info[3])

        self.ui.lbl_ecuaciones.setText(self.info[4])

        self.ui.btn_opc1.setText(str(nums[0]))
        self.ui.btn_opc2.setText(str(nums[1]))
        self.ui.btn_opc3.setText(str(nums[2]))
        self.ui.btn_opc4.setText(str(nums[3]))

        self.ui.btn_opc1.clicked.connect(lambda: self.func_btn('opc1'))
        self.ui.btn_opc2.clicked.connect(lambda: self.func_btn('opc2'))
        self.ui.btn_opc3.clicked.connect(lambda: self.func_btn('opc3'))
        self.ui.btn_opc4.clicked.connect(lambda: self.func_btn('opc4'))

    def func_btn(self, opc): 
        self.btn_cont = True
        azul = 'border: 4px solid rgb(5, 125, 189);' 
        gris = 'border: 4px solid rgb(56, 57, 59);'

        if self.opcSelec == '':
            self.ui.btn_continuar.setStyleSheet(
                'background: rgb(60, 193, 99);'
            )
            self.ui.btn_continuar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.opcSelec = opc

        self.ui.btn_opc1.setStyleSheet(gris)
        self.ui.btn_opc2.setStyleSheet(gris)
        self.ui.btn_opc3.setStyleSheet(gris)
        self.ui.btn_opc4.setStyleSheet(gris)

        if opc == 'opc1': self.ui.btn_opc1.setStyleSheet(azul)
        if opc == 'opc2': self.ui.btn_opc2.setStyleSheet(azul)
        if opc == 'opc3': self.ui.btn_opc3.setStyleSheet(azul)
        if opc == 'opc4': self.ui.btn_opc4.setStyleSheet(azul)

    def func_continuar(self):
        if self.modoCont == 'comprueba' and self.btn_cont: 
            num = '0'

            if self.opcSelec == 'opc1': num = self.ui.btn_opc1.text()
            if self.opcSelec == 'opc2': num = self.ui.btn_opc2.text()
            if self.opcSelec == 'opc3': num = self.ui.btn_opc3.text()
            if self.opcSelec == 'opc4': num = self.ui.btn_opc4.text()

            if int(num) == self.info[3]:
                self.ui.lbl_title.setText('Respuesta Correcta')
                self.ui.lbl_title.setStyleSheet('color: rgb(32, 195, 84);')
                self.ui.btn_continuar.setStyleSheet('background: rgb(32, 195, 84);')

            else:
                self.ui.lbl_title.setText('Respuesta Incorrecta')
                self.ui.lbl_title.setStyleSheet('color: rgb(228, 110, 130);')
                self.ui.btn_continuar.setStyleSheet('background: rgb(228, 110, 130);')

            self.ui.btn_continuar.setText('¡Siguiente Pregunta!')
            self.modoCont = 'siguiente'
        
        
        elif self.modoCont == 'siguiente':
            self.ui.lbl_title.setStyleSheet('color: rgba(202, 242, 255, 0.9);')
            self.ui.lbl_title.setText('Resuelve')

            self.ui.btn_continuar.setStyleSheet('background-color: rgb(56, 57, 59);')
            self.ui.btn_continuar.setText('Comprueba')
            gris = 'border: 4px solid rgb(56, 57, 59);'
            
            self.ui.btn_opc1.setStyleSheet(gris)
            self.ui.btn_opc2.setStyleSheet(gris)
            self.ui.btn_opc3.setStyleSheet(gris)
            self.ui.btn_opc4.setStyleSheet(gris)
            self.newForm()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv) 
    app.setWindowIcon(QtGui.QIcon('./Math.ico'))
    window = MainApp() 
    window.show() 
    sys.exit(app.exec_())

#* Author: Francisco Velez
