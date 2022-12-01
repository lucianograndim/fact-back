import datetime

import pymongo

from models.Boleta import Boleta

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["FactBase"]

def insertlist(db:str,Boleta: list()):
    mylist=[]
    for bol in Boleta:
        mylist.append(bol)
    mycol = mydb[db]
    print(mylist)
    try:
        mycol.insert_many(mylist)
        x=mycol.inserted_ids
        print("\n",x)
        return(True)
    except:
        print("error")
        return(False)

def get(db: str,a: dict()):
    mycol= mydb[db]
    for x in mycol.find(a):
        print(x)
movi=Boleta( None,33030, str(datetime.date.today()), 1300,  30400, 'USD')
a={'user_id': 33030, 'fecha_bol': '2022-11-30'}
l=[]
l.append({'user_id': movi.GetUserId(), 'fecha_bol': movi.GetFechaBol(), 'monto_Boleta': movi.GetMontoBol(), 'rol_boleta': movi.GetRolBol(), 'divisa_bol': movi.GetDivisaBole()})
insertlist("Boleta",l)
print("\n")
get("Boleta",a)
