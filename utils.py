from models import Pessoas, db_session

# Insere dados na tabela pessoa
def insere_pessoas():
    pessoa = Pessoas(nome='Russo', idade=19)
    print(pessoa)
    pessoa.save()

# Consulta pessoas na tabela pessoas
def consulta_pessoas():
    pessoas = Pessoas.query.all()
    print(pessoas)
    pessoa = Pessoas.query.filter_by(nome='Cristiano').first()
    print(pessoa.idade)

# Altera dados na tabela pessoa
def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Russo').first()
    pessoa.nome = 'Otavio'
    pessoa.save()

# Exclui pessoas da tabela pessoa
def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Russo').first()
    pessoa.delete()


if __name__ == '__main__':
    # insere_pessoas()
    # altera_pessoa()
    exclui_pessoa()
    consulta_pessoas()
