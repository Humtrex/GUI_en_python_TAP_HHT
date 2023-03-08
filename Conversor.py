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
        mainFrame = ttk.Frame(raiz, padding="7 7 16 16") #(izq, arriba, der, abajo)
        mainFrame.grid(column=0, row=0) #acomoda el frame

        piesEntry = ttk.Entry(mainFrame,width=7, textvariable=self.pies) #WIGHT numero de caracteres
        piesEntry.grid(column=1, row=0, sticky=(W,E))

        #objeto anonimo
        ttk.Label(mainFrame, text="Pies").grid(column=2, row=0) #sticky predeterminado centra
        ttk.Label(mainFrame, text="Son equivalentes a: ",padding=(5,10,5,10)).grid(column=0, row=1)
        ttk.Label(mainFrame, textvariable=self.metros).grid(column=1, row=1)
        ttk.Label(mainFrame, text="Metros").grid(column=2, row=1)

        ttk.Button(mainFrame, text="Calcular", command=self.calcular).grid(column=2, row=2)

        piesEntry.focus() #focus pone el interes en un widget

        #Hacer la operación presionando enter
        raiz.bind("<Return>",self.calcular)

    def calcular(self, *args):
        print("Boton presionado")
        piesUsuario = self.pies.get() #Siempre devuelve la cadena
        print("Pies ingresados: ", piesUsuario)
        try:
            piesFlotantes = float(piesUsuario)#Convertir dato a flotante
            metros = piesFlotantes * 0.3048
            print("Metros: ", metros)
            self.metros.set(metros)
        except ValueError:
            print("No es un dato valido")
            self.pies.set("")


if __name__ == "__main__":
    print("Este es el archivo principal")
    print("Solo se mostrara esto si es el principal")
