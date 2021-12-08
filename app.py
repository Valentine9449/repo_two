import uuid

from flask import Flask, render_template
from datetime import datetime
import time

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def first_page():
    return "Hello World"


@app.route('/post/<int:items>')
def main_page(items):
    result = []
    start_time = time.time()
    for item in range(items):
        result.append({})
        result[item]['uuid'] = uuid.uuid4()
        result[item]['elapsed'] = (time.time() - start_time)*1000
        result[item]['time'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return render_template('index.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)
