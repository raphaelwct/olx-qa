# Desafio QA OLX

Desafio para a vaga de QA na OLX

## Introdução

Estas instruções tem o objetivo de auxiliar você obter uma cópia do projeto instalado e funcionando em sua máquina local, para fins de teste e avaliação da solução.

### Pré-requisitos

Antes de iniciar a instalação do projeto é necessário configurar e instalar os itens abaixo:

## Python 2.7
Mac: [http://docs.python-guide.org/en/latest/starting/install/osx/](http://docs.python-guide.org/en/latest/starting/install/osx/)

Linux: [http://www.linuxfromscratch.org/blfs/view/svn/general/python2.html](http://www.linuxfromscratch.org/blfs/view/svn/general/python2.html)

## Pip
[https://packaging.python.org/installing/#install-pip-setuptools-and-wheel](https://packaging.python.org/installing/#install-pip-setuptools-and-wheel)

## Git
[https://git-scm.com/book/en/v2/Getting-Started-Installing-Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)

## Firefox
[https://www.mozilla.org/pt-BR/firefox/new/](https://www.mozilla.org/pt-BR/firefox/new/)

### Instalação

1) Clonando o repositório:
```
git clone https://github.com/raphaelwct/olx-qa.git
```

2) Instalando dependências do projeto
- Entre no diretório do raiz do projeto
- Mude o branch do projeto para develop: 
```
git checkout develop
```
- Execute como root: 
```
pip install -r requirements.pip
```

A partir disso já é possível executar a suite de testes funcionais e de integração do projeto.

## Rodando os testes

### Testes funcionais

* Entre no diretório do raiz do projeto
* Execute o comando abaixo:
```
behave tests/functional/features/
```

### Testes de integração

* Entre no diretório do raiz do projeto
* Execute o comando abaixo:
```
py.test
```

## Visualizando relatório de testes

É possível visualizar o relatório de execução da suite de testes através de uma página web,
para isso siga os passos abaixo:

### Colocando web server disponível para servir relatórios

* Entre no diretório do raiz do projeto
* Execute os comandos abaixo:
```
export FLASK_APP=tests/report.py
flask run
```

### Coletando dados para os relatórios

* Entre no diretório do raiz do projeto
* Execute os comandos abaixo:
```
py.test --html=tests/templates/integration_tests_report.html

behave tests/functional/features/ --format null --summary --multiline > tests/functional/tests_result.txt
```

Agora já é possível visualizar o relatório dos testes da nossa suite, através do endereço:
[http://localhost:5000/](http://localhost:5000/)

## Desenvolvido com

* Python
* Flask
* Behave
* Pytest

## Autor

* **Raphael Santos de Carvalho** - [Linkedin](https://br.linkedin.com/in/raphaelwct)
