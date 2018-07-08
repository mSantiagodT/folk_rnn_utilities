import os

rec = False
for base, dirs, files in os.walk('./ParaEntrenar/conCabeza/'):
    for nombre in files:
        dirFichero = "./ParaEntrenar/conCabeza/" + nombre
        dirFicheroGuardar = "./ParaEntrenar/dor/Dor_" + nombre
        with open(dirFichero, 'r') as reader:
            fichero = open(dirFicheroGuardar, 'w')
            for l in reader:
                if  (l.find('K:') != -1 and l.find('dor') != -1):
                    fichero.write(l)
                    rec = True;
                elif (rec == True and l.find('K:') == -1):
                    fichero.write(l)
                if l == '\n':
                    rec = False;

            print dirFichero + ' en ' + dirFicheroGuardar +'Solodor'
        reader.close()
        fichero.close()
print "dor creado"