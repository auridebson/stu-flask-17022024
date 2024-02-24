from flask import Flask, render_template, request, redirect, url_for
# from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

# Configuração do banco de dados SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ToDoList.db'

# Desativa o rastreamento de modificações do SQLAlchemy para evitar consumo de recursos
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicialização da extensão SQLAlchemy
db = SQLAlchemy(app)

# Inicialização da extensão Flask-Migrate para migrações do banco de dados
migrate = Migrate(app, db)

# Definição da classe Tarefa para mapeamento ORM do SQLAlchemy
class Tarefa(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), nullable=False)
    data = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.String(200), nullable=False)

# Rota principal da aplicação, exibe a lista de tarefas
@app.route("/")
@app.route("/index")
def index():
    # Consulta todas as tarefas no banco de dados
    tarefas = Tarefa.query.all()
    # Renderiza o template "index.html", passando as tarefas como argumento
    return render_template("index.html", tarefas=tarefas)

# Rota para exibir o formulário de cadastro de uma nova tarefa
@app.route("/cadastro")
def cadastro():
    # Renderiza o template "cadastro.html"
    return render_template("cadastro.html")

# Rota para processar o envio do formulário de cadastro
@app.route("/envio", methods=["POST"])
def envio():
    # Obtém os dados do formulário
    nome = request.form.get("nome")
    data = request.form.get("data")
    descricao = request.form.get("descricao")

    # Cria uma nova instância de Tarefa com os dados do formulário
    tarefa = Tarefa(nome=nome, data=data, descricao=descricao)
    # Adiciona a nova tarefa ao banco de dados
    db.session.add(tarefa)
    # Confirma a transação no banco de dados
    db.session.commit()

    # Redireciona para a página inicial após o cadastro da tarefa
    return redirect(url_for("index"))

# Rota para concluir (ou excluir) uma tarefa
@app.route("/conc/<int:id>")
def conc(id):
    # Consulta a tarefa pelo seu ID
    tarefa = Tarefa.query.get(id)

    # Remove a tarefa do banco de dados
    db.session.delete(tarefa)
    # Confirma a transação no banco de dados
    db.session.commit()

    # Redireciona para a página inicial após concluir a tarefa
    return redirect(url_for("index"))

# Inicia o servidor Flask
if __name__ == "__main__":
    # Ativa o modo de depuração para facilitar o desenvolvimento
    app.run(debug=True)