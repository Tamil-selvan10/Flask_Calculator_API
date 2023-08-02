from flask import Flask,request

app=Flask(__name__)

# __name__ => name of module 
#             by default , main.


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
    # If return type is int, it will throw error.
    # The return type should be string,list,dict and tuple.
     


print(f'__name__:{__name__}')

if __name__=='__main__':
    app.run()

# by default, debug=False . change --> save --> stop --> start
# debug=True.change --> save --> detect change --> reloading
