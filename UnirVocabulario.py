import os
from itertools import izip
data = ''
for base, dirs, files in os.walk('./ParaEntrenar/conEspaciosMejorado/'):
    for nombre in files:
        dirFichero = "./ParaEntrenar/conEspaciosMejorado/" + nombre
        with open(dirFichero, 'r') as f:
            data = data + f.read()

    tokens_set = set(data.split())
    start_symbol, end_symbol = '<s>', '</s>'
    tokens_set.update({start_symbol, end_symbol})

    idx2token = list(tokens_set)
vocab_size = len(idx2token)
print 'vocabulary size:', vocab_size
token2idx = dict(izip(idx2token, xrange(vocab_size)))
print token2idx


