#!/usr/bin/python
# -*- coding: iso-8859-15 -*_
#programa que conjuga o verbo
#primeiro criamos uma lista com terminacoes de verbos regulares
pessoas = ['Eu','Tu','Ele','Nós','Vós','Eles'];
conjuga_ar = ['o','as','a','amos','ais','am'];
conjuga_er = ['o','es','e','emos','eis','em'];
conjuga_ir = ['o','es','e','imos','is','em'];
verbo = raw_input("Digite o infinitivo de um verbo regular:") #verbo a se conjugado
termina_em = verbo[-2:] #separa a terminacao do verbo
#conjuga o verbo apropriadamente de acordo com  a terminacao
if termina_em == 'ar':
 for i in range(6): #repete seis vezes, percorrendo a lista
  print pessoas[i]+' '+verbo[:-2]+conjuga_ar[i]
elif termina_em == 'er':
 for i in range(6): #repete seis vezes, percorrendo a lista
  print pessoas[i]+' '+verbo[:-2]+conjuga_er[i]
elif termina_em == 'ir':
 for i in range(6): #repete seis vezes, percorrendo a lista
  print pessoas[i]+' '+verbo[:-2]+conjuga_ir[i]
else:
  print 'Tem certeza que '+verbo+' é um verbo regular?'

