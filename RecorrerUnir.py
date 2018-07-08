import os
Estilos = os.listdir('./Estilos')
c =-1
print "Iniciando"
for base, dirs, files in os.walk('./Estilos'):
    if c != -1:
        print "ajuntando archivos de "+ Estilos[c] +"..."
        fichero = open('./Estilos/'+Estilos[c] + "_all.abc", 'w')
        for nombre in files:
            with open(base+'/'+nombre, 'r') as reader:
                for l in reader:
                    fichero.write(l)
            reader.close()
        fichero.close()
    c = c + 1
print 'Proceso finalizado con exito'