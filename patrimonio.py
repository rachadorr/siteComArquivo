#ESSE É O COM FUNÇÕES
from flask import Flask, render_template, request


import pandas as pd
from itertools import chain

#caso for usar no Google Colab usar esse import abaixo
#from google.colab import drive
#drive.mount('/content/drive')


import logging
# Import das bibliotecas.
import sys # Biblioteca para acessar módulos do sistema

# Import das bibliotecas.
import os # Biblioteca para manipular arquivos
app = Flask(__name__)
# ============================
def verificaDiretorio():
    """
      Verifica se existe o diretório.
    """
    DIRETORIO = "content/drive/testedepasta"
    # Verifica se o diretório existe
    if not os.path.exists(DIRETORIO):
        # Cria o diretório
        os.makedirs(DIRETORIO)
        logging.info("Diretório criado: {}".format(DIRETORIO))

    return DIRETORIO


class Patrimonio:
    def __init__(self,patrimonio,descricao):
        self.patrimonio = patrimonio
        self.descricao = descricao

patrimonio = []

arquivo = "dados/ListaLevantamentoCSV.csv"

#carrega o arquivo no modelo necessário com a devida codificação
tabela = pd.read_csv(arquivo,encoding="utf-8", sep = ';')

    #apaga as linhas desnecessárias
tabela = tabela.drop([0,1,25], axis=0)

    #carrega somente as colunas de patrimonio
#tabela = tabela.iloc[:,[0,2,5,7]]
#tabela = tabela.iloc[:,[0,2]]
#for index,row in tabela.iterrows():
#    patrimonio.append(Patrimonio(row.values[0],row.values[1]))

tabela = tabela.iloc[:,[0,2,5,7]]
for index,row in tabela.iterrows():
    patrimonio.append(Patrimonio(row.values[2],row.values[3]))
    patrimonio.append(Patrimonio(row.values[0],row.values[1]))

#tabela = tabela.iloc[:,[0,2]]
#for index,row in tabela.iterrows():
#    patrimonio.append(Patrimonio(row.values[0],row.values[1]))

#tabela = tabela.iloc[:,[5,7]]
#print(type(tabela.))
#for index,row in tabela.iterrows():
#    patrimonio.append(Patrimonio(row.values[0],row.values[1]))

#print(f" patrimonio é original {patrimonio[1].patrimonio}")
##print(f" patrimonio é original {patrimonio.index[1]}")
#print(f" patrimonio após deletado {patrimonio[1].patrimonio}")



#carga  = ["000547116","000547117","000547118",]
carga  = [
"000547067",
"000547068",
"000547069",
"000547070",
"000547072",
"000547073",
"000547075",
"000547076",
"000547077",
"000547078",
"000547079",
"000547080",
"000547081",
"000547082",
"000547083",
"000547084",
"000547085",
"000547086",
"000547088",
"000547089",
"000547090",
"000547091",
"000547092",
"000547093",
"000547094",
"000547095",
"000547096",
"000547097",
"000547098",
"000547099",
"000547100",
"000547101",
"000547102",
"000547105",
"000547110",
"000547111",
"000547112",
"000547114",
"000547115",
"000547947",
"000551048",
"000551663",
"000552773",
"000552782",
"000566646",
"000568026",
"000571370",
"000571499",
"000571500",
"000571501",
"000571502",
"000574815",
"000574818",
"000575159",
"001292248",
"001295708",
"001298547",
"001296461",
"001297620",
"001297714",
"001297728",
"001298182",
"001298265"
]


resultado = []
for i,pat in enumerate(patrimonio):
  #print(f"lista original {i, pat.patrimonio}")
  resultado.append(pat.patrimonio)

#patrimoniofaltante = {}
#print("Micro-Ondas 220 V" in patrimonioteste.values())
#print(type(carga))
#print(carga[2])

def verificaResultado():
    result = list(sorted(set(resultado) - set(carga)))
    
    return result

result = verificaResultado()
print (f"Esse é o resultado antes {result}")


def verificaPatrimonio(result):
    faltante = []
    result = result
    for c in enumerate(result):
  #print(f"Esse é o patrimonio {i, pat.patrimonio}")
        for i,pat in enumerate(patrimonio):
        #print(f"Esse é a carga {c}")
            if (pat.patrimonio in c):
                faltante.append(pat)
    
    return faltante

faltante = verificaPatrimonio(result)
#print(type(faltante))
#print(f"Faltam os itens: {faltante.}")








@app.route('/', )
def index():
    return render_template('index.html', reprovados=patrimonio)
                                         #lado html = reprovados    lado Python = alunos
                                

@app.route('/login')
def login():
   return render_template('login.html')

@app.route('/autenticar', methods = ['GET'])
def autentica():
   codigo = request.args.get('codigo')
   carga.append(codigo)
   result = verificaResultado()
   faltante = verificaPatrimonio(result)
   print(f"esse é o carga do autenticar{carga}") 
   return render_template('autenticar.html', restante=faltante)
   #return render_template('index.html',reprovados=patrimonio, restante=faltante)
   #return "usuario: {}".format(codigo)


def atualizar1():
    novo_dado = request.form['novo_dado']
    patrimonio.append(novo_dado)
    return render_template('index.html', dados=patrimonio)


@app.route('/limpar')
def limpar():
    patrimonio.clear() 
    return render_template('index.html', dados=patrimonio)

if __name__ == '__main__':
    app.run(debug=True)
