import sys 
from PyQt5.QtWidgets import QApplication,QMainWindow , QDialog, QMessageBox,QLineEdit,QTextEdit
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QSlider
from PyQt5.QtGui import QRegExpValidator, QIntValidator, QPixmap
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
        x = self.__miControlador.recibir_login1(u, p)
        if x:
            return True
    def recibir_ruta(self, r):
        x= self.__miControlador.recibe_rut(r)

    def traer_ruta(self):
        return self.__miControlador.enviar_rut()
        
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
    def recibir_ruta1(self,r):
        self.__ventanaPadre.recibir_ruta(r)
    def trae_ruta(self):
        return self.__ventanaPadre.traer_ruta()

class Ventana_men(QDialog):
    def __init__(self,ppal=None): #Lo que se hace aquí es crear una ventana que me diga las carpetas DCM idsponibles y que el usuario seleccione una
        super().__init__(ppal)
        loadUi('menu.ui',self)
        self.__ventanaPadre=ppal
        self.carpeta= None
        self.setup()


    def setup(self):
            self.abrir_ruta.clicked.connect(self.abrir_carpeta)
            #self.carpeta = None  # Inicializar carpeta como None
            
    def abrir_carpeta(self):
        self.carpeta = self.ruta.text()
        self.carpeta = self.carpeta.replace("\\", "/")
        self.__ventanaPadre.recibir_ruta1(self.carpeta)
        ventana_vista = Ventana_vis(self)
        self.hide()
        ventana_vista.show()
    def ver_carpeta(self):
        return self.carpeta
    def envia_rut(self, r):
        self.__ventanaPadre.recibir_ruta1(r)

    def traer_ruta(self):
        return self.__ventanaPadre.trae_ruta()
class Ventana_vis(QDialog):
    def __init__(self,ppal=None): #Lo que se hace aquí es crear una ventana que me diga las carpetas DCM idsponibles y que el usuario seleccione una
       super().__init__(ppal)
       loadUi('visualizador.ui',self)
       self.__ventanaPadre=ppal
       self.carpeta= self.__ventanaPadre.traer_ruta()
       print(self.carpeta)
       self.setup()
       lista_archivos = os.listdir(self.carpeta)
  
       for i in lista_archivos:
           print(i)
       
       print(self.carpeta)
    
    def setup(self):
        pass
        # self.siguiente.cliked.connect(self.siguiente_img)
        # self.atras.cliked.connect(self.atras_img)
        # self.slider.cliked.connect(self.slider_img)
    
    
     
     
   