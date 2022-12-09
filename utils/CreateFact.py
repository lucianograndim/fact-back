from models.Empresa import Empresa
from models.Movimiento import Movimiento
from datetime import datetime, timezone
from datetime import timedelta
from bson.objectid import ObjectId
from utils.DataBase import *
from utils.pdf import PDF
valor_slm=12
valor_sms=30
valor_wsp=24
valor_hora=54

#con este sacas el total de movimientos
#end y strat en formato iso
def totalmoviento(id: str,end,start):
    from_date = datetime.strptime(start, '%Y-%m-%d')
    to_date = datetime.strptime(end, '%Y-%m-%d')
    a={'idEmpresa': id, 'fechaUP': {'$lt': to_date, '$gte': from_date}}
    ret=get("movimiento",a)
    total_slm=0
    total_sms=0
    total_wsp=0
    total_hora=0
    for a in ret:
        print(a,"\n")
        total_slm=total_slm+a["minutos_SLM_usados"]
        total_sms=total_sms+a["SMS_usados"]
        total_wsp=total_wsp+a["msje_wsp_usados"]
        total_hora=total_hora+a["horas_agente_usada"]
    total_slm=total_slm*valor_slm
    total_sms=total_sms*valor_sms
    total_wsp=total_wsp*valor_wsp
    total_hora=total_hora*valor_hora
    totalmovimiento=Movimiento(0,0,total_slm,total_sms,total_wsp,total_hora,0,0)
    return totalmoviento


def calcular_fact( empresa: Empresa,movimiento: Movimiento):
    pdf=PDF(orientation='P', unit='mm', format='Letter')
    pdf.add_page()
    pdf.lines()
    pdf.imagex()
    pdf.titles()
    pdf.ln(50)
    print(movimiento.GetMinutos()*valor_slm)
    header=("Razon social","Rut","Representante")
    dataenterprise=(("Razon social",empresa.Getnombre()),
                    ("Rut",empresa.GetRut()),
                    ("Representante",empresa.GetRepres()))
    pdf.set_text_color(0, 0, 0)
    pdf.set_font("Times", size=10)
    line_height = pdf.font_size * 2.5
    col_width = pdf.epw / 4  # distribute content 
    r=160
    b=160
    g=160
    for row in dataenterprise:
        for datum in row:
            if(row.index(datum)==0):
                pdf.set_fill_color(r,b,g)
            else:
                pdf.set_fill_color(r+40,b+40,g+40)
            pdf.multi_cell(col_width, line_height, datum, border=1,fill=True,
                new_x="RIGHT", new_y="TOP", max_line_height=pdf.font_size)
        pdf.ln(line_height)
    line_height=line_height+10.0
    pdf.ln(line_height)
    total=movimiento.GetMinutos()*valor_slm+movimiento.GetSMS()*valor_sms+movimiento.GetMsje()*valor_wsp+movimiento.GetHoras()+valor_hora
    datamovements=(("Servicio","Monto"),
                   ("Minutos SLM",str(movimiento.GetMinutos()*valor_slm)),
                   ("SMS",str(movimiento.GetSMS()+valor_sms)),
                   ("Mensajes WhatsAPP",str(movimiento.GetMsje()*valor_wsp)),
                   ("Horas de Agente",str(movimiento.GetHoras()*valor_hora)),
                   ("Total",str(total)))
    col_width = pdf.epw / 2
    for row in datamovements:
        for datum in row:
            if(datamovements.index(row)==0):
                pdf.set_fill_color(0,255,128)
                if(row.index(datum)==1):
                    al="R"
                    borde=["R","T","B"]
                else:
                    al="L"
                    borde=["L","T","B"]
                pdf.multi_cell(col_width, line_height/2, datum, border=borde,align=al,fill=True,
                new_x="RIGHT", new_y="TOP", max_line_height=pdf.font_size)
            else:
                if(row.index(datum)==1):
                    pdf.set_fill_color(102,255,178)
                    pdf.multi_cell(col_width, line_height, datum, border=["R","T","B"],align="R",fill=True,
                    new_x="RIGHT", new_y="TOP", max_line_height=pdf.font_size)
                else:
                    pdf.set_fill_color(153,255,204)
                    pdf.multi_cell(col_width, line_height, datum, border=["L","T","B"],align="L",fill=True,
                    new_x="RIGHT", new_y="TOP", max_line_height=pdf.font_size)
        if(datamovements.index(row)==0):
            pdf.ln(line_height/2)
        else:
            pdf.ln(line_height)
    date=datetime.date.today()
    title="Alloxentric-"+str(empresa.Getnombre())+"-"+str(date)
    print("1",empresa.Getnombre())
    pdf.output(title+".pdf")
    

list=[]
dic={"idEmpresa":"2231231","minutos_SLM_usados":20,"SMS_usados":10,"msje_wsp_usados":15,"horas_agente_usada":40,"fechaUP":datetime.strptime("2022-09-22", '%Y-%m-%d').isoformat()}
list.append(dic)
dic={"idEmpresa":"2231231","minutos_SLM_usados":20,"SMS_usados":10,"msje_wsp_usados":15,"horas_agente_usada":40,"fechaUP":datetime.strptime("2022-09-25", '%Y-%m-%d').isoformat()}
list.append(dic)
dic={"idEmpresa":"2231231","minutos_SLM_usados":20,"SMS_usados":10,"msje_wsp_usados":15,"horas_agente_usada":40,"fechaUP":datetime.strptime("2022-10-15", '%Y-%m-%d').isoformat()}
list.append(dic)
dic={"idEmpresa":"2231231","minutos_SLM_usados":20,"SMS_usados":10,"msje_wsp_usados":15,"horas_agente_usada":40,"fechaUP":datetime.strptime("2022-11-01", '%Y-%m-%d').isoformat()}
list.append(dic)
dic={"idEmpresa":"2231231","minutos_SLM_usados":20,"SMS_usados":10,"msje_wsp_usados":15,"horas_agente_usada":40,"fechaUP":datetime.strptime("2022-11-15", '%Y-%m-%d').isoformat()}
list.append(dic)
insertlist("movimiento")
empr= Empresa(str(2231231),"corfo","12345678-9","portugal 123","chile","humberto velez")
m=totalmoviento(2231231,datetime.strptime("2022-09-22", '%Y-%m-%d'),datetime.strptime("2022-11-20", '%Y-%m-%d'))
calcular_fact(Empresa(2231231,"corfo","12345678-9","portugal 123","chile","humberto velez"),m)



    # datamovements=(("Minutos SLM",movimiento.GetMinutos()*valor_slm),
    #                ("SMS",movimiento.GetSMS()+valor_sms),
    #                ("Mensajes WhatsAPP",movimiento.GetMsje()+valor_wsp),
    #                ("Horas de Agente",movimiento.GetHoras()+valor_hora))