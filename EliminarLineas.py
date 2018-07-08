import os

#dirFichero = "Download/musica1.abc"
#dirFicheroGuardar = 'LineasEliminadas.abc'
# dirFichero = "./ParaEntrenar/maj/Gmaj_reel.txt"
# dirFicheroGuardar = "./ParaEntrenar/maj/SinCGmaj_reel.txt"

for base, dirs, files in os.walk('./ParaEntrenar/conCabeza/'):
    for nombre in files:
        dirFichero = "./ParaEntrenar/conCabeza/" + nombre
        dirFicheroGuardar = "./ParaEntrenar/sinCabeza2/" + nombre
        #dirFicheroGuardar = "./ParaEntrenar/sinCabeza/" + nombre

        with open(dirFichero, 'r') as reader:
            fichero = open(dirFicheroGuardar, 'w')
            for l in reader:
                if  (l[:2] == 'K:' or l[:2] == 'M:'):
                    fichero.write(l)
                elif (l[:2] != 'X:' and l[:2] != 'T:' and l[:2] != 'Z:' and l[:2] != 'S:' and l[:2] != 'R:' and l[:2] != 'L:'): #and l[:2] != 'K:'  and l[:2] != 'M:'):
                    if l[:2] != '\n':
                        p=l.rstrip('\n')
                        p= p.replace('\r'," ")
                        fichero.write(p)
                    else:
                        fichero.write(l+'\n')

            print dirFichero + ' en ' + dirFicheroGuardar +' sin cabezera2'
        reader.close()
        fichero.close()
print "Cabezeras eliminadas"

