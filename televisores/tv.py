from televisores.control import Control

class TV:

    canal = int()
    volumen = int()
    precio = int()
    control = Control()
    numTV = int()

    def __init__(self, marca, estado):
        self.marca = marca
        self.estado = estado
        TV.numTV += 1
        self.canal = 1
        self.volumen = 1
        self.precio = 500


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
        if -1 < volumen < 8 and self.getEstado():
            self.volumen = volumen

    def getVolumen(self):
        return self.volumen

    def setCanal(self, canal):
        if 0 < canal < 121 and self.getEstado():
            self.canal = canal

    def getCanal(self):
        return self.canal

    @classmethod
    def setNumTV(cls, num):
        cls.numTV = num

    @classmethod
    def getNumTV(cls):
        return cls.numTV

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


if __name__ == "__main__":

    from televisores.tv import TV
    from televisores.control import Control
    from televisores.marca import Marca



    TV.setNumTV(0)
    marca = Marca("Semsung")

    tv1 = TV(marca, True)
    tv2 = TV(marca, True)
    tv3 = TV(marca, True)

    print(TV.getNumTV() == 3)


    def testConstructorMarca():

        TV.setNumTV(0)

        marca = Marca("Semsung")

        print(marca.getNombre() == "Semsung")


    def testConstructorTV():
        TV.setNumTV(0)
        marca = Marca("Xiomi")
        tv1 = TV(marca, True)
        ok = False

        if (tv1.getMarca().getNombre() == "Xiomi" and tv1.getEstado()):
            ok = True

        print(ok)


    def testValoresDefecto():

        marca = Marca("Xiomi")

        tv1 = TV(marca, True)

        ok = False
        if (tv1.getPrecio() == 500 and tv1.getCanal() == 1 and tv1.getVolumen() == 1):
            ok = True
        print(ok)


    # print(testContador())