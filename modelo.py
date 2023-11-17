import json
import os

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

    def verificar_usu(self, usu, password):
        if self.__usuarios[usu]==password:
            return True
        

