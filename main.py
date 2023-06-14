from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']

        return redirect('/home')
    
    return render_template('login.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        data_aniversario = request.form['data_aniversario']
        senha = request.form['senha']

        return redirect('/home')

    return render_template('cadastro.html')

@app.route('/home')
def home():
    return render_template('home.html')

if __name__ == '__main__':
  print('Rodando api...')
  app.run(port=5000)
