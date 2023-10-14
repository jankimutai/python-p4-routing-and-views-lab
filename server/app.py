#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route("/print/<string>")
def print_string(string):
    print(f'{string}')
    return f'{string}'

@app.route('/count/<int:num>')
def count(num):
    output = ''
    for i in range(0,num):
        output += str(i) + '\n'
    return output

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation,num2):
    if(operation == '+'):
      result = num1 + num2
    elif (operation == '-'):
       result =  num1 - num2
    elif (operation == '*'):
       result =  num1 * num2
    elif (operation == 'div'):
       result =  num1 / num2
    elif (operation == '%'):
       result =  num1 % num2
    else:
       print('Invalid operation!')
    return str(result)

if __name__ == '__main__':
    app.run(port=5555, debug=True)
