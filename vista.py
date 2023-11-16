import sys 
from PyQt5.QtWidgets import QApplication,QMainWindow, QDialog, QMessageBox,QLineEdit,QTextEdit
from PyQt5.QtGui import QRegExpValidator, QIntValidator
from PyQt5.QtCore import Qt,QRegExp
from PyQt5.uic import loadUi

class VentanaPpal(QMainWindow):
    def __init__(self,ppal=None):
        super().__init__(ppal)
        loadUi("Pantt.ui",self)
        self.setup()
    def setup(self):
            self.sesion.clicked.connect(self.abrir_ventana_login) 
            self.cerrar.connect(self.salir) #crear función 

    def abrir_ventana_login(self):
        ventana_ingresar= VentanaLogin(self)
        self.hide()
        ventana_ingresar.show()



class VentanaLogin(QDialog):
    def __init__(self,ppal=None):
        super().__init__(ppal)
        loadUi("Ingreso.ui",self)
        self.__ventanaPadre=ppal
        self.setup()

    def setup(self):
        self.usuario.setValidator(QRegExpValidator(QRegExp("[a-zA-Z ]+")))
        self.password.setValidator(QIntValidator())
        self.botonIngreso.accepted.connect(self.opcionAceptar)
        self.botonIngreso.rejected.connect(self.opcionCancelar)
    
    def opcionAceptar(self):
        login= self.usuario.text()
        password= self.password.text()
        print(login, password)

    def opcionCancelar(self):
        self.__ventanaPadre.show()

    