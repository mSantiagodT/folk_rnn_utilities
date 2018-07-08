import os
import operator
data_path = '../MusicaCreada/frp.txt'
data_save = '../MusicaCreada/FQfrp.txt'
total = 0.0
with open(data_path, 'r') as f:
    data = f.read()
tokens_set = set(data.split())
idx2token = list(tokens_set)
vocab_size = len(idx2token)

print 'vocabulary size: ' + str(vocab_size)
for p in idx2token:
    total = total + data.count(p)
frecuenciaPalab2 = [data.count(p) for p in idx2token]
frecuenciaPalab = zip(idx2token,frecuenciaPalab2)
frecuenciaPalab = sorted(frecuenciaPalab , key=operator.itemgetter(1), reverse = True)
print total
fichero = open(data_save, 'w')
fichero.write('vocabulary size:' + str(vocab_size) + '\n')
fichero.write('caracteres totales:'+ str(total) + '\n\n')
for token, freq in frecuenciaPalab:
    porcentaje = ((freq/total) * 100)
    tokenfre= token + '\t : \t' + str(freq) + '\t' + str(porcentaje)+ '\n'
    fichero.write(tokenfre)
fichero.close()
f.close()