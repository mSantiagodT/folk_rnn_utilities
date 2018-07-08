import urllib2
import time
limiteSuperior = 18000
contador = 1
fallo = 0
tiempo_total = 0
while True:
    archivoDescargar = "https://thesession.org/tunes/"+ str(contador) +"/abc"
    archivoGuardar = "Download/musica"+str(contador)+".abc"
    now = time.time()
    try:
        descarga = urllib2.urlopen(archivoDescargar)
        ficheroGuardar = file(archivoGuardar, "w")
        ficheroGuardar.write(descarga.read())
        ficheroGuardar.close()
        elapsed = time.time() - now
        tiempo_total = tiempo_total + elapsed
        print "Descargado el archivo: %s en %0.3fs" % (archivoDescargar, elapsed)
        fallo = 0
    except:
        print "URL no valida"
        fallo = fallo + 1
        if contador > limiteSuperior or fallo > 10:
            break
    contador += 1
print str(tiempo_total)+"s Tiempo total FIN"