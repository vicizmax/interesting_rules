import json
from flask import Flask, make_response, request
from flask_wtf import CSRFProtect
from django.http import HttpResponseRedirect

app = Flask(__name__)
csrf = CSRFProtect()
csrf.init_app(app)

def update_and_show_counter(counter):
    counter += 1

    counter =+ 8
    print(counter)


counter = 10
update_and_show_counter(counter)

def complicated_code(input):
    a=1
    b=2
    c=3
    d=4
    counter = 1

    if a in (a,b,c,d):
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

    print("Hello there!")
    return make_response(input)

@app.route('/xss2')
def index2():

    return complicated_code(request.args.get("input"))
