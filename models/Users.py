class users:
    
    def __init__(self , _id, usuario, password, salt, rol, nombre,  razon_social, email, fecha_nac, telefono, direccion, empresa_id, pais, celular, puntos_kap):
        self._id: _id
        self.usuario: usuario
        self.password: password
        self.salt: salt
        self.rol: rol
        self.nombre: nombre
        self.razon_social: razon_social
        self.email: email
        self.fecha_nac: fecha_nac
        self.telefono: telefono
        self.direccion: direccion
        self.empresa_id: empresa_id
        self.pais: pais
        self.celular: celular
        self.puntos_kap: puntos_kap
        pass
    #Get functions

    def GetId(self):
        return self._id
    
    def GetUsuario(self):
        return self.usuario

    def GetPasssword(self):
        return self.password

    def GetSalt(self):
        return self.salt

    def GetRol(self):
        return self.rol

    def GetNombre(self):
        return self.nombre

    def GetRazonSocial(self):
        return self.razon_social

    def GetEmail(self):
        return self.email

    def GetFechaNac(self):
        return self.fecha_nac
    
    def GetTelefono(self):
        return self.telefono
    
    def GetDireccion(self):
        return self.direccion

    def GetEmpresaId(self):
        return self.empresa_id

    def GetPais(self):
        return self.pais

    def GetCelular(self):
        return self.celular

    def GetPuntosKap(self):
        return self.puntos_kap

    #Set functions

    def SetId(self,nId):
        self._id = nId
    
    def SetUsuario(self, nUsuario):
        self.usuario = nUsuario

    def SetPasssword(self, nPassword):
        self.password = nPassword

    def SetSalt(self, nSalt):
        self.salt = nSalt

    def SetRol(self, nRol):
        self.rol = nRol

    def SetNombre(self, nNombre):
        self.nombre = nNombre

    def SetRazonSocial(self, nRazonSocial):
        self.razon_social = nRazonSocial

    def SetEmail(self, nEmail):
        self.email = nEmail

    def SetFechaNac(self, nFechNac):
        self.fecha_nac = nFechNac
    
    def SetTelefono(self, nTelefono):
        self.telefono = nTelefono
    
    def SetDireccion(self, nDireccion):
        self.direccion = nDireccion

    def SetEmpresaId(self, nEMpresaId):
        self.empresa_id = nEMpresaId

    def SetPais(self, nPais):
        self.pais = nPais

    def SetCelular(self, nCelular):
        self.celular = nCelular

    def SetPuntosKap(self, nPuntosKap):
        self.puntos_kap = nPuntosKap