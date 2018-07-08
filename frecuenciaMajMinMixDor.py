import os
import operator
fmix = 0
fmaj = 0
fmin = 0
fdor = 0
for base, dirs, files in os.walk('./ParaEntrenar/conCabeza/'):
    for nombre in files:
        data_path = './ParaEntrenar/conCabeza/'+ nombre
        with open(data_path, 'r') as f:
            data = f.read()
        tokens_set = set(data.split())
        idx2token = list(tokens_set)
        vocab_size = len(idx2token)
        frecuenciaPalab2 = [data.count(p) for p in idx2token]
        frecuenciaPalab = zip(idx2token,frecuenciaPalab2)
        frecuenciaPalab = sorted(frecuenciaPalab , key=operator.itemgetter(1), reverse = True)

        for token, freq in frecuenciaPalab:
            tokenfre= token + '\t : \t' + str(freq) + '\n'
            if str(token).find('mix') != -1:
                fmix = freq + fmix
            elif str(token).find('min') != -1:
                fmin = freq + fmin
            elif str(token).find('maj') != -1:
                fmaj = freq + fmaj
            elif str(token).find('dor') != -1:
                fdor = freq + fdor
        f.close()
        total = float(fmaj + fmin + fmix + fdor)
        pmaj= (fmaj / total) * 100
        pmin= (fmin / total) * 100
        pmix= (fmix / total) * 100
        pdor= (fdor / total) * 100
        print "\n ESTILO:"+ nombre+ "\n"
        print "Maj = "+str(fmaj)+"\t"+str(pmaj)[0:4]+"% \n"
        print "Min = "+str(fmin)+"\t"+str(pmin)[0:4]+"% \n"
        print "Dor = "+str(fdor)+"\t"+str(pdor)[0:4]+"% \n"
        print "Mix = "+str(fmix)+"\t"+str(pmix)[0:4]+"% \n"
        pmaj = 0
        pmin = 0
        pdor = 0
        pmix = 0
        fmix = 0
        fmaj = 0
        fmin = 0
        fdor = 0
print "fin"