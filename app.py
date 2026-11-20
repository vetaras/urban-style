
from flask import Flask, render_template, session, redirect, url_for

app = Flask(__name__)

app.secret_key = "urban_style_chave_secreta"

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


@app.route("/adicionar/<int:produto_id>", methods=["POST"])
def adicionar_carrinho(produto_id):
    carrinho = session.get("carrinho", [])

    carrinho.append(produto_id)

    session["carrinho"] = carrinho

    return redirect(url_for("pagina_produtos"))


@app.route("/carrinho")
def carrinho():
    ids_carrinho = session.get("carrinho", [])

    produtos_carrinho = []

    for produto_id in ids_carrinho:
        for produto in lista_produtos:
            if produto["id"] == produto_id:
                produtos_carrinho.append(produto)

    total = 0

    for produto in produtos_carrinho:
        total += produto["preco"]

    return render_template(
        "carrinho.html",
        carrinho=produtos_carrinho,
        total=total
    )


@app.route("/remover/<int:produto_id>", methods=["POST"])
def remover_carrinho(produto_id):
    ids_carrinho = session.get("carrinho", [])

    if produto_id in ids_carrinho:
        ids_carrinho.remove(produto_id)

    session["carrinho"] = ids_carrinho

    return redirect(url_for("carrinho"))


if __name__ == "__main__":
    app.run(debug=True)
