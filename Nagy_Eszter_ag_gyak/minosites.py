def muzeum():
    print("I/A:\n")
    m_nev:str=input("Múzeum neve: ")
    lat_nev:str=input("Látogató neve: ")
    ertekeles:int=int(input(f"Értékelés(1-20): "))

    print("I/B:\n")
    if(ertekeles<=0):
        print("Az értékelés nem lehet negatív vagy 0!")
    elif(ertekeles>20):
        print("20 pont feletti értékelés nem elfogadható!")
    else:
        print("Köszönjük az értékelést!")
