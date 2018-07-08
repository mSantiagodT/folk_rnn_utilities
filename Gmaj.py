import os
rec = False
cD = 0
cE = 0
cF = 0
cA = 0
cC = 0
cG = 0
c = 0
recD = False
recE = False
recF = False
recA = False
recC = False
recG = False
dirFichero = "./ParaEntrenar/maj/Maj_polka_all.abc"
dirFicheroGuardarD = "./ParaEntrenar/maj/Dmaj_polka"
dirFicheroGuardarA = "./ParaEntrenar/maj/Amaj_polka"
dirFicheroGuardarC = "./ParaEntrenar/maj/Cmaj_polka"
dirFicheroGuardarF = "./ParaEntrenar/maj/Fmaj_polka"
dirFicheroGuardarE = "./ParaEntrenar/maj/Emaj_polka"
dirFicheroGuardarG = "./ParaEntrenar/maj/Gmaj_polka.txt"

with open(dirFichero, 'r') as reader:
    ficheroD = open(dirFicheroGuardarD, 'w')
    ficheroA = open(dirFicheroGuardarA, 'w')
    ficheroC = open(dirFicheroGuardarC, 'w')
    ficheroF = open(dirFicheroGuardarF, 'w')
    ficheroE = open(dirFicheroGuardarE, 'w')
    ficheroG = open(dirFicheroGuardarG, 'w')
    for l in reader:
        if  (l.find('K:') != -1 and l.find('Dmaj') != -1): ###DDDDDDDD
            ficheroD.write('X:'+ str(c) + '\n')
            ficheroD.write(l)
            #cD += 1
            c += 1
            recD = True;
        elif (recD == True and l.find('K:') == -1):
            ficheroD.write(l)


        if (l.find('K:') != -1 and l.find('Amaj') != -1): ####AAAAAAAAAA
            ficheroA.write('X:' + str(c) + '\n')
            ficheroA.write(l)
            #cA += 1
            c += 1
            recA = True;
        elif (recA == True and l.find('K:') == -1):
            ficheroA.write(l)

        if (l.find('K:') != -1 and l.find('Cmaj') != -1): ####CCCCCCCC
            ficheroC.write('X:' + str(c) + '\n')
            ficheroC.write(l)
            #cC += 1
            c += 1
            recC = True;
        elif (recC == True and l.find('K:') == -1):
            ficheroC.write(l)

        if (l.find('K:') != -1 and l.find('Fmaj') != -1): ####FFFFF
            ficheroF.write('X:' + str(c)+ '\n')
            ficheroF.write(l)
            #cF += 1
            c += 1
            recF = True;
        elif (recF == True and l.find('K:') == -1):
            ficheroF.write(l)

        if (l.find('K:') != -1 and l.find('Emaj') != -1): ####EEE
            ficheroE.write('X:' + str(c) + '\n')
            ficheroE.write(l)
            #cE += 1
            c += 1
            recE = True;
        elif (recE == True and l.find('K:') == -1):
            ficheroE.write(l)

        if (l.find('K:') != -1 and l.find('Gmaj') != -1):  ###GGG
            ficheroG.write('X:' + str(c) + '\n')
            ficheroG.write(l)
            #cG += 1
            c += 1
            recG = True;
        elif (recG == True and l.find('K:') == -1):
            ficheroG.write(l)

        if l == '\n':
            recD = False
            recE = False
            recF = False
            recA = False
            recC = False
            recG = False

    print dirFichero + ' en ----- Solo maj'
reader.close()
ficheroD.close()
ficheroA.close()
ficheroC.close()
ficheroF.close()
ficheroE.close()
ficheroG.close()

os.system('abc2abc '+ dirFicheroGuardarD +' -t 5 -e >>'+ dirFicheroGuardarG)
os.system('abc2abc '+ dirFicheroGuardarA +' -t -2 -e >>'+ dirFicheroGuardarG)
os.system('abc2abc '+ dirFicheroGuardarC +' -t 7 -e >>'+ dirFicheroGuardarG)
os.system('abc2abc '+ dirFicheroGuardarF +' -t 2 -e >>'+ dirFicheroGuardarG)
os.system('abc2abc '+ dirFicheroGuardarE +' -t 3 -e >>'+ dirFicheroGuardarG)

os.remove(dirFicheroGuardarD)
os.remove(dirFicheroGuardarA)
os.remove(dirFicheroGuardarC)
os.remove(dirFicheroGuardarF)
os.remove(dirFicheroGuardarE)

print "maj creado"