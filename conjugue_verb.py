#!/usr/bin/python
# -*- coding: iso-8859-15 -*_
#programa que conjuga o verbo regulares
#informaçoes de conexao à base de dados:
#carrega a biblioteca de funçoes de acesso e manipulaçao de dados
import MySQLdb
#informa os dados da conexao 
dados = MySQLdb.connect(host="*******", port=*****, user="*******", passwd="*****", db="******") 
# cursor de manipulaçao   
cobra = dados.cursor()
#informaçoes do usuario
seu_nome = raw_input("Digite seu primeiro nome: ")
seu_sobrenome = raw_input("Digite seu sobrenome: ")
#verifica se usuario ja existe
existe = cobra.execute(("SELECT nome, sobrenome FROM usuario WHERE nome=%s AND sobrenome=%s"))
if existe > 0:
 print 'Obrigado por usar novamente nosso conjugador, ' + seu_nome + ' ' + seu_sobrenome
else:
 cobra.execute("INSERT INTO usuario (nome, sobrenome, visitas) VALUES (%s, %s, %s) ", (seu_nome, seu_sobrenome,1))
 dados.commit()
#lista com terminacoes de verbos regulares
pessoas = ['Eu','Tu','Ele','Nós','Vós','Eles'];
conjuga_ar = ['o','as','a','amos','ais','am'];
conjuga_er = ['o','es','e','emos','eis','em'];
conjuga_ir = ['o','es','e','imos','is','em'];
print 'Conjugarei um verbo regular para você'
print
#O usuario informa o verbo
seu_verbo = raw_input("Digite o infinitivo de um verbo regular:") #verbo a se conjugado
#existencia do verbo dentro da base de dados
existe = cobra.execute(("SELECT verbo FROM verbo WHERE verbo=s%"), (seu_verbo))
if existe > 0:
 cobra.execute(("SELECT frequencia FROM verbo WHERE verbo =%s"), (seu_verbo))
 frequencia_bd = cobra.fetchone()
 frequencia_bd = frequencia_bd[0] #extrai o primeiro dado da tupla
 print 'O verbo' + 'seu_verbo' + 'já foi conjugado' + str(frequencia_bd) + 'vezes.'
 cobra.execute("UPDATE verbo SET frequencia = %s WHERE verbo = %s", (frequencia_bd + 1, seu_verbo))
 dados.commit()
 print 'Esse verbo ja foi anteriormente conjugado: ' + seu_verbo
else:
 cobra.execute("INSERT INTO verbo (verbo, frequencia, regular) VALUES(s%, s% s%)", (seu_verbo,1,1))
 dados.commit()
termina_em = seu_verbo[-2:] #separa a terminacao do verbo
#conjuga o verbo apropriadamente de acordo com  a terminacao
if termina_em == 'ar':
 for i in range(6): #repete seis vezes, percorrendo a lista
  print pessoas[i]+' '+seu_verbo[:-2]+conjuga_ar[i]

elif termina_em == 'er':
 for i in range(6): #repete seis vezes, percorrendo a lista
  print pessoas[i]+' '+seu_verbo[:-2]+conjuga_er[i]

elif termina_em == 'ir':
 for i in range(6): #repete seis vezes, percorrendo a lista
  print pessoas[i]+' '+seu_verbo[:-2]+conjuga_ir[i]

else:
  print 'Tem certeza que '+seu_verbo+' é um verbo regular?'
dados.close()
