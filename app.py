from flask import Flask, render_template

lista = [
    "Giovanni", "Maria", "Giuseppe", "Anna", "Luca", "Sofia", "Marco", "Giulia", "Alessandro", "Martina",
    "Francesco", "Alessia", "Lorenzo", "Emma", "Matteo", "Chiara", "Leonardo", "Alice", "Luisa", "Niccolò",
    "Alessandra", "Davide", "Elena", "Riccardo", "Laura", "Simone", "Sophia", "Federico", "Greta", "Gabriele",
    "Beatrice", "Lorenza", "Filippo", "Camilla", "Mattia", "Elisa", "Nicola", "Aurora", "Vittorio", "Valentina",
    "Alberto", "Caterina", "Roberto", "Gabriella", "Daniele", "Isabella", "Emanuele", "Clara", "Andrea"
]

app = Flask(__name__)

@app.route('/')
def index():
    nome = "auridebson"
    idade = 39
    return render_template('index.html', nome=nome, idade=idade, lista=lista)


@app.route("/cadastrar", methods=["POST"])
def cadastrar():
    nome = request.form.get('nome')
    lista.append(nome)

    return """
    <script>
        alert("Cadastro realizado com sucesso")
        window.location.href = "/"
    </script>
    """

@app.route("/visulizar")
def visualizar():
    render_template("visualizar.html", lista)


if __name__ == "__main__":
    app.run(debug=True)