import json
from flask import Flask, make_response, request
from flask_wtf import CSRFProtect
from django.http import HttpResponseRedirect

app = Flask(__name__)
csrf = CSRFProtect()
csrf.init_app(app)

def update_and_show_counter(counter):
    counter += 1
    counter += 8
    print(counter)

counter = 10
update_and_show_counter(counter)

def simplified_code(input_value):
    a, b, c, d = 1, 2, 3, 4
    counter = 1

    if a < b and b < c and c < d:  # Simplified the condition checks
        input_value += c + b + d  # Simplified arithmetic operations
        while counter < 10:
            input_value += a
            counter += 1
        input_value += d + a  # Combined the final operations

    print("Hello there!")
    return make_response(input_value)

@app.route('/xss2')
def index2():
    user_input = request.args.get("input")
    
    # Sanitize the user input to prevent XSS
    sanitized_input = json.dumps(user_input)  # Ensure proper escaping/encoding
    
    return simplified_code(sanitized_input)
