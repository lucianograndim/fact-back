class Discrepancia:
    
    def __init__(self, _id, user_id, fecha_dis, estado_dis, tipo_dis):
        self._id= _id
        self.user_id= user_id
        self.fecha_dis= fecha_dis
        self.estado_dis= estado_dis
        self.tipo_dis= tipo_dis
        pass

    #Get function

    def GetId(self):
        return self._id
    
    def GetUsuerId(self):
        return self.user_id

    def GetFechaDis(self):
        return self.fecha_dis

    def GetEstadoDs(self):
        return self.estado_dis

    def GetTipoDis(self):
        return self.tipo_dis

    #Set function

    def SetId(self, nId):
        self._id = nId
    
    def SetUsuerId(self, nUser):
        self.user_id = nUser

    def SetFechaDis(self, nFecha):
        self.fecha_dis = nFecha

    def SetEstadoDs(self, nEstado):
        self.estado_dis = nEstado

    def SetTipoDis(self, nTipo):
        self.tipo_dis = nTipo