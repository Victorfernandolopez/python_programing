import tkinter as tk
from tkinter import ttk

class conversorMoneda:
    def __init__(self, root):
        self.root = root
        self.root.title("Conversor de Monedas")
        
        self.cantidad_label = tk.Label(root, text="Cantidad de moneda:")
        self.cantidad_label.grid(row=0, column=0)
        
        self.cantidad_entry = tk.Entry(root)
        self.cantidad_entry.grid(row=0, column=1)
        
        self.moneda_origen_label = tk.Label(root, text="Moneda de origen:")
        self.moneda_origen_label.grid(row=1, column=0)
        
        self.moneda_origen = ttk.Combobox(root, values=["usd", "eur", "gbp", "jpy"])
        self.moneda_origen.grid(row=1, column=1)
        self.moneda_origen.set("usd")
        
        self.moneda_destino_label = tk.Label(root, text="Moneda de destino:")
        self.moneda_destino_label.grid(row=2, column=0)
        
        self.moneda_destino = ttk.Combobox(root, values=["usd", "eur", "gbp", "jpy"])
        self.moneda_destino.grid(row=2, column=1)
        self.moneda_destino.set("eur")
        
        self.convertir_btn = tk.Button(root, text="Convertir", command=self.convertir)
        self.convertir_btn.grid(row=3, column=0, columnspan=2)
        
        self.resultado_label = tk.Label(root, text="Resultado:")
        self.resultado_label.grid(row=4, column=0, columnspan=2)
    
    def convertir(self):
        cantidad = float(self.cantidad_entry.get())
        moneda_origen = self.moneda_origen.get()
        moneda_destino = self.moneda_destino.get()
        tasa_cambio = self.obtener_tasa_cambio(moneda_origen, moneda_destino)
        resultado = cantidad * tasa_cambio
        self.resultado_label.config(text=f"Resultado: {resultado:.2f} {moneda_destino}")
    
    def obtener_tasa_cambio(self, moneda_origen, moneda_destino):
        tasa_cambio = {
            "usd": { "eur": 0.85, "gbp": 0.78, "jpy": 112.70 },
            "eur": { "usd": 1.15, "gbp": 0.89, "jpy": 128.80 },
            "gbp": { "usd": 1.36, "eur": 1.18, "jpy": 151.20 },
            "jpy": { "usd": 0.009, "eur": 0.008, "gbp": 0.007 }
        }
        if moneda_origen == moneda_destino:
            return 1
        return tasa_cambio[moneda_origen][moneda_destino]

if __name__ == "__main__":
    root = tk.Tk()
    app = conversorMoneda(root)
    root.mainloop()