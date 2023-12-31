import sys 
from PyQt5.QtWidgets import QApplication,QMainWindow , QDialog, QMessageBox,QLineEdit,QTextEdit
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QSlider, QFileDialog, QWidget
from PyQt5.QtGui import QRegExpValidator, QIntValidator, QPixmap
from PyQt5.QtCore import Qt,QRegExp
from PyQt5.uic import loadUi
import pyqtgraph as pg
import os
import matplotlib.pyplot as plt
from io import BytesIO
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
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
    def r_controlador(self):
        return self.__miControlador
    

class VentanaLogin(QDialog):
    def __init__(self,ppal=None):
        super().__init__(ppal)
        loadUi("Ingreso.ui",self)
        self.__ventanaPadre=ppal
        self.setup()

    def setup(self):
        self.usuario.setValidator(QRegExpValidator(QRegExp("[a-zA-Z ]+")))
        self.password.setValidator(QRegExpValidator())
        self.buttonBox.accepted.connect(self.opcionAceptar)
        self.buttonBox.rejected.connect(self.opcionCancelar)
    
    def opcionAceptar(self):
        
        login= self.usuario.text()
        password= self.password.text()
        
        a = self.__ventanaPadre.recibir_login(login,password)
        
        if a:
            self.controlador = self.__ventanaPadre.r_controlador()
            ventana_menu = Ventana_men(self)
            self.hide()
            ventana_menu.show()
         
        else:
            self.mensaje_('Contraseña o usuario incorrecto, vuelva a intentar.')
    def set_controlador1(self):
        self.controlador = self.__ventanaPadre.r_controlador()

    def r_controlador1(self):
        return self.controlador
    
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
        self.controlador = ''


    def setup(self):
        self.abrir_archivo.clicked.connect(self.abrir_carpeta)
            #self.carpeta = None  # Inicializar carpeta como None
    
    def set_controlador(self):
        self.controlador = self.__ventanaPadre.r_controlador1()

    def abrir_carpeta(self):
        ruta_carpeta = QFileDialog.getExistingDirectory(self, 'Seleccionar Carpeta', '/')
        self.controlador = self.__ventanaPadre.r_controlador1()
        archivos = os.listdir(ruta_carpeta)
        todos_dcm = all(archivo.endswith(".dcm") for archivo in archivos)

        if todos_dcm:
            print(f"Archivo cargado exitosamente!!!")
            self.controlador.recibe_rut(ruta_carpeta)
            self.controlador.recibir_lista(archivos)
            ventana_vista = Ventana_vis(self)
            self.hide()
            ventana_vista.show()

        else:
            print("Formato no válido.")

            msg = QMessageBox(self)
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle("Resultado")
            msg.setText("Archivo no valido")
            msg.show()
    # def abrir_carpeta(self):
    #     self.carpeta = self.ruta.text()
    #     self.carpeta = self.carpeta.replace("\\", "/")
    #     self.__ventanaPadre.recibir_ruta1(self.carpeta)
    #     ventana_vista = Ventana_vis(self)
    #     self.hide()
    #     ventana_vista.show()
    # def ver_carpeta(self):
    #     return self.carpeta
    # def envia_rut(self, r):
    #     self.__ventanaPadre.recibir_ruta1(r)

    # def traer_ruta(self):
    #     return self.__ventanaPadre.trae_ruta()
    

    def r_controlador2(self):
        return self.controlador
class Ventana_vis(QDialog):
    def __init__(self,ppal=None): #Lo que se hace aquí es crear una ventana que me diga las carpetas DCM idsponibles y que el usuario seleccione una
       super().__init__(ppal)
       loadUi('visualizador.ui',self)
       self.figure = Figure()
       self.layout = QVBoxLayout()
       self.canvas = FigureCanvas(self.figure)
       self.layout.addWidget(self.canvas)
       self.__ventanaPadre=ppal
       
       self.controlador = self.__ventanaPadre.r_controlador2()
       self.numero = self.controlador.enviar_rut()
       self.setup()
       print(self.numero)
    def set_controlador(self):
        self.controlador = self.__ventanaPadre.r_controlador2()
        
        

    
    def setup(self):
        # self.siguiente.cliked.connect(self.siguiente_img)
        # self.atras.cliked.connect(self.atras_img)
        a = self.numero 
        self.valor_slider = 0
        self.slider.setMinimum(0)   
        self.slider.setMaximum(a-1)
        self.slider.valueChanged.connect(self.actualizar_img)
        self.meta.setText(self.controlador.enviar_metadata())
        
        
    def actualizar_img(self,valor):
        self.valor_slider = valor
        print(self.valor_slider)
        self.img = self.controlador.send_img(self.valor_slider) 
        plt.imsave('imagen.png', self.img, cmap='gray')
        pixmap = QPixmap("imagen.png")
        self.imagen.setPixmap(pixmap)
        os.remove('imagen.png')
    

        # Crear un QPixmap desde la imagen y configurarlo en un QLabel
        #pixmap = QPixmap('imagen.png')
        # etiqueta_imagen = QLabel()
        # etiqueta_imagen.setPixmap(pixmap)
        # # self.figure.clear()
        # ax = self.figure.add_subplot(111)
        # img = plt.imread(BytesIO(self.img))
        # ax.imshow(img)
        # self.canvas.draw()
        # pixmap = QPixmap()
        # pixmap.loadFromData(self.imagen)
        # self.labelImagen.setPixmap(pixmap)
        # print('hola')
    
     
     
   