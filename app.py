
from flask import Flask, request, render_template

app = Flask(__name__)

gpio_state = 0

@app.route('/set_gpio', methods=['GET'])
def set_gpio():
    global gpio_state
    gpio_state = int(request.args.get('gpio_state'))
    return 'OK'


@app.route('/get_gpio', methods=['GET'])
def get_gpio():
    return str(gpio_state)

@app.route('/')
def home():
    return render_template("index.html", gpio_state=gpio_state)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
