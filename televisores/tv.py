class TV:
    from televisores.control import Control

    canal = 1
    volumen = 1
    precio = 500
    control = Control
    numTV = 0

    def __init__(self, marca, estado):
        self.marca = marca
        self.estado = estado
        self.numTV += 1


    def setMarca(self, marca):
        self.marca = marca

    def getMarca(self):
        return self.marca

    def setControl(self, control):
        self.control = control

    def getControl(self):
        return self.control

    def setPrecio(self, precio):
        self.precio = precio

    def getPrecio(self):
        return self.precio

    def setVolumen(self, volumen):
        self.volumen = volumen

    def getVolumen(self):
        return self.volumen

    def setCanal(self, canal):
        if 0 < canal > 121 and self.getEstado():
            self.canal = canal

    def getCanal(self):
        return self.canal

    def setNumTV(self, numTV):
        self.numTV = numTV

    def getNumTV(self):
        return self.numTV

    def turnOn(self):
        self.estado = True

    def turnOff(self):
        self.estado = False

    def getEstado(self):
        return self.estado

    def canalUp(self):
        if self.getCanal() < 120 and self.getEstado():
            self.canal += 1

    def canalDown(self):
        if self.getCanal() > 1 and self.getEstado():
            self.canal -= 1

    def volumenUp(self):
        if self.getVolumen() < 7 and self.getEstado():
            self.volumen += 1

    def volumenDown(self):
        if self.getVolumen() > 0 and self.getEstado():
            self.volumen -= 1