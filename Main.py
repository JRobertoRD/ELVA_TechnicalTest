
from tkinter import messagebox
from typing import final
import InputText as it

class Aplicacion:
    def __init__(self):
        self.strArr = []

    def validate(self):
        flag = False
        listWords1 = self.strArr[0].get().split(",")
        listWords2 = self.strArr[1].get().split(",")

        listWords1 = self.toLoweCase(listWords1)
        listWords2 = self.toLoweCase(listWords2)

        set1 = set(listWords1)
        set2 = set(listWords2)

        final = set1 & set2

        print (final)
        if(len(final) > 0):
            
            messagebox.showinfo(message="TRUE\n"+"The repeat words are\n"+"["+", ".join(final)+"]", title="Título")
        else:
            messagebox.showinfo(message="FALSE", title="Título")


    
    def toLoweCase(self,list):
        for i in range(len(list)):
            list[i] = list[i].lower()
        return list



aplicacion1=Aplicacion() 
it.inputText(aplicacion1.strArr, aplicacion1.validate)
