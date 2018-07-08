import os

#dirFichero = "./ParaEntrenar/sinCabeza/three-two_all.abc"
#dirFicheroGuardar = "./ParaEntrenar/Prueba.txt"
lnueva = []
#for base, dirs, files in os.walk('./ParaEntrenar/sinCabeza/'):
#    for nombre in files:
dirFichero = "./ParaEntrenar/conEspaciosMejorado/jig_all.abc"
dirFicheroGuardar = "./ParaEntrenar/Prueba.txt"
with open(dirFichero, 'r') as reader:
     fichero = open(dirFicheroGuardar, 'w')
     for l in reader:
        if  (l[:2] == 'K:' or l[:2] == 'M:'):
            l1 =l[:2]+l[2:]
            fichero.write(l1)
        else:
            for caracter in l:
                if caracter != ' ' and caracter != '=':
                    lnueva.append(caracter)
                elif caracter == "=":
                    lnueva.append(' ')
            fichero.write("".join(lnueva))
            lnueva=[]
reader.close()
fichero.close()
print "Espacios Insertados en " + dirFicheroGuardar
print "Final del proceso"