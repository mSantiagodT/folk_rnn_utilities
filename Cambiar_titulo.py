import glob
lista_error=[]
elementos = len(glob.glob('./Download/*'))
for x in range(elementos):
    dirFichero = './Download/musica' + str(x + 1) + '.abc'
    try:
        with open(dirFichero, 'r') as reader:
             reader.readline()
             titulo = reader.readline()[3:]
             reader.readline()
             reader.readline()
             estilo =  reader.readline()[3:]
             reader.close()
             estilo =estilo[:-2]
             titulo = titulo[:-2]
    except:
        estilo = ''
        lista_error.append(dirFichero)
    if (estilo != ''):
        dirFicheroGuardar = './Estilos/'+estilo+'/' +titulo
        try:
            with open(dirFichero, 'r') as reader:
                fichero = open(dirFicheroGuardar, 'w')
                for l in reader:
                    fichero.write(l)
                print dirFichero + ' en ' + dirFicheroGuardar
        except:
            lista_error.append(dirFichero)
        print str(x) + "/" + str(elementos)

print 'ficheros no guardados correctamente:'
print len(lista_error)
print lista_error
print 'FIN'

