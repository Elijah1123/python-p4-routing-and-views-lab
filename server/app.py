from flask import Flask

app = Flask(__name__)

# Index route: returns an h1 title as required by test
@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

# Print string route: returns plain text, not HTML
@app.route('/print/<string:param>')
def print_string(param):
    print(param)  # Logs to console
    return param

# Count route: returns numbers on separate lines with a trailing newline
@app.route('/count/<int:param>')
def count(param):
    numbers = '\n'.join(str(i) for i in range(param)) + '\n'
    return numbers

# Math route: supports +, -, *, div, %
@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 == 0:
            return 'Error: Division by zero is not allowed.'
        result = num1 / num2
    elif operation == '%':
        if num2 == 0:
            return 'Error: Modulo by zero is not allowed.'
        result = num1 % num2
    else:
        return 'Invalid operation.'

    return str(result)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
