
dirFichero = "./ParaEntrenar/maj/SinCGmaj_reel.txt"
dirFicheroGuardar = "./ParaEntrenar/conEspaciosMejorado/Gmaj_reel2.txt"
nc = 0
cadena = ""
lnueva = []
with open(dirFichero, 'r') as reader:
     fichero = open(dirFicheroGuardar, 'w')
     for l in reader:
        for caracter in l:
            if caracter != ' ' and caracter:
                lnueva.append(caracter)
            else:
                lnueva.append('=')
     Todo = ("".join(lnueva))
     lnueva = []
     for caracter2 in Todo:
        if caracter2 == '\n':
            fichero.write('\n')
            nc = -1
        if nc < 2 and caracter2 !='\n':
            fichero.write(caracter2)
        if nc == 2 and caracter2 !='\n':
            fichero.write(" ")
            fichero.write(caracter2)
            nc = 0
        nc = nc + 1
reader.close()
fichero.close()
print "Con espacios M"