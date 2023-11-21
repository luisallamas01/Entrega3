import sys 
from PyQt5.QtWidgets import QApplication,QMainWindow , QDialog, QMessageBox,QLineEdit,QTextEdit
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QSlider,QPixmap
from PyQt5.QtGui import QRegExpValidator, QIntValidator
from PyQt5.QtCore import Qt,QRegExp
from PyQt5.uic import loadUi
import os
import pydicom
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
        x = self.__miControlador.recibir_login1(u, p)
        if x:
            return True

    def set_controlador(self,c):
        self.__miControlador  = c

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
        
        login= self.usuario.text()
        password= self.password.text()
        
        a = self.__ventanaPadre.recibir_login(login,password)
        
        if a:
            print('hola')
            ventana_menu = Ventana_men(self)
            self.hide()
            ventana_menu.show()
         
        else:
            self.mensaje_('Contraseña o usuario incorrecto, vuelva a intentar.')

    def mensaje_(self,m):
        self.mensaje.setText(m) #buscar si este metodo sirve
       
    def opcionCancelar(self):
        self.usuario.text('')
        self.password.text('')

class Ventana_men(QDialog):
    def __init__(self,ppal=None): #Lo que se hace aquí es crear una ventana que me diga las carpetas DCM idsponibles y que el usuario seleccione una
        super().__init__(ppal)
        loadUi('menu.ui',self)
        self.setup()

    def setup(self):
            self.abrir_ruta.clicked.connect(self.abrir_carpeta)
            self.carpeta = None  # Inicializar carpeta como None
            self.slider = QSlider(self)
            self.layout = QVBoxLayout(self)
            self.layout.addWidget(self.slider)
            self.imagen_label = QLabel(self)
            self.layout.addWidget(self.imagen_label)

            self.slider.valueChanged.connect(self.mostrar_imagen)
    def abrir_carpeta(self):
            self.carpeta = self.ruta.text()
            lista_archivos = os.listdir(self.carpeta)

            # Configurar el slider
            self.slider.setMinimum(0)
            self.slider.setMaximum(len(lista_archivos) - 1)
            self.slider.setSingleStep(1)

            # Mostrar la primera imagen
            if lista_archivos:
                self.mostrar_imagen(0)
    def mostrar_imagen(self, indice):#en imagen_path lo que se carga es el dataset, hay que cambiar la logica con un metodo que extraiga el data set,
            if self.carpeta:
                lista_archivos = os.listdir(self.carpeta)
                if 0 <= indice < len(lista_archivos):
                    imagen_path = os.path.join(self.carpeta, lista_archivos[indice])
                    pixmap = QPixmap(imagen_path)
                    self.imagen_label.setPixmap(pixmap)
    