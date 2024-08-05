import tkinter as tk
from tkinter import messagebox

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Alumnos")
        
        # Diccionario para almacenar los alumnos y sus materias
        self.alumnos = {}
        
        # Widgets de la interfaz
        self.crear_widgets()

    def crear_widgets(self):
        # Etiquetas y entradas para el nombre del alumno
        tk.Label(self.root, text="Nombre del alumno:").grid(row=0, column=0)
        self.alumnos_entry = tk.Entry(self.root)
        self.alumnos_entry.grid(row=0, column=1)
        
        # Etiquetas y entradas para la materia
        tk.Label(self.root, text="Materia:").grid(row=1, column=0)
        self.materia_entry = tk.Entry(self.root)
        self.materia_entry.grid(row=1, column=1)
        
        # Botones para agregar, editar y borrar
        tk.Button(self.root, text="Agregar alumno", command=self.agregar_alumnos).grid(row=2, column=0)
        tk.Button(self.root, text="Agregar materia", command=self.agregar_materias).grid(row=2, column=1)
        tk.Button(self.root, text="Borrar Alumno", command=self.borrar_alumno).grid(row=3, column=0)
        tk.Button(self.root, text="Borrar Materia", command=self.borrar_materia).grid(row=3, column=1)
        
        # Lista para mostrar alumnos y materias
        self.listbox = tk.Listbox(self.root, width=50)
        self.listbox.grid(row=4, column=0, columnspan=2)
        tk.Button(self.root, text='Mostrar lista completa', command=self.mostrar_lista).grid(row=5, column=0, columnspan=2)

    def agregar_alumnos(self):
        nombre = self.alumnos_entry.get()
        if nombre:
            if nombre not in self.alumnos:
                self.alumnos[nombre] = []
                self.actualizar_listbox()
                messagebox.showinfo('Éxito', f'Alumno {nombre} agregado')
            else:
                messagebox.showwarning('Advertencia', 'El alumno ya existe.')
        else:
            messagebox.showwarning('Advertencia', 'El nombre del alumno no puede estar vacío.')

    def agregar_materias(self):
        nombre = self.alumnos_entry.get()
        materia = self.materia_entry.get()
        if nombre in self.alumnos and materia:
            self.alumnos[nombre].append(materia)
            self.actualizar_listbox()
            messagebox.showinfo('Éxito', f'Materia {materia} agregada a {nombre}')
        else:
            messagebox.showwarning('Advertencia', 'Debes seleccionar un alumno válido y una materia válida.')

    def borrar_alumno(self):
        nombre = self.alumnos_entry.get()
        if nombre in self.alumnos:
            del self.alumnos[nombre]
            self.actualizar_listbox()
            messagebox.showinfo('Éxito', f'Alumno {nombre} eliminado')
        else:
            messagebox.showwarning('Advertencia', 'El alumno no existe.')

    def borrar_materia(self):
        nombre = self.alumnos_entry.get()
        materia = self.materia_entry.get()
        if nombre in self.alumnos and materia in self.alumnos[nombre]:
            self.alumnos[nombre].remove(materia)
            self.actualizar_listbox()
            messagebox.showinfo('Éxito', f'Materia {materia} eliminada de {nombre}')
        else:
            messagebox.showwarning('Advertencia', 'El alumno o la materia no existen.')

    def mostrar_lista(self):
        self.listbox.delete(0, tk.END)
        for alumno, materias in self.alumnos.items():
            self.listbox.insert(tk.END, f'{alumno}: {", ".join(materias)}')

    def actualizar_listbox(self):
        self.listbox.delete(0, tk.END)
        for alumno in self.alumnos:
            self.listbox.insert(tk.END, alumno)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()