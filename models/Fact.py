class Fact:
    
    def __init__(self,_Id, emprasa_id, tipo, fecha_fact, deposito, estado_fac, divisa_fact, documento, url):
        self._id: _Id
        self.empresa_id: emprasa_id
        self.tipo: tipo
        self.fecha_fac: fecha_fact
        self.deposito: deposito
        self.estado_fac: estado_fac
        self.divisa_fac: divisa_fact
        self.documento: documento
        self.url: url

    #Get function
    
    def GetId(self):
        return self._id

    def GetEmpresaId(self):
        return self.empresa_id

    def GetTipo(self):
        return self.tipo

    def GetFechaFac(self):
        return self.fecha_fac

    def GetDeposito(self):
        return self.deposito
    
    def GetEstadoFac(self):
        return self.estado_fac

    def GetDivisaFac(self):
        return self.divisa_fac

    def GetDocumento(self):
        return self.documento

    def GetUrl(self):
        return self.url

    #Set function

    def SetId(self, nId):
        self._id = nId

    def SetEmpresaId(self, nEmpresaId):
        self.empresa_id = nEmpresaId

    def SetTipo(self, nTipo):
        self.tipo = nTipo

    def SetFechaFac(self, nFechaFac):
        self.fecha_fac = nFechaFac

    def SetDeposito(self, nDeposito):
        self.deposito = nDeposito
    
    def SetEstadoFac(self, nEstadoFac):
        self.estado_fac = nEstadoFac

    def SetDivisaFac(self, nDivisaFac):
        self.divisa_fac = nDivisaFac

    def SetDocumento(self, nDocumento):
        self.documento = nDocumento

    def SetUrl(self, nUrl):
        self.url = nUrl