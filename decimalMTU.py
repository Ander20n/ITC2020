# coding: utf-8
import sys

'''
Código que transforma um número decimal nas transições

O código deve ser rodado via prompt de comando, como o seguinte exemplo: 

python decimalMTU.py 450813704461563958982113775643437908

Caso o valor informado gere máquina sem transições, o retorno será: Não existe máquina para o número informado

Algumas entradas como 0, 6 e 12 retornam máquinas que fazem a leitura do 0, segue no estado 0 e andando para direita, 
assim o retorno para todas elas será o número zero.
'''

numeroDecimal = 12#sys.argv[1]
entrada = str(bin(int(numeroDecimal))[2:])

if entrada[-3:] != '110':
    entrada+='110'
    
entradaApagar = entrada
transicoes = []

condicao = True
while condicao:
    if '110' in entradaApagar:
        posicao = entradaApagar.index('110')
        transicoes.append(entradaApagar[:posicao+3])
        entradaApagar = entradaApagar[posicao+3:]
    else:
        condicao = False

resposta = []
tran = ""
while len(transicoes) > 0 :
    if len(transicoes[0]) > 0:
        if transicoes[0] == "110":
            posicao = transicoes[0].index('110')
            tran += "R"
            resposta.append(tran)
            del transicoes[0]
            tran = ""
        else:
            if transicoes[0][:5] == "11111":
                resposta.append('Não existe máquina para o número informado')
                transicoes = []
            elif "0" in transicoes[0][0]:
                posicao = transicoes[0].index('0')
                tran += "0"
                transicoes[0] = transicoes[0][posicao+1:]
            elif len(transicoes[0]) == 4 and "1110" in transicoes[0]:
                posicao = transicoes[0].index('1110')
                tran += "L"
                resposta.append(tran)
                del transicoes[0]
                tran = ""
            elif len(transicoes[0]) == 5 and "11110" in transicoes[0]:
                posicao = transicoes[0].index('11110')
                tran += "STOP"
                resposta.append(tran)
                del transicoes[0]
                tran = ""
            elif "10" in transicoes[0]:
                posicao = transicoes[0].index('10')
                tran += "1" 
                transicoes[0] = transicoes[0][posicao+2:]
            elif "0" in transicoes[0][0]:
                posicao = transicoes[0].index('0')
                tran += "0"
                transicoes[0] = transicoes[0][posicao+1:]
else:
    
    if resposta[0] != 'Não existe máquina para o número informado':
    
        if len(resposta) == 1 and resposta[0] == "R":
            resposta.append('R')
        if resposta[0] != "R":
            resposta[:0] = "R"
        for x in range(len(resposta)):
            if resposta[x] == "R" or resposta[x] == "0R":
                resposta[x] = "00R"
            elif resposta[x] == "L" or resposta[x] == "0L":
                resposta[x] = "00L"
            elif resposta[x] == "STOP":
                resposta[x] = "0STOP"
        tamanho = len(resposta)
        
        transicoesFinais = []
        
        for z in range(int(tamanho/2)):
            if resposta[0][-2] != 'O':
                transicoesFinais.append('q%d'%(z) + ' 0' + ' ' +  'q'+str(int(resposta[0][:-2],2)) + ' ' + resposta[0][-2] + ' ' +resposta[0][-1])
            else: 
                if len(resposta[0]) < 6:
                    transicoesFinais.append('q%d'%(z) + ' 1' + ' ' +  'q0 '+ resposta[0][-5] + ' ' +resposta[0][-4:])
                else:
                    transicoesFinais.append('q%d'%(z) + ' 0' + ' ' +  'q'+ resposta[1][-6] + ' ' + resposta[0][-5] + ' ' +resposta[0][-4:])
            if resposta[1][-2] != 'O' and len(resposta[1]) > 2:
                transicoesFinais.append('q%d'%(z) + ' 1' + ' ' +  'q'+str(int(resposta[1][:-2],2)) + ' ' + resposta[1][-2] + ' ' +resposta[1][-1])
            elif len(resposta[1]) == 2 and not 'STOP' in resposta:
                transicoesFinais.append('q%d'%(z) + ' 1' + ' ' +  'q ' + resposta[1][-2] + ' ' +resposta[1][-1])
            else:
                if len(resposta[1]) < 6:
                    transicoesFinais.append('q%d'%(z) + ' 1' + ' ' +  'q0 '+ resposta[1][-5] + ' ' +resposta[1][-4:])
                else:
                    transicoesFinais.append('q%d'%(z) + ' 1' + ' ' +  'q'+ resposta[1][-6] + ' ' + resposta[1][-5] + ' ' +resposta[1][-4:])
            del resposta[0]
            del resposta[0]
            if len(resposta) == 0:
                break 
            
          
        for w in range(len(transicoesFinais)):
            print(transicoesFinais[w])
    else:
        print(resposta[0])