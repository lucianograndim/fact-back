class OrdenCompra:
    
    def __init__(self, _id, user_id, monto_oc, fecha_oc):
        self._id= _id
        self.user_id= user_id
        self.monto_oc= monto_oc
        self.fecha_oc= fecha_oc
        pass
    #Get function

    def GetId(self):
        return self._id

    def GetUserId(self):
        return self.user_id

    def GetMontoOc(self):
        return self.monto_oc

    def GetFechaOc(self):
        return self.fecha_oc

    #set function

    def SetId(self, nId):
        self._id = nId
    
    def SetUserId(self, nUserId):
        self.user_id = nUserId

    def SetMontoOc(self, nMontoOc):
        self.monto_oc = nMontoOc

    def SetFechaOc(self, nFechaOc):
        self.fecha_oc = nFechaOc