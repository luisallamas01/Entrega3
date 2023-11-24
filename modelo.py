import json
import os
import pydicom
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
from io import BytesIO

dicc={'medicoAnalitico': 'bio12345', 'Yesid': '31415', 'Luisa': '12345', 'Paulina': '27182'}
usuarios=json.dumps(dicc, indent=4)
ruta_completa = os.path.join("Usuarios")


with open(ruta_completa,'w') as archivo:
    archivo.write(usuarios)

class Sistema():
    def __init__(self):
        with open('Usuarios') as file:
            dicc= json.load(file)
        self.__usuarios= dicc
        self.__ruta=""
        self.archivos = ''

    def verificar_usu(self, usu, password):
        
        if self.__usuarios.get(usu, False):
            return True
        else:
            print('no esta')

    def guardar_ruta(self, r): #esta función me debe retornar el plot del pixel array y los 5 datos del paciente
        self.__ruta= r

    def enviar_ruta(self):
        return self.__ruta
    def mandar_img(self):
        for i in self.archivos:
            ruta = f'{self.__ruta}/{i}'
            dcm = pydicom.dcmread(ruta)
            img = dcm.pixel_array

            if (len(img.shape))==3:
                slice_index = img.shape[0] // 2
                selected_slice = img[slice_index, :, :]
                a = plt.imshow(selected_slice, cmap=plt.cm.bone)
                datos_imagen = a.get_array()
                buffer = BytesIO()
                np.save(buffer, datos_imagen)
                imagen_bytes = buffer.getvalue()
                return imagen_bytes
            else:
                a = plt.imshow(img, cmap = plt.cm.bone)
                datos_imagen = a.get_array()
                buffer = BytesIO()
                np.save(buffer, datos_imagen)
                imagen_bytes = buffer.getvalue()
                return imagen_bytes
            plt.axis('off')
            plt.savefig("temp_image.png")
            


    def abrir_img(self, img):
        dcm = pydicom.dcmread(img)
        img = dcm.pixel_array

        if (len(img.shape))==3:
            slice_index = img.shape[0] // 2
            selected_slice = img[slice_index, :, :]
            plt.imshow(selected_slice, cmap=plt.cm.bone)
        else:
            plt.imshow(img, cmap = plt.cm.bone)
        plt.axis('off')
        plt.savefig("temp_image.png")

    def guardar_lista(self, l):
        self.archivos = l
           #return(plt.imshow(img))
        
    def metadata(self,r):
        dcm = pydicom.dcmread(r)

        n = dcm.PatientName
        c = dcm.PatientID
        s = dcm.PatientSex
        e = dcm.PatientAge
        p = dcm.PatientWeight

        return n,c,s,e,p

