class Ticket:

    def __init__(self, _id, nombre, email, telefono, tipo_telf, pais, asunto, mensaje):
        self._id= _id
        self.nombre= nombre
        self.email= email
        self.telefono= telefono
        self.tipo_telf= tipo_telf
        self.pais= pais
        self.asunto= asunto
        self.mensaje= mensaje
        pass
    
    #Get function

    def GetId(self):
        return self._id

    def GetNombre(self):
        return self.nombre

    def GetEmail(self):
        return self.email

    def GetTelefono(self):
        return self.telefono

    def GetTipoTelf(self):
        return self.tipo_telf

    def GetPais(self):
        return self.pais

    def GetAsunto(self):
        return self.asunto

    def GetMensaje(self):
        return self.mensaje

    #Set function

    def SetId(self, nId):
        self._id = nId

    def SetNombre(self, nNombre):
        self.nombre = nNombre

    def SetEmail(self, nEmail):
        self.email = nEmail

    def SetTelefono(self, nTelefono):
        self.telefono = nTelefono

    def SetTipoTelf(self, nTipoTelf):
        self.tipo_telf = nTipoTelf

    def SetPais(self, nPais):
        self.pais = nPais

    def SetAsunto(self, nAsunto):
        self.asunto = nAsunto

    def SetMensaje(self, nMensaje):
        self.mensaje = nMensaje