from modelo import Banco
from vista import Vista


class Controlador:
    def __init__(self):
        self.modelo = Banco()
        self.vista = Vista(self)

    def ejecutar(self):
        self.vista.iniciar()



if __name__ == "__main__":
    controlador = Controlador()
    controlador.ejecutar()

#JOHAN BORRERO desarrollo de aplicaciones web ii 
