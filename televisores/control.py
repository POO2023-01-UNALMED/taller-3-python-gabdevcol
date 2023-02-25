
class Control:

    def __init__(self):
        self.tv = self.__class__
    def getTv(self):
        return self.tv

    def turnOn(self):
        self.tv.turnOn()

    def turnOff(self):
        self.tv.turnOff()

    def canalUp(self):
        self.tv.canalUp()

    def canalDown(self, canal):
        self.tv.canalDown(self, canal)

    def volumenUp(self):
        self.tv.volumenUp()

    def volumenDown(self):
        self.tv.volumenDown()

    def enlazar(self, televisor):
        self.tv = televisor
        self.tv.control = Control

    def setCanal(self, canal):
        self.tv.setCanal(canal)