#!/usr/bin/python
# -*- coding: iso-8859-15 -*_
#programa que conjuga o verbo regulares
#informaçoes de conexao à base de dados:
#carrega a biblioteca de funçoes de acesso e manipulaçao de dados
import MySQLdb
#informa os dados da conexao 
dados = MySQLdb.connect(host='****', port=*****, user='******', passwd='*****', db='******') 
# cursor de manipulaçao   
cobra = dados.cursor()
#Informações relativas à conexão com a web
# carrega a biblioteoca de funções para o acesso webb
import urllib2
#usuario
print '===================================================='
print 'Programa conjugador de verbos regulares em portugues'
print '===================================================='
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
#Consulta no wikcionario 
print 'Aguarde um momento enquanto consulto o Wikicionario para saber'
print 'se o verbo' + seu_verbo + 'consta como verbo regular'
print
#endereço com o verbo a ser consultado
endereco_web = 'http://pt.wiktionary.org/wiki/' + seu_verbo
# depois, cria a requisição para a busca
req_web = urllib.Request(endereco_web, headers={'User-Agent': "Mozilla5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0"})
# busca conteudo
conteudo_web = urllib2.urlopen(req_web)
# armazena conteudo
conteudo_web = conteudo_web.read()
#pesquisa se o verbo é regular
if ("Verbo regular da "in conteudo_web):
  print 'Confirmado: ' + seu_verbo + ' é um verbo regular!'
  print 'Verificarei se ja foi conjugado anteriormente.'
  print 
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
 print 'Essa é a primeira vez que conjugo '+ seu_verbo + ' !'
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
  print 
  print 'O Wikicionário é um projeto colaborativo e pode ser que ' + seu_verbo
  print 'ainda não conste nele. Se for esse o caso, visite a página web'
  print 'htttp://pt.wiktionary.org e complemente a informação sobre ' + seu_verbo + '.'
  print
  print 'Obrigado'
  print 
dados.close()
