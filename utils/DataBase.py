import datetime

import pymongo

from models.Boleta import Boleta

from bson.objectid import ObjectId

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
    mycol= mydb["fact"]
    ret=[]
    try:
        for x in mycol.find(a):
            ret.append(x)
        return ret
    except:
        return False

movi=Boleta( None,33030, str(datetime.date.today()), 1300,  30400, 'USD')
a={'_id': ObjectId('6386c36ea1490bcf5e7199fd')}
l=[]
l.append({'user_id': movi.GetUserId(), 'fecha_bol': movi.GetFechaBol(), 'monto_Boleta': movi.GetMontoBol(), 'rol_boleta': movi.GetRolBol(), 'divisa_bol': movi.GetDivisaBole()})
insertlist("boleta",l)
print("\n")
b=get("boleta",a)
print(b)

def update(db: str, id,a: dict):
    mycol= mydb[db]
    myquery={"_id":id}
    newvalues=a
    try:
        mycol.update_one(myquery, newvalues)
        return True
    except:
        return False


    