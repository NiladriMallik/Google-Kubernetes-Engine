from flask import Flask
import time

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to the auto-scaling GKE app!"

@app.route('/cpu')
def cpu_intensive():
    x = 0
    for i in range(10**7):
        x += i*i
    return f"CPU load generated! Result: {x}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)