from modelo import *
from vista import VentanaPpal
from PyQt5.QtWidgets import QApplication
import sys 

class Coordinador:
    def __init__(self,vista,modelo):
        self.__miVista = vista
        self.__miModelo = modelo

def main():
    app=QApplication(sys.argv)
    mi_vista=VentanaPpal()
    #mi_modelo=Sistema()
    #mi_controlador=Coordinador(mi_vista,mi_modelo)
    #mi_vista.setControlador(mi_controlador)
    #mi_vista.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
    