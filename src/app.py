from flask import Flask, render_template

app = Flask(__name__)


# Rotas
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/projetos')
def projetos():
    return render_template('projetos.html')

@app.route('/curriculo')
def curriculo():
    return render_template('curriculo.html')


@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

# Rodando o app
if __name__ == 'main':
    app.run() 