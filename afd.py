# coding: utf-8
import sys

'''
Modo de uso: 

O programa deve rodar via linha de comandos (shell) como: python afd.py afd.txt "cadeia"

A tabela do AFD no arquivo deve conter uma transição por linha na forma:
qx s qx
significando δ(q,s)=p

A primeira linha tem o estado inicial. 
A segunda linha tem o(os) estado(os) final(is)
A demais linhas contem as transicoes.

qx representa o estado, sendo necessário ser informado inicialmente com a letra q seguida do símbolo que representa o estado.
    Exemplo: q0 => representa o estado zero
''' 

tabelaCMD = sys.argv[1]

cadeiaCMD = sys.argv[2]
entrada = []
for posicaoEntrada in range(len(cadeiaCMD)):
    entrada += cadeiaCMD[posicaoEntrada]

estadosTransicoes = open(tabelaCMD, 'r')
estadoInicial = estadosTransicoes.readline().rstrip('\n')
estadoFinal = estadosTransicoes.readline().rstrip('\n')
transicoes = []

def saberEstado(letraAlfabeto, estado, listaTransicoes):
    for x in range(len(listaTransicoes)):
        estadoELetra = estado + ' ' + letraAlfabeto
        if estadoELetra in listaTransicoes[x]:
            novoEstado = listaTransicoes[x][5:]
            break
    return novoEstado

for linha in estadosTransicoes:
    conteudoLinha = linha.rstrip('\n')
    transicoes.append(conteudoLinha)

estadoAtual = estadoInicial
resultado = ''
for letra in range(len(cadeiaCMD)):
    ultimoEstado = saberEstado(cadeiaCMD[letra], estadoAtual, transicoes)
    estadoAtual = ultimoEstado
if estadoAtual in estadoFinal:
    resultado += (cadeiaCMD + ' - reconhece')
else:
    resultado += (cadeiaCMD + ' - nao reconhece')

print(resultado)