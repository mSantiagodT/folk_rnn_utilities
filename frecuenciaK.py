import os
import operator

for base, dirs, files in os.walk('./ParaEntrenar/mix/'):
    for nombre in files:
        data_path = './ParaEntrenar/mix/'+ nombre
        data_save = './ParaEntrenar/mix/FQ'+ nombre
        with open(data_path, 'r') as f:
            data = f.read()
        tokens_set = set(data.split())
        idx2token = list(tokens_set)
        vocab_size = len(idx2token)

        print 'vocabulary size: ' + str(vocab_size) + ' de ' + nombre

        frecuenciaPalab2 = [data.count(p) for p in idx2token]
        frecuenciaPalab = zip(idx2token,frecuenciaPalab2)
        frecuenciaPalab = sorted(frecuenciaPalab , key=operator.itemgetter(1), reverse = True)
        fichero = open(data_save, 'w')
        fichero.write('vocabulary size:' + str(vocab_size) + '\n\n')

        for token, freq in frecuenciaPalab:
            tokenfre= token + '\t : \t' + str(freq) + '\n'
            if str(token).find('mix') != -1:
                fichero.write(tokenfre)
        fichero.close()
        f.close()
