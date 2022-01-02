from flask import Flask
from flask.helpers import url_for
from flask.templating import render_template
import json
from datetime import datetime
import datetime

from werkzeug.utils import redirect
f = open('gym_percents.json')
gym_data = json.load(f)

app = Flask(__name__)

@app.route('/')
def index():
    list_of_days = []
    context = gym_data
    today = datetime.date.today()
    next_1 = today + datetime.timedelta(days=1)
    for i in range(7):
        list_of_days.append(today + datetime.timedelta(days=i))
    list_of_days = [i.strftime("%m/%d/%y") for i in list_of_days]
    date_time = today.strftime("%d/%m/%y %H:%M:%S")
    return render_template('home.html', context=context, date_time=date_time, list_of_days=list_of_days)

@app.route('/marino')
def marino():
    return redirect(url_for('index'))

@app.route('/squashbusters')
def squash():
    return render_template('squash.html', context=gym_data)

if __name__ == "__main__":
    app.run(debug=True)

f.close()