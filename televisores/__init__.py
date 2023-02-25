# class Marca:
#     def __init__(self, nombre):
#         self.nombre = nombre
#
#     def setNombre(self, nombre):
#         self.nombre = nombre
#     def getNombre(self):
#         return self.nombre


# class TV:
#
#     canal = 1
#     volumen = 1
#     precio = 500
#     control = None
#     numTV = int
#
#     def __init__(self, marca, estado):
#         self.marca = marca
#         self.estado = estado
#         self.numTV += 1
#
#     def setMarca(self, marca):
#         self.marca = marca
#
#     def getMarca(self):
#         return self.marca
#
#     def setControl(self, control):
#         self.control = control
#
#     def getControl(self):
#         return self.control
#
#     def setPrecio(self, precio):
#         self.precio = precio
#
#     def getPrecio(self):
#         return self.precio
#
#     def setVolumen(self, volumen):
#         self.volumen = volumen
#
#     def getVolumen(self):
#         return self.volumen
#
#     def setCanal(self, canal):
#         self.canal = canal
#
#     def getCanal(self):
#         return self.canal
#
#     def setNumTV(self, num):
#         self.numTV = num
#
#     def getNumTV(self):
#         return self.numTV
#
#     def turnOn(self):
#         self.estado = True
#
#     def turnOff(self):
#         self.estado = False
#
#     def getEstado(self):
#         return self.estado
#
#     def canalUp(self):
#         if self.getCanal() < 120 and self.getEstado():
#             self.canal += 1
#
#     def canalDown(self, canal):
#         if self.getCanal() > 1 and self.getEstado():
#             self.canal -= 1
#
#     def volumenUp(self):
#         if self.getVolumen() < 7 and self.getEstado():
#             self.volumen += 1
#
#     def volumenDown(self):
#         if self.getVolumen() > 0 and self.getEstado():
#             self.volumen -= 1


# class Control:
#
#     def __init__(self):
#         self.tv = TV
#
#     def turnOn(self):
#         self.tv.turnOn()
#
#     def turnOff(self):
#         self.tv.turnOff()
#
#     def canalUp(self):
#         self.tv.canalUp()
#
#     def canalDown(self, canal):
#         self.tv.canalDown(canal)
#
#     def volumenUp(self):
#         self.tv.volumenUp()
#
#     def volumenDown(self):
#         self.tv.volumenDown()
#
#     def enlazar(self, televisor):
#         self.tv = televisor
#         self.tv.control = Control









