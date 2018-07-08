import os
#dirFichero = "./ParaEntrenar/maj/SinCGmaj_reel.txt"
#dirFicheroGuardar = "./ParaEntrenar/conEspaciosMejorado/Gmaj_reel.txt"
lnueva = []
l1=[]
for base, dirs, files in os.walk('./ParaEntrenar/sinCabeza2/'):
    for nombre in files:
        dirFichero = "./ParaEntrenar/sinCabeza2/" + nombre
        dirFicheroGuardar = "./ParaEntrenar/conEspaciosMejorado/" + nombre
        with open(dirFichero, 'r') as reader:
             fichero = open(dirFicheroGuardar, 'w')
             for l in reader:
                if  (l[:2] == 'K:' or l[:2] == 'M:') and len(l) < 15:
                    for c in l:
                        if c != ' ':
                            l1.append(c)
                    fichero.write("".join(l1))
                    l1=[]

                else:
                    for caracter in l:
                        if caracter != ' ' and caracter:
                            lnueva.append(caracter)
                        else:
                            lnueva.append('=')
                    fichero.write(" ".join(lnueva))
                    lnueva=[]
        reader.close()
        fichero.close()
        print "Espacios Insertados en " + dirFicheroGuardar
print "Final del proceso"