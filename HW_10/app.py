from flask import Flask
from flask import render_template
from flask import request
from werkzeug.exceptions import HTTPException
from dotenv import load_dotenv
import csv

load_dotenv('.env')
app = Flask(__name__)


@app.route('/')
def about():
    some_text = ['Перспективный студент. В сентябре 2021 года закончил базовый'
                 ' курс по пайтону на отлично!',
                 'В октябре 2021 года поступил на продвинутый курс по пайтону.'
                 ' Показывает себя как старательного и рудолюбивого студента. '
                 'Всегда старается выполнить домашнее задание на максимальный '
                 'балл. К заданиям имеет творческий подход, если предоставить '
                 'достаточную свободу, то домашнее задание будет уникальным и '
                 'интересным, местами даже очень забавным.']
    return render_template('about.html', some_text=some_text)


@app.route('/index/')
def index():
    data = []
    try:
        with open('timetable.csv') as file:
            some_data = csv.DictReader(file)
            for d in some_data:
                data.append(d)
        return render_template('index.html', data=data)
    except FileNotFoundError as e:
        data = [{'Some_errors': e}]
        return render_template('index.html', data=data)


@app.route('/contact/', methods=['GET', 'POST'])
def contact():
    user_message = {}
    if request.method == 'GET':
        output = render_template('contact.html')
    elif request.method == 'POST':
        user_message['firstname'] = request.form.get('firstname')
        user_message['lastname'] = request.form.get('lastname')
        user_message['email'] = request.form.get('email')
        user_message['message_type'] = request.form.get('message_type')
        user_message['response'] = request.form.get('response')
        user_message['user_message'] = request.form.get('user_message')

        with open('user_message.txt', mode='a') as file:
            for key, value in user_message.items():
                file.write("{:20s}{:4s}\n".format(key, str(value)))

        output = render_template('contact.html')

    return output


@app.errorhandler(HTTPException)
def http_errors(e):
    output = e.description
    if e.code == 404:
        output = render_template('404.html')
    elif e.code == 500:
        output = render_template('500.html')
    return output
