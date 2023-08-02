from flask import Flask,request

app=Flask(__name__)


@app.route('/')
def welcome():
    return 'Welcome to Flask'

@app.route('/cal',methods=['GET'])
def calculator():
    operation=request.json['operation']
    number1=request.json['number1']
    number2=request.json['number2']

    if operation=='add':
        result=number1+number2
    elif operation=='subtract':
        result=number1-number2
    elif operation=='multiply':
        result=number1*number2
    else:
        result=number1/number2

    return f'The operation is {operation} and the result {number1} and {number2} is {result}'


print(f'__name__:{__name__}')

if __name__=='__main__':
    app.run()