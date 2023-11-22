from modelo import *
from vista import VentanaPpal
from PyQt5.QtWidgets import QApplication
import sys 
import pydicom
class Coordinador:
    def __init__(self,vista,modelo):
        self.__miVista = vista
        self.__miModelo = modelo
    def recibir_login1(self, u,p):
        b= self.__miModelo.verificar_usu(u,p)
        if b :
            return True
    def recibe_rut(self, r):
        a=self.__miModelo.guardar_ruta(r)
        return True
    
    def enviar_rut(self):
        b= self.__miModelo.enviar_ruta()
        return b
    
def main():
    app=QApplication(sys.argv)
    mi_vista=VentanaPpal()
    mi_modelo=Sistema()
    mi_controlador=Coordinador(mi_vista,mi_modelo)
    mi_vista.set_controlador(mi_controlador)
    mi_vista.show()
    sys.exit(app.exec_())


# dcm = pydicom.dcmread("C:/Users/luisa/Documents/TrabajoF_Monitor/Entrega3/DCM1/1-001.dcm")
# img = dcm.pixel_array
# print(img.shape)
# plt.imshow(img)
# plt.show()
# print("Hola")
# if (len(img.shape))==3:
#     slice_index = img.shape[0] // 2
#     selected_slice = img[slice_index, :, :]
#     plt.imshow(selected_slice, cmap=plt.cm.bone)
# else:
#     plt.imshow(img, cmap = plt.cm.bone)
#     plt.axis('off')
#     plt.savefig("temp_image.png")

if __name__ == '__main__':
   main()
#C:/Users/luisa/Documents/TrabajoF_Monitor/Entrega3/DCM1
