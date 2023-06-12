#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>' 

@app.route('/print/<string:route>') #takes one string parameter. .// URL Format 
def print_string(route): #print_string function // route = parameter 
    print(route) #print the string on the console and display it on the web browser.
    return route 

@app.route('/count/<int:number>') #URL Format and number = parameter
def count(number):
    count = f'' #initializes the variable count as an empty string.
    #f before the ' ' is an f-string, allows for the inclusion of expressions within curly braces {}.
    for n in range(number): #starts a loop that iterates the number param aka all numbers.
        #range function generates a sequence of numbers from 0 to number - 1, and the loop assigns each value to the variable n. 
        count += f'{n}\n' #appends the value of n to the count string using the += operator
        #f before the string allows for the inclusion of the value of n within curly braces.
        #'\n' adds a newline character at the end of each appended value to create a new line.
    return count #returns the final value of the count string. It ends the execution of the function and passes the value back to the caller.
#defines a function that takes a parameter called number. It then loops number times, appending each value of n to the count string along with a newline character. Finally, it returns the complete count string. 

@app.route('/math/<int:num1>/<string:operation>/<int:num2>') #URL FORMAT  that defines a route for the Flask application.
def math(num1, num2, operation): #function named 'math' that takes three parameters: num1, num2, and operation.
    if operation == '+': #if statement that checks if the value of the 'operation' parameter is '+'
        return str(num1 + num2) #returns the sum of num1 and num2 as a string.
    
    elif operation == '-': #checks if the value of the 'operation' parameter is '-
        return str(num1 - num2) # returns the difference between num1 and num2 as a string.

    elif operation == '*': #
        return str(num1 * num2) #

    elif operation == 'div':
        return str(num1 / num2)

    elif operation == '%':
        return str(num1 % num2)

    return 'Operation not recognized. Please use one of the following: + - * div %'
# If none of the previous conditions are met, this line returns a string indicating that the provided operation is not recognized.

#defines a Flask route that performs various mathematical operations (addition, subtraction, multiplication, division, and modulo) based on the values provided in the URL parameters. It returns the result of the operation as a string. If the operation is not recognized, it returns a message indicating so.

if __name__ == '__main__':
    app.run(port=5555, debug=True) 