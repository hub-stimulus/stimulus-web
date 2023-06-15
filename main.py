from flask import Flask, render_template, request, redirect,url_for,jsonify
import json,os


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
       
        file_path = os.path.join('data', f'{email}.json')
        if not os.path.exists(file_path):
            return 'Email não encontrado'

        with open(file_path, 'r') as file:
            json_data = file.read()

        data = json.loads(json_data)
        admin = False
        if email=='admin@admin.com':
            admin = True

        if data['email'] == email and data['senha'] == senha:
            return render_template('home.html', data=data,admin={'admin':admin})
        else:
            return render_template('login.html')

    
    return render_template('login.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':

        nome = request.form['nome']
        email = request.form['email']
        data_aniversario = request.form['data_aniversario']
        senha = request.form['senha']
        sexo = request.form['sexo']
        escolaridade = request.form.getlist('escolaridade')
        regiao_brasil = request.form['regiao-brasil']
        faixa_renda = request.form['renda']
        teve_covid = request.form['teve-covid']
        sequelas = request.form['sequelas']
        tratamento_cognitivo = request.form['tratamento-cognitivo']
        mudancas_cognitivas = request.form['mudancas-cognitivas']
        mudancas_cognitivas_quais = request.form.getlist('mudancas-cognitivas-quais')
        atividade_fisica = request.form['atividade-fisica']
        doenca_associada = request.form['doenca-associada']
        
        
        
        data = {
            'nome': nome,
            'email': email,
            'data_aniversario': data_aniversario,
            'senha': senha,
            'sexo': sexo,
            'escolaridade': escolaridade,
            'regiao_brasil': regiao_brasil,
            'faixa_renda': faixa_renda,
            'teve_covid': teve_covid,
            'sequelas': sequelas,
            'mudancas_cognitivas': mudancas_cognitivas,
            'mudancas_cognitivas_quais': mudancas_cognitivas_quais,
            'atividade_fisica': atividade_fisica,
            'doenca_associada': doenca_associada,
            'tratamento_cognitivo' : tratamento_cognitivo
        }
        
        json_data = json.dumps(data)

        folder_path = os.path.join(os.getcwd(), 'data')
        file_name = f"{email}.json"
        file_path = os.path.join(folder_path, file_name)
        
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        with open(file_path, 'w') as file:
            file.write(json_data)
          
        return redirect('/')

    return render_template('cadastro.html')

@app.route('/listar', methods=['GET'])
def listar():
    dados_combinados = []
    for arquivo in os.listdir(os.path.join(os.getcwd(), 'data')):
        if arquivo.endswith('.json'):
            caminho_arquivo = os.path.join(os.path.join(os.getcwd(), 'data'), arquivo)
        
            with open(caminho_arquivo, 'r') as file:
                dados_json = json.load(file)
            
            dados_combinados.append(dados_json)

    objeto_combinado = {
    'dados': dados_combinados,
    'total_arquivos': len(dados_combinados)
                                            }
    return render_template('listar.html',data=objeto_combinado,len=len(dados_combinados))

if __name__ == '__main__':
  print('Rodando api...')
  app.run(port=5000)
