# TEST

## Start up

### 1. Install the dependencies
- Instalar python 
- Instalar pip
- pip install -r requirements.txt
    - Obs.: Não esquecer de criar um ambiente virtual com o seguinte comando `python -m venv env` e ativa-lo com o seguinte comando `source env/bin/activate` ou `env\Scripts\activate` no windows

### 2. Run the application

- Precisamos criar um superuser para fazer uso do basic auth , para isso usaremos o seguinte comando `python manager.py createsuperuser`
- Precisamos instanciar o banco de dados, para isso usaremos o seguinte comando `python manager.py migrate`
- Precisamos rodar o servidor, para isso usaremos o seguinte comando `python manager.py runserver`, com isso ele te informará uma url para acessar a aplicação

### 3. Run the tests

- Para rodar os testes, usaremos o seguinte comando `python manager.py test`, onde está sendo usado test de integração.
