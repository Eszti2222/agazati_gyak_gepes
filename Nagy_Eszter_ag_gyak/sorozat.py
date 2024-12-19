import random

def intervallum():    
    vel_szam_lista=[]
    i:int=0
    while(i<15):
        vel_szam:int=int(random.random()*590)-90
        vel_szam_lista.append(vel_szam)
        i+=1
    return vel_szam_lista

def lista_kiir(vel_szam_lista):
    print("II/A, B, C:\n")
    for i in range(0,len(vel_szam_lista), 1):
        print(f"{vel_szam_lista[i]}", end ="*")

def oszthatoak_szama(vel_szam_lista):
    i:int=0
    db:int=0
    while(i<len(vel_szam_lista)):
        if(vel_szam_lista[i]%10==0):
            db+=1
        i+=1
    return db

def konzolra_ir(db):
    print("II/D, E:\n")
    print(f"Tízzel osztható számok száma: {db}.")

def fajl_ir(db):
    f = open("kimutatas.txt", "w")
    f.write(f"Tízzel osztható számok száma: {db}.")
    f.close()
        


       