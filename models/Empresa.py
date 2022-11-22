class Empresa:

    def __init__(self, _id, nombre, rut, direccion, pais, representante_legal):
        self._id: _id
        self.nombre: nombre
        self.rut: rut
        self.direccion: direccion
        self.pais: pais
        self.representante_legal: representante_legal

    #Get function

    def GetId(self):
        return self._id

    def Getnombre(self):
        return self.nombre

    def GetRut(self):
        return self.rut

    def GetDireccion(self):
        return self.direccion
    
    def GetPais(self):
        return self.pais
    
    def GetRepres(self):
        return self.representante_legal

    #Set function

    def SetId(self, nId):
        self._id = nId

    def Setnombre(self, nNombre):
        self.nombre = nNombre

    def SetRut(self, nRut):
        self.rut = nRut

    def SetDireccion(self, nDireccion):
        self.direccion = nDireccion
    
    def SetPais(self, nPais):
        self.pais = nPais
    
    def SetRepres(self, nRepres):
        self.representante_legal = nRepres

    