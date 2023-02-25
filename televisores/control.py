from televisores.tv import TV

class Control:

    tv = TV(None, None)
    
    @classmethod
    def getTv(cls):
        return cls.tv

    @classmethod
    def turnOn(cls):
        cls.tv.turnOn()

    @classmethod
    def turnOff(cls):
        cls.tv.turnOff()

    @classmethod
    def canalUp(cls):
        cls.tv.canalUp()

    @classmethod
    def canalDown(cls):
        cls.tv.canalDown()

    @classmethod
    def volumenUp(cls):
        cls.tv.volumenUp()

    @classmethod
    def volumenDown(cls):
        cls.tv.volumenDown()

    @classmethod
    def enlazar(cls, televisor):
        cls.tv = televisor
        cls.tv.control = Control

    @classmethod
    def setCanal(cls, canal):
        cls.tv.setCanal(canal)