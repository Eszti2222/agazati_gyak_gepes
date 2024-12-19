from Gep import Gep
def gepek_db(adat_lista):
    i:int=0
    gepek_db:int=0
    while(i<len(adat_lista)):
        gepek_db+=1
        i+=1
    return gepek_db

def gepek_szama(gepek_db):
    print("III/A, B:")
    print(f"A gépek száma: {gepek_db}.")

def atlag(gep,adat_lista):
    print("III/C:")
    i:int=0
    db:int=0
    azon:int=0
    while(i<len(adat_lista)):
        if(gep.hely %2==0):
            db+=1
            azon+=gep.id
        i+=1
    atlag=azon/db
    print(f"A páros teremszámú termek azonosító átlaga: {atlag}.")

def legkisebb(gep,adat_lista):
    i:int=0
    legkisebb_id:int=75
    min_index=0
    while(i<len(adat_lista)):
        if(gep.tipus=="asztali"):
            if(gep.id<legkisebb_id):
                legkisebb_id=gep.id
                min_index=i
        i+=1
    return min_index





