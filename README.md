# Python + AWS Lambda Hands On

## Python

- Criada em 1990, por Guido Van Rossum.
- "Bala de prata" (quase).
- Muito utilizado em:
  - Automatizações - [Selenium](https://selenium-python.readthedocs.io/), [Beautiful Soap](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
  - Bigdata - [PySpark](http://spark.apache.org/docs/latest/api/python/)
  - Data Sciente - [Jupyter](https://jupyter.readthedocs.io/en/latest/), Libs estatisticas e analise exploratória
  - Machine Learn / Deep Learning - [NLTK](https://www.nltk.org/), [Scikit-Learn](https://scikit-learn.org/stable/), [Tensor Flow](https://www.tensorflow.org/?hl=pt-br), [Keras](https://keras.io/)
  - Web - [Django](https://www.djangoproject.com/)
  - Hack (Mr. Robot)

### Exemplos de script

1. **python/exemplos/1-hello-world.py**
2. **python/exemplos/2.teste-unitario.py**

### Preparação do Ambiente

Criação do ambiente:

```sh
cd python
```

```sh
# Versão >= Python 3.3
python3 -m venv ./hands-on-env -p=<CAMINHO_PYTHON_HOME>/python
# Versão < Python 3.3
pip install virtualenv
virtualenv -p=<CAMINHO_PYTHON_HOME>/python ./hands-on-env
```

Ativação do ambiente:

```sh
# Linux/Gitbash
source ./hands-on-env/bin/activate
# Windows
hands-on-env/Script/activate.bat
```

### PIP

- É o gerenciador de pacotes do Python.
- Gradle/Maven/NPM do Python

#### Instalação das dependências

```sh
pip install <NOME DO PACOTE>

# OU

pip install -r requirements.txt
```

### Notebooks

```sh
jupyter notebook notebooks
```

1. [Python Básico](https://github.com/ortisan/python-aws-lambda-hands-on/blob/main/python/notebooks/1-PythonBasico.ipynb)
1. [Bot Bitcoin](https://github.com/ortisan/python-aws-lambda-hands-on/blob/main/python/notebooks/2-BotBitcoinNow.ipynb)
1. [Analise Dados Bitcoin](https://github.com/ortisan/python-aws-lambda-hands-on/blob/main/python/notebooks/3-AnalyticsBitcoinPrice.ipynb)

## AWS Lambda

- Function as a service (FAAS)
- Functions são configuradas, carregadas e executadas por uma runtime
- Configuramos somente a memória. CPU é alocada indiretamente
- Pagamos pelo tempo de duração da execução da função
- Uma das peças principais de uma arquitetura Serverless

Pontos principais (Cai nas certificações):

- Tempo máximo de duração 15 min
- Pacote pode ter até 50 Mb zipado e 250 Mb deszipado
- 512 Mb storage disponível no /tmp
- Mínimo 128 MB and máximo 3GB

### Permissões

- AWS Lambda execution role

Exemplo: Assume role policy:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Effect": "Allow",
    }
  ]
}
```

### [Versões](https://docs.aws.amazon.com/lambda/latest/dg/configuration-aliases.html)

- Cada deploy de uma lambda recebe uma versão sequencial e um ARN.
- O ARN com sufixo latest aponta para o último deploy
- Por essa caracteristica de imutabilidade de versão, podemos utilizar apelidos (Alias). Feature muito utilizada em integrações com o API Gateway para os modelos de deploy Blue Green

```sh
# Criar um apelido
aws lambda create-alias --function-name my-function --name alias-name --function-version version-number --description " "
# Alterar o apelido
aws lambda update-alias --function-name my-function --name alias-name --function-version version-number 
To delete an alias, use the delete-alias command.
# Deletar o apelido
aws lambda delete-alias --function-name my-function --name alias-name 
```

### [Ciclo de Vida](https://docs.aws.amazon.com/lambda/latest/dg/runtimes-context.html)

![image](images/lambda-lifecycle.png)

**Fase Inicial**:

- Cria ou descongela a função
- Faz download do código;
- Configura as variáveis de ambiente;
- Roda as funções de inicialização - Tudo que não pertença à função **handler**

**Fase Execução**:

- A função **handler** é executada. Só pagamos por esse tempo (Billing execution).

**Fase Desligamento**:

- Quando a função não recebe requisições por x segundos, a lambda é desligada.

### Criação da Infraestrutura

- [Exemplo em terraform de lambda com integrado com o Event Bridge](https://github.com/ortisan/aws-terraform-recipes/tree/main/lambda/lambda-eventbridge)

### Criação do Projeto

Podemos criar o projeto utilizando o Serverless Application Model (SAM).

1. Instalar o [client](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)

2. Criar a base do projeto:
  ```sh
  sam init
  # Seguir o passo a passo
  ```

### Execução local

```sh
sam local invoke FunctionExemplo --event events/event.json
```
