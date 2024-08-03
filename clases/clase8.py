#calculadora simple

#importamos tkinter para crear la interfaz gráfica
import tkinter as tk

#generamos la clase calculadora que hereda de tk.Tk
class calculadora:
    #constructor de la clase calculadora
    def __init__(self,root):
        self.root = root
        self.root.title("Calculadora Simple")
        
        #tamaño de la pantalla y borde
        self.pantalla = tk.Entry(root, width = 35, borderwidth = 5) 
        self.pantalla.grid(row = 0, column = 0, columnspan = 4, padx = 10, pady = 10)
        
        #botones numéricos
        botones = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]
        
        fila = 1
        columna = 0
        #recorremos los botones y los añadimos a la pantalla
        for btn in botones:
            self.crear_boton(btn, fila, columna)
            columna += 1
            if columna > 3:
                columna = 0
                fila += 1
        self.operacion = ""

    def crear_boton(self, valor, fila, columna):
        boton = tk.Button(self.root, text = valor, padx = 40, pady = 20, command = lambda: self.bton_click(valor))
        boton.grid(row = fila, column = columna)

    def bton_click(self, valor):
        if valor == "=":
            try:
                resultado = str(eval(self.operacion))
                self.pantalla.delete(0, tk.END)
                self.pantalla.insert(0, resultado)
                self.operacion = ""
            except:
                self.pantalla.delete(0, tk.END)
                self.pantalla.insert(0, 'herror')
                self.operacion = ""
        else:
            self.operacion += str(valor)
            self.pantalla.delete (0, tk.END)
            self.pantalla.insert(0, self.operacion)
if __name__ == "__main__":
    root = tk.Tk()
    app = calculadora(root)
    root.mainloop()


"----------------------------------------------------------------------------"

