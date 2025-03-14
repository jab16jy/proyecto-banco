import tkinter as tk
from tkinter import messagebox


class Vista:
    def __init__(self, controlador):
        self.controlador = controlador
        self.ventana = tk.Tk()
        self.ventana.title("Banco App")
        self.ventana.geometry("400x300")


        self.etiqueta_titulo = tk.Label(self.ventana, text="Bienvenido al Banco", font=("Arial", 16))
        self.etiqueta_titulo.pack(pady=10)


        self.etiqueta_cantidad = tk.Label(self.ventana, text="Cantidad:")
        self.etiqueta_cantidad.pack()
        self.entrada_cantidad = tk.Entry(self.ventana)
        self.entrada_cantidad.pack()


        self.boton_depositar = tk.Button(self.ventana, text="Depositar", command=self.depositar)
        self.boton_depositar.pack(pady=5)


        self.boton_retirar = tk.Button(self.ventana, text="Retirar", command=self.retirar)
        self.boton_retirar.pack(pady=5)


        self.boton_consultar = tk.Button(self.ventana, text="Consultar Saldo", command=self.consultar_saldo)
        self.boton_consultar.pack(pady=5)


        self.boton_salir = tk.Button(self.ventana, text="Salir", command=self.ventana.quit)
        self.boton_salir.pack(pady=10)

    def depositar(self):
        try:
            cantidad = float(self.entrada_cantidad.get())
            exito, mensaje = self.controlador.modelo.depositar(cantidad)
            messagebox.showinfo("Resultado", mensaje)
        except ValueError:
            messagebox.showerror("Error", "Ingrese un número válido.")

    def retirar(self):
        try:
            cantidad = float(self.entrada_cantidad.get())
            exito, mensaje = self.controlador.modelo.retirar(cantidad)
            messagebox.showinfo("Resultado", mensaje)
        except ValueError:
            messagebox.showerror("Error", "Ingrese un número válido.")

    def consultar_saldo(self):
        saldo = self.controlador.modelo.consultar_saldo()
        messagebox.showinfo("Saldo", saldo)

    def iniciar(self):
        self.ventana.mainloop()

#JOHAN BORRERO desarrollo de aplicaciones web ii 
