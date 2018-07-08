dirFichero = "./ParaEntrenar/maj/Gmaj_polka.txt"
dirFicheroGuardar = "./ParaEntrenar/maj/SinCGmaj_polka.txt"
with open(dirFichero, 'r') as reader:
    fichero = open(dirFicheroGuardar, 'w')
    for l in reader:
        if (l[:2] != 'X:' and l[:2] != 'T:' and l[:2] != 'Z:' and l[:2] != 'S:' and l[:2] != 'R:' and l[:2] != 'L:' and l[:2] != 'K:'  and l[:2] != 'M:'):
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

dirFichero = "./ParaEntrenar/maj/SinCGmaj_polka.txt"
dirFicheroGuardar = "./ParaEntrenar/conEspaciosMejorado/Gmaj_polka.txt"
lnueva = []
l1=[]
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
print "Con espacios M"