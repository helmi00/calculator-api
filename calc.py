from flask import Flask, request
from flask_restful import Resource, Api
import os
import math

app = Flask(__name__)
api = Api(app)

@app.route('/')
def sayHello():
        return "hello world, this is a calculator backend application that executes the following operations: add, substract, multiply, divide, sqrt, exp and factorial. Have fun :D"


@app.route('/add', methods = ['GET'])
def add():

    arg1 = request.args.get('arg1')
    arg2 = request.args.get('arg2')
    return "result = " + str(float(arg1) + float(arg2))

@app.route('/substract', methods = ['GET'])
def subtract():

    arg1 = request.args.get('arg1')
    arg2 = request.args.get('arg2')
    return "result = " + str(float(arg1) - float(arg2))

@app.route('/multiply', methods = ['GET'])
def multiply():

    arg1 = request.args.get('arg1')
    arg2 = request.args.get('arg2')
    return "result = " + str(float(arg1) * float(arg2))

@app.route('/divide', methods = ['GET'])
def divide():

    arg1 = request.args.get('arg1')
    arg2 = request.args.get('arg2')
    return "result = " + str(float(arg1) / float(arg2))

@app.route('/sqrt', methods = ['GET'])
def sqrt():

    arg1 = request.args.get('arg1')
    return "result = " + str(math.sqrt(float(arg1)))


@app.route('/exp', methods = ['GET'])
def exp():

    arg1 = request.args.get('arg1')
    arg2 = request.args.get('arg2')
    return "result = " + str(float(arg1) ** float(arg2))



def factorial_calcul(x):
        if x == 1:
                return 1
        else:
                return x * factorial_calcul(x - 1)

@app.route('/factorial', methods = ['GET'])
def factorial():
    arg1 = request.args.get('arg1')
    return "result = " + str(factorial_calcul(float(arg1)))

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = int(os.environ.get('PORT', 3000)))
