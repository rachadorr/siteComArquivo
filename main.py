from flask import Flask, render_template, request

#app = Flask(__name__)

# Dados iniciais
dados = []

class Aluno:
    def __init__(self,id,nome,nota,media,situacao):
        self.id = id
        self.nome = nome
        self.nota = nota
        self.media = media
        self.situacao = situacao
a1= Aluno(1,"pedro",5,8,"aprovado")
a2= Aluno(2,"joaquim",5,8,"reprovado")
a3= Aluno(3,"laura",9,8,"aprovado")


class Dados:
    def __init__(self,patrimonio):
        self.patrimonio = patrimonio

d1 = Dados(222)
d2 = Dados(33)



alunos = []
alunos.append(a1)
alunos.append(a2)


print(alunos[1].nome)
a2= Aluno(3,"laura",9,8,"aprovado")
alunos.append(Aluno(3,"laura",9,8,"aprovado"))
print(alunos[2].nome)

dados.append(d1)
dados.append(d2)
print(alunos[1].media)
print(dados[1])

#@app.route('/')
#def index():
#    return render_template('index.html', reprovados=alunos )
#                                         #lado html = reprovados    lado Python = alunos
#
#@app.route('/atualizar', methods=['POST'])
#def atualizar():
#    novo_dado = request.form['novo_dado']
#    dados.append(novo_dado)
#    return render_template('index.html', dados=dados)
#
#@app.route('/limpar')
#def limpar():
#    dados.clear()
#    return render_template('index.html', dados=dados)
#
#if __name__ == '__main__':
#    #app.run(debug=True)
#