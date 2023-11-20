from modelo import *
from vista import VentanaPpal
from PyQt5.QtWidgets import QApplication
import sys 

class Coordinador:
    def __init__(self,vista,modelo):
        self.__miVista = vista
        self.__miModelo = modelo
    def recibir_login1(self, u,p):
        b= self.__miModelo.verificar_usu(u,p)
        if b :
            return True
def main():
    app=QApplication(sys.argv)
    mi_vista=VentanaPpal()
    mi_modelo=Sistema()
    mi_controlador=Coordinador(mi_vista,mi_modelo)
    mi_vista.set_controlador(mi_controlador)
    mi_vista.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
    