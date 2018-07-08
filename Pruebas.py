import os

dirFichero = "./ParaEntrenar/sinCabeza/three-two_all.abc"
dirFicheroGuardar = "./ParaEntrenar/Prueba.txt"
lnueva = []
with open(dirFichero, 'r') as reader:
    fichero = open(dirFicheroGuardar, 'w')
    for l in reader:
        if  (l[:2] == 'K:'):
            fichero.write(l)
        else:
            for caracter in l:
                print (caracter)
                if caracter != ' ':
                    lnueva.append(caracter)
            fichero.write(" ".join(lnueva))
            lnueva=[]
        """ else:
                fichero.write(l+'\n')

    print dirFichero + ' en ' + dirFicheroGuardar +' sin cabezera'"""
reader.close()
fichero.close()
print lnueva
lnueva = []
print lnueva
print "Espacios Insertados"

