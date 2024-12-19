import minosites
import sorozat
from Gep import Gep
import helyzet
import beolvasas

#minosites.muzeum()

sorozat.lista_kiir(vel_szam_lista=sorozat.intervallum())

sorozat.konzolra_ir(db=sorozat.oszthatoak_szama(vel_szam_lista=sorozat.intervallum()))

sorozat.fajl_ir(db=sorozat.oszthatoak_szama(vel_szam_lista=sorozat.intervallum()))

beolvasas.gep_beolvas()
helyzet.gepek_db(adat_lista=beolvasas.gep_beolvas())
helyzet.gepek_szama(helyzet.gepek_db(adat_lista=beolvasas.gep_beolvas()))
helyzet.atlag()

