#  Teste Técnico BYNE

## Requisitos

- [x] Servidor deve implementar dois serviços: Um que retorne números pares, e outro números ímpares;
- [x] Cada cliente ao se conectar ao servidor deve iniciar um processo que incrementa o valor recebido do servidor em 1 a cada 500ms, enviando o novo valor ao servidor;
- [x] Cada cliente deve, em um intervalo aleatório entre 3 e 5 segundos, requisitar ao servidor um número par ou ímpar, escolhido de forma aleatória, que será utilizado como novo valor de incremento, ao invés de 1;
- [x] Os números devem estar sempre no range 0-99;
- [x] Servidor deve enviar um valor ao aceitar conexão do cliente;
- [x] Servidor deve manter o último valor enviado para cada cliente. Caso um mesmo cliente se conecte, enviar esse valor para o mesmo. Caso não haja valor registrado, enviar 0;
- [x] Servidor deve manter um log de todas as mensagens trocadas;
- [x] Você pode utilizar qualquer linguagem/framework que se sentir mais confortável.
- [x] A entrega deve ser feita através de um repositório git público de sua escolha;
- [x] A data limite é até 28/02/22 às 23:59:59.

## Introdução

Assume-se que já tenha instalado Python e pip e que o sistema seja Windows.

[Flask](https://flask.palletsprojects.com/en/2.0.x/) é um micro framework que utiliza a linguagem [Python](https://www.python.org/) para criar aplicativos Web. Foi criado em 2010 e é baseado no kit de ferramentas [Werkzeug](https://werkzeug.palletsprojects.com/en/2.0.x/) [WSGI](https://wsgi.readthedocs.io/en/latest/) e na biblioteca [Jinja2](https://jinja.palletsprojects.com/en/3.0.x/).

## Reprodução

Inicia-se criando um ambiente de desenvolvimento virtual. Para criar um ambiente chamado "venv" e ativa-lo:

```
$ python -m venv venv
$ venv\Scripts\activate
```

Quanto terminar, para desativar o ambiente:

```
$ deactivate
```

Após criar o ambiente virtual é necessário instalar os requerimentos:

```
$ pip install -r requirements.txt
```

Antes de rodar o projeto localmente é importante definir corretamente a url base com a variavel `app.config['BASE_URL']` no arquivo `app.py`:

```
app.config['BASE_URL'] = 'http://127.0.0.1:5000/'
```

Então, finalmente para rodar o projeto flask localmente:

```
$ python app.py
```

No flask, porta padrão é `5000` e para acessar o sistema: [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

Página de documentação Swagger:  `http://127.0.0.1:5000/api/`


## Descrição

Sistema com desenvolvido em `Flask` para construir uma API com `flask-restx` com documentação Swagger.

A API funciona 100% desacoplada do APP (verificar [Swagger](http://teste-tecnico-byne.herokuapp.com/api/)).

No lado do cliente, foi somente explorado `html` e `javascript`.

Sistema de login simples para registrar e manter o último valor de cada cliente.

Os dados são armazenados no `data.json`.

Todas as mensagens trocadas entre o cliente e servidor são registradas em `logs.log`.

## Features:

- [Flask](https://flask.palletsprojects.com/en/2.0.x/)
- [gunicorn](https://gunicorn.org)
- [Jinja2](https://jinja.palletsprojects.com/en/3.0.x/)
- [Werkzeug](https://werkzeug.palletsprojects.com/en/2.0.x/)
- [flask-restx](https://flask-restx.readthedocs.io/en/latest/)
- [requests](https://docs.python-requests.org/en/latest/)

## Estrutura do Sistema
```
.
|──────teste-tecnico-byne/
| |────app.py
| |────api.py
| |────config.py
| |────utils.py
| |────data.json
| |────logs.log
| |────Procfile
| |────requirements.txt
| |────readme.md
| |────templates/
| |──────home.html
| |──────login.html
| |──────registro.html
```
## Descrição dos Arquivos

- app.py -> Códigos relacionados a parte de 
- api.py -> Códigos relacionados a API.
- utils.py -> Classe para manusear o JSON.
- data.json -> JSON para armazenar os dados.
- logs.log -> Log das interações entre o cliente e o servidor.
- Procfile -> Arquivo relacionado ao deploy no Heroku.
- requirements.txt -> Requerimentos do sistema.
- readme.md -> Leia-me.
- .gitignore -> Lista de arquivos ignorados pelo rep.
- home.html -> HTML da página princial, com 
- login.html -> HTML da página de login.
- registro.html -> HTML da página de registro.

## Deploy com Heroku

1. Fazer cadastro no Heroku.
2. Conectar com Github.
3. Indicar repositório.
4. Deploy automático ou manual.

## Referências

- [Flask](http://flask.pocoo.org/)
- [Heroku](https://devcenter.heroku.com/articles/getting-started-with-python)
- [pythonise](https://pythonise.com/series/learning-flask/your-first-flask-app)