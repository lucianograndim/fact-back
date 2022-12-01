class Boleta:

    def __init__(self, _id, user_id, fecha_bol, monto_boleta, rol_boleta, divisa_bol):
        self._id= _id
        self.user_id= user_id
        self.fecha_bol= fecha_bol
        self.monto_Boleta= monto_boleta
        self.rol_boleta= rol_boleta
        self.divisa_bol= divisa_bol
        pass

    #Get function

    def GetId(self):
        return self._id

    def GetUserId(self):
        return self.user_id

    def GetFechaBol(self):
        return self.fecha_bol

    def GetMontoBol(self):
        return self.monto_Boleta
    
    def GetRolBol(self):
        return self.rol_boleta

    def GetDivisaBole(self):
        return self.divisa_bol

    #Set function

    def SetId(self, nId):
        self._id = nId

    def SetUserId(self, nUser):
        self.user_id = nUser

    def SetFechaBol(self, nFecha):
        self.fecha_bol = nFecha

    def SetMontoBol(self, nMonto):
        self.monto_Boleta = nMonto
    
    def SetRolBol(self, nRol):
        self.rol_boleta = nRol

    def SetDivisaBole(self, nDivisa):
        self.divisa_bol = nDivisa