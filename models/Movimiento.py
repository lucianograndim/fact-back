class movimiento:
    
    def __init__(self, _id, user_id, minutos_SLM_usados, SMS_usados, msje_wsp_usados, horas_agente_usada, puntos_premios_agente):
        self._id: _id
        self.user_id: user_id
        self.minutos_SLM_usados: minutos_SLM_usados
        self.SMS_usados: SMS_usados
        self.msje_wsp_usados: msje_wsp_usados
        self.horas_agente_usadas: horas_agente_usada
        self.puntos_premio_agente: puntos_premios_agente

    #Get function
    
    def GetId(self):
        return self._id

    def GetUserId(self):
        return self.user_id

    def GetMinutos(self):
        return self.minutos_SLM_usados

    def GetSMS(self):
        return self.SMS_usados

    def GetMsje(self):
        return self.msje_wsp_usados

    def GetHoras(self):
        return self.horas_agente_usadas

    def GetPuntos(self):
        return self.puntos_premio_agente

    #Set function

    def SetId(self, nId):
        self._id = nId

    def SetUserId(self, nUser):
         self.user_id = nUser

    def SetMinutos(self, nMin):
         self.minutos_SLM_usados = nMin

    def SetSMS(self, nSMS):
         self.SMS_usados = nSMS

    def SetMsje(self, nMsje):
         self.msje_wsp_usados = nMsje

    def SetHoras(self, nHoras):
         self.horas_agente_usadas = nHoras

    def SetPuntos(self, nPuntos):
         self.puntos_premio_agente = nPuntos