# -*- coding: utf-8 -*-

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def tests_report():
    return render_template('tests_report.html')


@app.route('/funcional-tests-report')
def functional_tests_report():
    try:
        tests_results_file = open('functional/tests_result.txt', 'r')
        str_file_content = tests_results_file.read()
        functional_tests_info = "<br>".join(str_file_content.split("\n"))
        tests_results_file.close()
    except IOError:
        function_tests_info = u"""
            Não existem ainda resultados da nossa suite de testes funcionais. <br><br>
            Para obter feedback sobre nossos testes funcionais sigua os passos abaixo: <br>
            1) Entre no diretório do projeto <br>
            2) Execute o comando a seguir: <br>
            behave tests/functional/features/ --format null --summary --multiline > tests/functional/tests_result.txt <br><br>
            E em seguida acesse novamente essa url para ver o relatório dos testes.<br>
        """
    return render_template('functional_tests_report.html', functional_tests_info=functional_tests_info)
