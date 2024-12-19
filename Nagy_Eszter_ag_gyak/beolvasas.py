from Gep import Gep    
def gep_beolvas():
        adat_lista=[]
        f = open("gep.txt", "r", encoding="UTF-8")
        print(f.readline())
        szov_lista=f.readlines()
        f.close()
        i:int=0
        while(i<len(szov_lista)):
            sor=szov_lista[i].strip()
            sor_lista=sor.split("!")
            gep=Gep(sor_lista[0],sor_lista[1])
            adat_lista.append(gep)
            i+=1
        return adat_lista


