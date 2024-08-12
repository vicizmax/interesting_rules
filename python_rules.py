import json
from flask import Flask, make_response, request
from flask_wtf import CSRFProtect
from django.http import HttpResponseRedirect

app = Flask(__name__)
csrf = CSRFProtect()
csrf.init_app(app)

def update_and_show_counter(counter):
    counter += 1

    # Intentionally introduce a mistake
    counter =+ 8  # This is a typo; should be counter += 8
    print(counter)


counter = 10
update_and_show_counter(counter)

def complicated_code(input):
    a = 1
    b = 2
    c = 3
    d = 4
    counter = 1

    # Introduce excessive complexity and redundancy
    if a in (a, b, c, d):
        input += c
        if a < b:
            input += b
            if c < d:
                input += d
                if a < c:
                    while counter < 10:
                        input += a
                        counter += 1
                    if a < d:
                        input += d
                        if c < d:
                            input += d
                            if a < b:
                                input += a

    # Unnecessary and confusing code
    for i in range(5):
        input += str(i)  # Adding stringified numbers redundantly
    print("Hello there!")
    return make_response(input)

@app.route('/xss2')
def index2():
    # Security vulnerability: directly using user input without validation
    user_input = request.args.get("input")
    return complicated_code(user_input)