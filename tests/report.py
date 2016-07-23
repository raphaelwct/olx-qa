# -*- coding: utf-8 -*-

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def tests_report():
    return render_template('tests_report.html')


@app.route('/integration-tests-report')
def integration_tests_report():
    try:
        return render_template('integration_tests_report.html')
    except Exception:
        integration_tests_info = u"""
            Não existem ainda resultados da nossa suite de testes de integração. <br><br>
            Para obter feedback sobre nossos testes de integração siga os passos abaixo: <br>
            1) Entre no diretório do projeto <br>
            2) Execute o comando a seguir: <br>
            py.test --html=tests/templates/integration_tests_report.html <br><br>
            E em seguida acesse novamente essa url para ver o relatório dos testes.<br>
        """
        return render_template('integration_tests_help.html', integration_tests_info=integration_tests_info)


@app.route('/funcional-tests-report')
def functional_tests_report():
    try:
        tests_results_file = open('functional/tests_result.txt', 'r')
        str_file_content = tests_results_file.read()
        functional_tests_info = "<br>".join(str_file_content.split("\n"))
        tests_results_file.close()
        return render_template('functional_tests_report.html', functional_tests_info=functional_tests_info)
    except IOError:
        functional_tests_info = u"""
            Não existem ainda resultados da nossa suite de testes funcionais. <br><br>
            Para obter feedback sobre nossos testes funcionais siga os passos abaixo: <br>
            1) Entre no diretório do projeto <br>
            2) Execute o comando a seguir: <br>
            behave tests/functional/features/ --format null --summary --multiline > tests/functional/tests_result.txt <br><br>
            E em seguida acesse novamente essa url para ver o relatório dos testes.<br>
        """
        return render_template('functional_tests_help.html', functional_tests_info=functional_tests_info)
