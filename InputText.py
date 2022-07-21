import tkinter as tk
def inputText(strArr,validate):
        ventana1 = tk.Tk()
        ventana1.title("Welcome")
        label1=tk.Label(ventana1,text="Input Text 1")
        label1.grid(column=0, row=0)

        label2=tk.Label(ventana1,text="Input Text 2")
        label2.grid(column=0, row=2)

        

        stringA = tk.StringVar()
        stringB = tk.StringVar()
        strArr.append(stringA)
        strArr.append(stringB)

        entry1=tk.Entry(ventana1, width=30, textvariable=stringA)
        entry2=tk.Entry(ventana1, width=30, textvariable=stringB)

        entry1.grid(column=1, row=0)
        entry2.grid(column=1, row=2)
        
        boton1=tk.Button(ventana1, text="Validate", command=validate)
        boton1.grid(column=1, row=3)
        ventana1.mainloop()