#App para convertir pies a metros usando Tkinter
#Hernández Trejo Humberto
#23-02-2023

from tkinter import *
from tkinter import ttk

class Conversor:
    #normalmente las variables van dentro del init
    def __init__(self, raiz): #init es equivalente al contructor de la clase
        
        raiz.title("Pies a Metros")

        self.pies = StringVar()
        self.metros = StringVar()

        #Se crea el frame principal
        mainFrame = ttk.Frame(raiz)
        mainFrame.grid(column=0, row=0) #acomoda el frame

        piesEntry = ttk.Entry(mainFrame, textvariable=self.pies)
        piesEntry.grid(column=1, row=0)

        #objeto anonimo
        ttk.Label(mainFrame, text="Pies").grid(column=2, row=0)
        ttk.Label(mainFrame, text="Son equivalentes a: ").grid(column=0, row=1)
        ttk.Label(mainFrame, textvariable=self.metros).grid(column=1, row=1)
        ttk.Label(mainFrame, text="Metros").grid(column=2, row=1)

        ttk.Button(mainFrame, text="Calcular", command=self.calcular).grid(column=2, row=2)

        #Hacer la operación presionando enter
        raiz.bind("<Return>",self.calcular)

    def calcular(self, *args):
        print("Boton presionado")
        piesUsuario = self.pies.get() #Siempre devuelve la cadena
        print("Pies ingresados: ", piesUsuario)
        piesFlotantes = float(piesUsuario)#Convertir dato a flotante
        metros = piesFlotantes * 0.3048
        print("Metros: ", metros)
        self.metros.set(metros)


if __name__ == "__main__":
    print("Este es el archivo principal")
    print("Solo se mostrara esto si es el principal")
