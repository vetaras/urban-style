
from flask import Flask, render_template

app = Flask(__name__)

lista_produtos = [
    {
        "id": 1,
        "nome": "Camiseta Oversized",
        "categoria": "Masculino",
        "preco": 89.90
    },
    {
        "id": 2,
        "nome": "Moletom Streetwear",
        "categoria": "Masculino",
        "preco": 159.90
    },
    {
        "id": 3,
        "nome": "Calça Cargo",
        "categoria": "Feminino",
        "preco": 129.90
    },
    {
        "id": 4,
        "nome": "Jaqueta Jeans",
        "categoria": "Feminino",
        "preco": 189.90
    }
]


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/produtos")
def pagina_produtos():
    return render_template("produtos.html", produtos=lista_produtos)


@app.route("/carrinho")
def carrinho():
    return render_template("carrinho.html")


if __name__ == "__main__":
    app.run(debug=True)
