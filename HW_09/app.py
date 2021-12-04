from flask import Flask
from flask import render_template
from faker import Faker
import requests
import base58
import csv


app = Flask(__name__)


@app.route('/')
def main():
    propose = ['информацию о некоторых требованиях к виртуальной среде пайтона;',
               'информацию о рандомных именах, фамилиях и электронных адресах, которую вы же зами можете и генерировать'
               ' указав количество;', 'средний вес и рост сферического коня в вакууме...(внезапно, да?)...;',
               'информацию о количестве астронавтов находящихся в космосе в данную минуту;',
               'закодировать любую строку в формате base58;', 'посмотреть на вашу строку в уже раскодированном виде...']
    output = render_template('main.html', propose=propose)
    return output


@app.route('/requirements/')
def requirements():
    try:
        with open('requirements.txt', 'r') as file:
            some_text = file.read().split('\n')
        output = render_template('requirements.html', some_list=some_text)
        return output
    except FileNotFoundError as e:
        some_error = [e]
        output = render_template('requirements.html', some_list=some_error)
        return output


@app.route('/generate-users/<int:number>')
def generate_users(number):
    fake = Faker()
    fake_users = dict((fake.name(), fake.email()) for i in range(number))
    output = render_template('generate-users.html', users=fake_users)
    return output


@app.route('/mean/')
def mean():
    try:
        with open('hw05.csv') as file:
            data = csv.DictReader(file)
            average_height = 0
            average_weight = 0
            strings_of_data = 0
            for row in data:
                average_height += float(row['Height(Inches)'])
                average_weight += float(row['Weight(Pounds)'])
                strings_of_data += 1

        mean = {'Parsed file:': 'hw05.csv', 'Total values in file (strings of data):': strings_of_data,
                'Average height:': f'{2.54 * average_height} cm', 'Average weight:': f'{0.453592 * average_weight} kg'}
        output = render_template('mean.html', mean=mean)
        return output
    except FileNotFoundError as e:
        mean = {'Parsed file:': e}
        output = render_template('mean.html', mean=mean)
        return output


@app.route('/space/')
def space():
    r = requests.get('http://api.open-notify.org/astros.json')
    astronauts = r.json()['number']
    output = render_template('space.html', number_of_astronauts=f'Now in space {astronauts} people')
    return output


@app.route('/base58encode/<string:string>')
def base58encode(string):
    base58encode = base58.b58encode(string)
    output = render_template('base58encode.html', base58encode=base58encode)
    return output


@app.route('/base58decode/<string:string_in_base58>')
def base58decode(string_in_base58):
    base58decode = base58.b58decode(string_in_base58)
    output = render_template('base58decode.html', base58decode=base58decode)
    return output


app.run(debug=True)
