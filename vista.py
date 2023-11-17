import sys 
from PyQt5.QtWidgets import QApplication,QMainWindow , QDialog, QMessageBox,QLineEdit,QTextEdit
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout
from PyQt5.QtGui import QRegExpValidator, QIntValidator
from PyQt5.QtCore import Qt,QRegExp
from PyQt5.uic import loadUi
import os
class VentanaPpal(QMainWindow):
    def __init__(self,ppal=None):
        super().__init__(ppal)
        loadUi("Pantt.ui",self)
        self.setup()
    def setup(self):
            self.sesion.clicked.connect(self.abrir_ventana_login) 
            self.cerrar.clicked.connect(self.salir) #crear función 

    def abrir_ventana_login(self):
        ventana_ingresar= VentanaLogin(self)
        self.hide()
        ventana_ingresar.show()
    def salir(self):
        pass
    def recibir_login(self, u, p):
        self.__miCoordinador.recibir_login(u, p)


class VentanaLogin(QDialog):
    def __init__(self,ppal=None):
        super().__init__(ppal)
        loadUi("Ingreso.ui",self)
        self.__ventanaPadre=ppal
        self.setup()

    def setup(self):
        self.usuario.setValidator(QRegExpValidator(QRegExp("[a-zA-Z ]+")))
        self.password.setValidator(QIntValidator())
        self.buttonBox.accepted.connect(self.opcionAceptar)
        self.buttonBox.rejected.connect(self.opcionCancelar)
    
    def opcionAceptar(self):
        w= QLabel(self)
        w.setText("Ha ingresado con éxito")
        w.show()
        login= self.usuario.text()
        password= self.password.text() 
        #Verificar que esté en el json
        #Ventana_men= Ventana_men()
    def opcionCancelar(self):
        self.__ventanaPadre.show()
class Ventana_men(QDialog):
    def __init__(self,ppal=None): #Lo que se hace aquí es crear una ventana que me diga las carpetas DCM idsponibles y que el usuario seleccione una
        super().__init__(ppal)
        
        ruta_actual = os.getcwd()

        # Obtener la lista de subcarpetas en el directorio actual
        subcarpetas = [nombre for nombre in os.listdir(ruta_actual) if os.path.isdir(os.path.join(ruta_actual, nombre))]

        # Crear botones para cada subcarpeta
        self.botones_subcarpetas = []

        for subcarpeta in subcarpetas:
            boton = QPushButton(subcarpeta)
            boton.clicked.connect(self.mostrar_mensaje)
            self.botones_subcarpetas.append(boton)

        # Configurar el diseño de la ventana
        layout = QVBoxLayout()

        for boton in self.botones_subcarpetas:
            layout.addWidget(boton)

        self.setLayout(layout)

    def mostrar_mensaje(self):
        # Mostrar el mensaje correspondiente al botón presionado
        boton_presionado = self.sender()
        mensaje = f"Has presionado el botón '{boton_presionado.text()}'"
        print(mensaje)


    def opcionCancelar(self):
        self.__ventanaPadre.show()

    